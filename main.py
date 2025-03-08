#importing fastapi
from fastapi import FastAPI, HTTPException, status; 
from pydantic import BaseModel, Field;
from typing import Optional;
from datetime import date


user_db = {
    'alice': {
        'username': 'alice',
        'date_joined': '2023-01-15',
        'location': 'New York',
        'email': 'alice@example.com',
        'is_active': True,
        'age' : 22
    },
    'bob': {
        'username': 'bob',
        'date_joined': '2023-02-20',
        'location': 'San Francisco',
        'email': 'bob@example.com',
        'is_active': False,
        'age' : 33
    },
    'charlie': {
        'username': 'charlie',
        'date_joined': '2023-03-10',
        'location': 'Chicago',
        'email': 'charlie@example.com',
        'is_active': True,
        'age' : 24
    },
    'dave': {
        'username': 'dave',
        'date_joined': '2023-04-05',
        'location': 'Miami',
        'email': 'dave@example.com',
        'is_active': True,
        'age' : 25
    },
    'eve': {
        'username': 'eve',
        'date_joined': '2023-05-25',
        'location': 'Seattle',
        'email': 'eve@example.com',
        'is_active': False,
        'age' : 26
    },
    'frank': {
        'username': 'frank',
        'date_joined': '2023-06-30',
        'location': 'Austin',
        'email': 'frank@example.com',
        'is_active': True,
        'age' : 10
    },
    'grace': {
        'username': 'grace',
        'date_joined': '2023-07-12',
        'location': 'Denver',
        'email': 'grace@example.com',
        'is_active': True,
        'age' : 60
    },
    'henry': {
        'username': 'henry',
        'date_joined': '2023-08-18',
        'location': 'Boston',
        'email': 'henry@example.com',
        'is_active': False,
        'age' : 24
    },
    'ivy': {
        'username': 'ivy',
        'date_joined': '2023-09-05',
        'location': 'Phoenix',
        'email': 'ivy@example.com',
        'is_active': True,
        'age' : 20
    },
    'jack': {
        'username': 'jack',
        'date_joined': '2023-10-22',
        'location': 'Los Angeles',
        'email': 'jack@example.com',
        'is_active': True,
        'age' : 20
    }
}

class User(BaseModel):
    username : str = Field(min_length= 3, max_length=40)
    date_joined: date
    location: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
    age: int = Field(None, gt=5, lt=120) #ge, le

class UserUpdate(User):
    date_joined: Optional[date] = None
    age: int = Field(None, gt=5, lt=500) #ge, le

def ensure_username_in_db(username:str): 
    if username not in user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User {username} not found")

app = FastAPI();


@app.get('/users')
def get_users_query(limit : int = 30):
    user_list = list(user_db.values());
    return user_list[:limit];


@app.get('/users/{username}')
def get_user_path(username : str):
    ensure_username_in_db(username)
    return user_db[username];


@app.post('/create-user')
def create_user(user : User):
    username = user.username
    if username in user_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"Cannot create user, {username} already exists")
    user_db[username] = user.model_dump()
    return {'message' : f"Successfully created user : {username}"};


@app.delete('/user/{username}')
def delete_user(username : str):
    if username in user_db:
        del user_db[username]
        return {'message' : f"{username} deleted successfully"}
    else:
        return {'message' : f"{username} not found"}
    

@app.put('/user')
def update_user(user : User):
    username = user.username
    ensure_username_in_db(username)
    user_db[username] = user.model_dump()
    return {'message' : f"User {username} updated successfully"}
    
        
@app.patch('/user')
def update_user_partial(user : UserUpdate):
    username = user.username
    ensure_username_in_db(username)
    user_db[username].update(user.model_dump(exclude_unset=True)) 
    return {'message' : f"User {username} updated successfully"}
    
   