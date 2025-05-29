from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.config import settings
from app.database import SessionLocal
from app.schemas import TokenPayload
from app.models import *
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db ():

    '''
        Dependency to get a database session.
        Input:
            - None
        Output:
            - A database session object
    '''

    # Create a new database session using the SessionLocal factory.
    db = SessionLocal()

    # Ensure the session is closed after use, even if an error occurs.
    try:
        yield db

    # If an error occurs, rollback the session to avoid leaving it in a broken state.
    finally:
        db.close()



def get_current_user (token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    '''
        Dependency to get the current user from the JWT token.
        Input:
            - token: The JWT token from the request header
            - db: The database session
        Output:
            - The user object if the token is valid, otherwise raises an HTTP exception
    '''

    # Raise an HTTP exception if the token is not provided or invalid.
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"},
    )

    # Decode the JWT token to get the payload.
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms = [settings.JWT_ALGORITHM])
        token_data = TokenPayload(**payload)
    
    # If the token is invalid or expired, raise an HTTP exception.
    except JWTError:
        raise credentials_exception
    
    # Query the database to find the user by username from the token payload.
    # user = db.query(models.User).filter(models.User.username == token_data.sub).first()
    user = db.query(models.User).filter(models.User.id == int(token_data.sub)).first()
    
    # If the user is not found, raise an HTTP exception.
    if user is None:
        raise credentials_exception
    
    # Return the user object if found.
    return user