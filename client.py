#!/bin/python3
import socket
import threading

# Choosing Nickname
nickname = input("Введите ваш ник: ")

# Connecting To Server ()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            raise()
            break

def write():
    try:
        while True:
            message = '{}: {}'.format(nickname, input(''))
            client.send(message.encode())
    except:
        raise()
    
# Starting Threads For Listening And Writing
try:
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()    

    write_thread = threading.Thread(target=write)
    write_thread.start()
except Exception as E:
    print("Error start client with error: {}".format(E))