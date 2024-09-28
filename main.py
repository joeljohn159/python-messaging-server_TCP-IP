from server import Server
from node import Node

class Main:
    def main():
        server = Server() #Initializes a Server 
        server.start() # Starts the server, where new users and messaging functionality are handled separately using threads
        try:
            nodeSize = int(input('Enter the number of nodes for Server to initialize : '))
        except:
            print('Invalid Character')
            exit()
            
        nodes = [] # Add all new Nodes connected to the server
        for _ in range(nodeSize):  # Server initialized 2 nodes. 
            node = Node() 
            node.start()
            nodes.append(node)

        try:                #Error handling to prevent keyboard intervention and have a clean exit.
            while True:
                pass
        except KeyboardInterrupt:
            for node in nodes:
                node.shutdown()
            server.servershutdown()

if __name__ == "__main__":
    newMain = Main
    newMain.main()
