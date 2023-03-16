"""
This module provides functionality to read an excel file containing
information about people and filter the rows based on a user's input by
communicating with a tcp server.

Functions:
send_message(message: str) -> str:
Sends a message to a server and returns the server's response.

read_request(name: str) -> None
Sends a read request message to a server and returns the server's response.

create_request(name: str) -> None
Sends a create request message to a server and returns the server's response.

update_request(name: str) -> None
Sends a update request message to a server and returns the server's response.

delete_request(name: str) -> None
Sends a delete request message to a server and returns the server's response.
"""

# Built In Imports
import socket


def send_message(message: str) -> str:
    """
    Sends a message to a server and returns the server's response.

    Parameters:
    ----------
    message : str
        The message to be sent to the server.

    Returns:
    -------
    str: The response from the server.
    """

    # create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = ('localhost', 7777)
    client_socket.connect(server_address)

    # send the message
    client_socket.sendall(message.encode())

    # receive the response
    response = client_socket.recv(1024)

    # close the socket
    client_socket.close()

    # return the response
    return response.decode()


def read_request(name: str) -> None:
    """
    Sends a read request message to a server and returns the server's response.

    Parameters:
    ----------
    name : str
        The user name to be read from the server.
    """

    # create the message
    request_message = f"READ {name}"

    # sending message
    return_response = send_message(request_message)
    print(return_response)


def create_request(name: str, age: int, email: str) -> None:
    """
    Sends a create request message to a server and returns the server's response.

    Parameters:
    ----------
    name : str
        The user name to be created in the server.
    age : int
        The age of user to be created in the server.
    email : str
        The email of the user to be created in the server.
    """

    # create the message
    request_message = f"CREATE {name} {age} {email}"

    # sending message
    return_response = send_message(request_message)
    print(return_response)


def update_request(name: str, age: int, email: str) -> None:
    """
    Sends a update request message to a server and returns the server's response.

    Parameters:
    ----------
    name : str
        The user name to be updated in the server.
    age : int
        The age of user to be updated in the server.
    email : str
        The email of the user to be updated in the server.
    """

    # create the message
    request_message = f"UPDATE {name} {age} {email}"

    # sending message
    return_response = send_message(request_message)
    print(return_response)


def delete_request(name: str) -> None:
    """
    Sends a delete request message to a server and returns the server's response.

    Parameters:
    ----------
    name : str
        The user name to be deleted from the server.
    """

    # create the message
    request_message = f"DELETE {name}"

    # sending message
    return_response = send_message(request_message)
    print(return_response)


if __name__ == '__main__':
    #read_request("nisha")
    #create_request(name="nish", age=26, email="tom@example.com")
    #update_request(name="nish", age=32, email="benz@sit.ac.in")
    delete_request("nish")
