"""
This module defines a FastAPI application with endpoints to perform CRUD (Create, Read, Update, Delete)
operations on users.

The endpoints are:
- POST /users: create a new user
- GET /users/{name}: read a user by name
- PUT /users/{name}: update a user by name
- DELETE /users/{name}: delete a user by name

The users are stored in an in-memory (a simple list) database.

This module requires FastAPI, Pydantic, and uvicorn to be installed.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory database (a simple list) to store users
db = []


class User(BaseModel):
    """Model representing a user"""
    name: str
    age: int
    email: str


@app.post("/users")
async def create_user(user: User):
    """Create a new user.

    Args:
        user (User): A user object containing name, age, and email.

    Returns:
        dict: A dictionary containing a message indicating the success of the operation.
    """
    print("Got a message from client:. the messge is")
    print(user.dict())
    db.append(user.dict())
    return {"message": "User created successfully"}


@app.get("/users/{name}")
async def read_user(name: str):
    """Read a user by name.

    Args:
        name (str): The name of the user to read.

    Returns:
        dict: A dictionary containing the user's information, or an error message if the user is not found.
    """
    print("Got a message from client for a read request")
    print(name)
    for user in db:
        if user["name"] == name:
            return user
    return {"error": "User not found"}


@app.get("/users/age/{age}")
async def read_user(age: int):
    """Read a user by name.

    Args:
        name (str): The name of the user to read.

    Returns:
        dict: A dictionary containing the user's information, or an error message if the user is not found.
    """
    print("Got a message from client for a read request")
    print(age)
    for user in db:
        if user["age"] == age:
            return user
    return {"error": "User not found"}


@app.put("/users/{name}")
async def update_user(name: str, user: User):
    """Update a user by name.

    Args:
        name (str): The name of the user to update.
        user (User): A user object containing the updated information.

    Returns:
        dict: A dictionary containing a message indicating the success of the operation, or an error message
         if the user is not found.
    """
    for u in db:
        if u["name"] == name:
            u.update(user.dict())
            return {"message": "User updated successfully"}
    return {"error": "User not found"}


@app.delete("/users/{name}")
async def delete_user(name: str):
    """Delete a user by name.

    Args:
        name (str): The name of the user to delete.

    Returns:
        dict: A dictionary containing a message indicating the success of the operation,
         or an error message if the user is not found.
    """
    for user in db:
        if user["name"] == name:
            db.remove(user)
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}


# Execute the code from the correct folder
#uvicorn http_server_framework_main:app --reload --host 172.18.7.27 --port 9090
