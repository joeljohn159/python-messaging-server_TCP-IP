import socket;
import sys;


# create a socket
def create_socket():
    try:
        global host
        global port 
        global s  
        host = ''
        port = 8989
        s = socket.socket()  
    except socket.error as msg:
        print('Socket creation error : '+str(msg))


#Binding the socket and listing  to connections
def bind_socket():
    try:
        print('Binding the port : ' +str(port))
        s.bind((host,port))
        s.listen()

    except socket.error as msg:
        print('Socket Binding error : ' + str(msg)+'/n'+'Retrying...')
        bind_socket()


