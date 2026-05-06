from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from security import verify_password, get_password_hash, create_access_token, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

app = FastAPI()
@app.get("/")
async def root():
    """
    Root endpoint to verify the API is running.
    """
    return {
        "status": "online",
        "message": "Welcome to the FastAPI Authentication Module! Navigate to /docs to explore the API."
    }
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "testuser": {
        "username": "testuser",
        "email": "testuser@example.com",
        # Hashed version of "secretpassword123"
        "hashed_password": get_password_hash("secretpassword123"), 
    }
}
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    email: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

async def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = fake_users_db.get(username)
    if user is None:
        raise credentials_exception
        
    return User(**user)


@app.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):

    if user.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    hashed_password = get_password_hash(user.password)

    fake_users_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
    }
    
    return {"username": user.username, "email": user.email}

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    user_dict = fake_users_db.get(form_data.username)
    
    if not user_dict or not verify_password(form_data.password, user_dict["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_dict["username"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):

    return current_user