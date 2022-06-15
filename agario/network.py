import socket
import pickle

class Network():

    #Intilizing the socket and connecting to server
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("localhost",5001))

    #Send randompoints and this player blob's position to other players
    def send(self,datatobesent):
        msg = pickle.dumps(datatobesent)
        self.s.send(msg)

    #Recieve randompoints and other players blob's position
    def recieve(self):
        msg = self.s.recv(4096)
        fullMsg=pickle.loads(msg)
        return fullMsg