from pydantic import BaseModel, EmailStr
from typing import Optional, List



class UserCreate (BaseModel):

    '''
        Schema for creating a new user.
        This schema is used to validate the input data when creating a new user.
    '''

    # Attributes.
    username: str
    email: EmailStr
    password: str
    is_owner: bool = False



class UserOut (BaseModel):

    '''
        Schema for outputting user data.
        This schema is used to return user data after creation or retrieval.
    '''

    # Attributes.
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_owner: bool


    class Config:

        '''
            Configuration for the Pydantic model.
            This specifies that the model should use ORM mode to read data from ORM models.
        '''

        # This allows the model to read data from ORM models like SQLAlchemy.
        orm_mode = True



class Token (BaseModel):

    '''
        Schema for the authentication token.
        This schema is used to return access and refresh tokens after user login.
    '''

    # Attributes.
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenRefresh(BaseModel):
    """
       Schema for a refresh‐token request.
    """
    refresh_token: str

class TokenPayload (BaseModel):

    '''
        Schema for the payload of the authentication token.
    '''

    # Attributes.
    sub: str
    roles: List[str]
    exp: int