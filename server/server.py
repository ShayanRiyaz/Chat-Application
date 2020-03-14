from socket import AF_INET, socket,SOCK_STREAM
from threading import Thread
import time
from person import Person

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST,PORT)
MAX_CONNECTIONS = 10


# GLOBAL VARIABLES
persons = []
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR) # Set up server

def broadcast(message, name):
    """
    Send new messages to all clients
    :param msg: bytes["utf8]
    :param name: str
    :return: 
    """
    for person in persons:
        client = person.client
        try:
            client.send(bytes(name,"utf8") + message)
        except Exception as e:
            print("[EXCEPTION]",e)


def client_communication(person):
    """
    Thread to handle all messages from client
    
    Parameters:
    Client : Person

    Output: 
    Return : None

    """
    client = person.client
    #addr = person.addr
    name = client.recv(BUFSIZ).decode("utf 8")

    message = bytes(f"{name} has joined the chat","utf8")
    broadcast(message,name)
    
    #run = True  
    while True:
        try:
            message = client.recv(BUFSIZ)
            #message = person.recv(BUFSIZ)
            print(f"{name}:" ,message.decode("utf8"))
            if message == bytes("{quit}","utf8"):
                #client.send(bytes("{quit}","utf8"))
                client.close()
                persons.remove(person)
                broadcast(f"{name} has left the chat....","")
                
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(message,name+": ")
                print(f"{name}: ", message.decode("utf8"))
                break

        except Exception as e:
            print("[EXCEPTION]",e)
            #run = False
            break

    print("PERFECT")


def wait_for_connection(SERVER):
    """
    wait for connection from new clients, start new thread once connected
    Parameters:
    SERVER : SOCKET
    
    Outputs:
    return: None
    """
    run = True
    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connection to the server at time {time.time()} ")
            Thread(target = client_communication, args =(person,)).start()
        except Exception as e:
            print("[FAILURE TO RUN]")
            run = False
            #break
    print("SERVER CRASHED")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("[STARTED] Waiting for the connection...")
    ACCEPT_THREAD = Thread(target = wait_for_connection, args = (SERVER,))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()


