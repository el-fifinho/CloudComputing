from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

BASE_DIR = Path(__file__).resolve().parent.parent   #.parent
CA_PATH = BASE_DIR / "certs" / "BaltimoreCyberTrustRoot.crt.pem"

if not CA_PATH.exists():
    raise FileNotFoundError(f"CA file not found at {CA_PATH}")

# Create the SQLAlchemy engine and session local factory.
# engine = create_engine(settings.DATABASE_URL, pool_pre_ping = True)
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={
        "ssl_ca": str(CA_PATH)
    },
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()