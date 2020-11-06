import socket
import argparse

class server(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--address", type=str, help="Ip address to listen to")
        parser.add_argument("-p", "--port", type=int, help="Port to listen to")
        args = parser.parse_args()

        self.address = args.address if args.address else "localhost"
        self.port = args.port if args.port else 8092

        self.connect()

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Starting server...')
        s.bind((self.address,self.port))
        s.listen(1)
        print('Waiting for connections...')
        connection, address = s.accept()

        while 1:
            command = input('Shell> ')
            if 'terminate' in command:
                connection.send(command.encode('utf-8'))
                print(connection.recv(1024).decode())
                s.close()
                break

            connection.send(command.encode('utf-8'))
            print(connection.recv(1024).decode())

server()