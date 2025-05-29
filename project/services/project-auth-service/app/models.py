from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base



class User (Base):

    '''
        User model representing a user in the authentication service.
        Attributes:
            - id: Unique identifier for the user
            - username: Unique username for the user
            - email: Unique email address for the user
            - hashed_password: Hashed password for the user
            - is_active: Boolean indicating if the user is active
            - is_owner: Boolean indicating if the user is an owner
    '''

    # SQLAlchemy model for the User table.
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(50), unique = True, index = True, nullable = False)
    email = Column(String(100), unique = True, index = True, nullable = False)
    hashed_password = Column(String(255), nullable = False)
    is_active = Column(Boolean, default = True)
    is_owner = Column(Boolean, default = False)