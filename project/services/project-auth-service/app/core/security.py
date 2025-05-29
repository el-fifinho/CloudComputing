from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from .config import settings



# Security module for handling password hashing and JWT token creation
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")



def verify_password (plain_password: str, hashed_password: str) -> bool:

    '''
        Verify a plain password against a hashed password.
        Input:
            - plain_password: The password to verify
            - hashed_password: The hashed password to verify against
        Output:
            - True if the password matches, False otherwise
    '''

    # Use the CryptContext to verify the plain password against the hashed password.
    return pwd_context.verify(plain_password, hashed_password)



def get_password_hash (password: str) -> str:

    '''
        Hash a password using bcrypt.
        Input:
            - password: The password to hash
        Output:
            - The hashed password
    '''

    # Hash the password using bcrypt and return the hashed value.
    return pwd_context.hash(password)



def create_access_token (subject: str, roles: list[str]) -> str:

    '''
        Create a JWT access token.
        Input:
            - subject: The subject of the token (the user ID)
            - roles: The roles associated with the user
        Output:
            - The JWT access token as a string
    '''
    
    # Get the current time and calculate the expiration time for the token.
    now = datetime.utcnow()
    exp = now + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "roles": roles, "iat": now, "exp": exp}

    # Encode the payload into a JWT token using the secret key and algorithm specified in the settings.
    return jwt.encode(payload, settings.JWT_SECRET, algorithm = settings.JWT_ALGORITHM)



def create_refresh_token (subject: str) -> str:

    '''
        Create a JWT refresh token.
        Input:
            - subject: The subject of the token (the user ID)
        Output:
            - The JWT refresh token as a string
    '''

    # Get the current time and calculate the expiration time for the refresh token.
    now = datetime.utcnow()
    exp = now + timedelta(minutes = settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "iat": now, "exp": exp}

    # Encode the payload into a JWT token using the secret key and algorithm specified in the settings.
    return jwt.encode(payload, settings.JWT_SECRET, algorithm = settings.JWT_ALGORITHM)