import argparse
import socket


class portScanner(object):
    def __init__(self):
      parser = argparse.ArgumentParser("Port scannerby davidfegyver")
      parser.add_argument("-a", "--address", type=str, help="The target hostname or ip", required=True)
      parser.add_argument("-p", "--port", type=str, help="Ports to scan", required=True)
      parser.add_argument("-v", "--verbose", help="Show closed ports", action="store_true")

      args = parser.parse_args()

      self.address = args.address
      self.ports = args.port.split(",")
      self.verbose = args.verbose


      self.portScan()

    
    def portScan(self):
      try:
        targetIp = socket.gethostbyname(self.address)
      except Exception as e:
        print("[E] --- Error: unknown host --- \n Details: %s" % e)
        exit(0)

      print("[!] --- Scan results for %s (%s) ---" % (self.address, targetIp))

      socket.setdefaulttimeout(10)

      for port in self.ports:
        self.connectScan(int(port))

    def connectScan(self,port):
      try:
        connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connectionSocket.connect((self.address, port))
        print("[+] TCP port %d OPEN" % port)

      except:
        if self.verbose:
          print("[-] TCP port %d CLOSED" % port)

      finally:
        connectionSocket.close()


portScanner()
