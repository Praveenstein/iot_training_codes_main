"""
This module provides functionality to read an excel file containing
information about people and filter the rows based on a user's input.

Functions:
read_excel_file(file_path: str, user: str) -> Union[pd.DataFrame, None]:
reads an excel file and returns the row matching the user's input.
"""
# Built In Imports
from typing import Union
import socket

# 3rd party libraries
import pandas as pd


################################################
# Functions for CRUD commands on excel file    #
################################################

def read_excel_file(user: str, file_path: str = "./user.xls") -> Union[pd.DataFrame, None]:
    """
    Reads an excel file and returns the row matching the user's input.

    Parameters:
    ----------
    user : str
        The user to filter by.
    file_path : str
        The path to the excel file.

    Returns:
    -------
    Union[pd.DataFrame, None]
        The row matching the user's input or None if the user is not found.
    """

    # Read the excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Filter the DataFrame to only include rows where the name column matches the user input
    filtered_df = df[df['name'] == user]
    #filtered_df = df[df['email'] == user]

    # Check if the filtered DataFrame has any rows
    if filtered_df.empty:
        return None
    else:
        # Return the first row of the filtered DataFrame
        return filtered_df.iloc[0]


def create_excel_row(name: str, age: int, email: str, file_path: str = "./user.xls") -> None:
    """
    Creates a new row in the excel sheet with the given information.

    Parameters:
    ----------
    name : str
        The name of the person to add.
    age : int
        The age of the person to add.
    email : str
        The email of the person to add.
    file_path : str
        The path to the excel file.
    """
    # Read the excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Add a new row to the DataFrame
    new_row = pd.DataFrame({"name": [name], "age": [age], "email": [email]})
    df = pd.concat([df, new_row], ignore_index=True)

    # Write the updated DataFrame to the excel file
    df.to_excel(file_path, index=False)
    print("Created New Row in Excel sheet")


def update_excel_row(name: str, age: int, email: str, file_path: str = "./user.xls") -> None:
    """
    Updates the row in the excel sheet with the given name.

    Parameters:
    ----------
    name : str
        The name of the person to update.
    age : int
        The new age of the person.
    email : str
        The new email of the person.
    file_path : str
        The path to the excel file.
    """
    # Read the excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Find the row to update
    index = df[df['name'] == name].index

    # Update the row with the new information
    df.loc[index, 'age'] = age
    df.loc[index, 'email'] = email

    # Write the updated DataFrame to the excel file
    df.to_excel(file_path, index=False)

    print("Updated")


def delete_excel_row(name: str, file_path: str = "./user.xls") -> None:
    """
    Deletes the row in the excel sheet with the given name.

    Parameters:
    ----------
    name : str
        The name of the person to delete.
    file_path : str
        The path to the excel file.
    """
    # Read the excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Find the row to delete
    index = df[df['name'] == name].index

    # Delete the row
    df.drop(index, inplace=True)

    # Write the updated DataFrame to the excel file
    df.to_excel(file_path, index=False)

    print("Deleted")


########################################################
# Supporting functions for Server Related services     #
########################################################


def handle_command(command, file_path):
    """
    Handles the given command and returns the result.

    Parameters:
    ----------
    command : str
        The command to execute.
    file_path : str
        The path to the excel file.

    Returns:
    -------
    str
        The result of the command.
    """

    # Split the command into parts and check if it matches a valid command format
    parts = command.split()
    if len(parts) == 2 and parts[0] == "READ":

        # If the command is READ, call read_excel_file with the user input
        user_input = read_excel_file(parts[1], file_path)

        # Check if the user was found in the excel file
        if user_input is not None:

            # Return the user's information in the specified format
            return f"Name: {user_input['name']}, Age: {user_input['age']}, Email: {user_input['email']}"
        else:

            # If the user was not found, return a message indicating that
            return "User not found"
    elif len(parts) == 4 and parts[0] == "CREATE":

        # If the command is CREATE, call create_excel_row with the provided information
        name, age, email = parts[1:]
        create_excel_row(name, int(age), email, file_path)

        # Return a message indicating that the user was created
        return "User created"
    elif len(parts) == 4 and parts[0] == "UPDATE":

        # If the command is UPDATE, call update_excel_row with the provided information
        name, age, email = parts[1:]
        update_excel_row(name, int(age), email, file_path)

        # Return a message indicating that the user was updated
        return "User updated"
    elif len(parts) == 2 and parts[0] == "DELETE":

        # If the command is DELETE, call delete_excel_row with the provided name
        delete_excel_row(parts[1], file_path)

        # Return a message indicating that the user was deleted
        return "User deleted"
    else:

        # If the command does not match a valid format, return an error message
        return "Invalid command"


def start_server(file_path):
    """
    Starts the TCP server and listens for incoming connections.

    Parameters:
    ----------
    file_path : str
        The path to the excel file.
    """
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a localhost and port
    server_socket.bind(('localhost', 7777))

    # Listen for incoming connections
    server_socket.listen(1)

    # Wait for a mqtt_client to connect
    while True:
        print('Waiting for a client to connect...')
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Receive the mqtt_client's command
        command = client_socket.recv(1024).decode()
        print(f"Received command: {command}")

        # Handle the command and send the result back to the mqtt_client
        result = handle_command(command, file_path)
        client_socket.send(result.encode())

        # Close the mqtt_client socket
        client_socket.close()


################################################
# Supporting functions for CRUD commands       #
################################################


def main_read():
    """Reads the excel file and returns the row with the given user name."""
    print(read_excel_file(user="rahul"))


def main_create():
    """Creates a new row in the excel file with the given data."""
    print(create_excel_row(name="ntp", age=19, email="ntp@example.com"))


def main_update():
    """Updates the row with the given name with the new data."""
    print(update_excel_row(name="prasad", age=27, email="prasad_27@example.com"))


def main_delete():
    """Deletes the row with the given name from the excel file."""
    print(delete_excel_row(name="prasad"))


#####################################################
# Supporting functions for Starting the tcp server  #
#####################################################

def main_server():
    """Starts the server with the user.xls file."""
    start_server("./user.xls")


if __name__ == '__main__':
    #main_read()
    #main_create()
    #main_update()
    #main_delete()
    main_server()
