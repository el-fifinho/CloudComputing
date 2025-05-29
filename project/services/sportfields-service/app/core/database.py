from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CA_PATH = BASE_DIR / "certs" / "BaltimoreCyberTrustRoot.crt.pem"

if not CA_PATH.exists():
    raise FileNotFoundError(f"CA file not found at {CA_PATH}")

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={
        "ssl_ca": str(CA_PATH)
    },
    pool_pre_ping=True
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()