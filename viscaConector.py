
from socket import *
import translator
#from pip._vendor.distlib.compat import raw_input
import sys

a=5

class ViscaConector:
    def __init__(self,serverName):
        self.serverPort=5678
        self.serverName=serverName
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((serverName, self.serverPort))
        self.clientSocket.settimeout(1)

    def sendMessage(self,message):
        try:
            self.clientSocket.send(message)
        except BrokenPipeError:
            self.resetSocket()
            return

        return self.doResponse()
    def doResponse(self):
        try:
            modifiedSentence = self.clientSocket.recv(1024)
        except timeout:
            return "Socket timeout"

        # print('From Server:')
        returnStr = str(modifiedSentence.hex())
        niceStr = ""
        for i in range(0, int(len(returnStr)), 2):
            niceStr += returnStr[i:i + 2]
            niceStr += " "
        return translator.translateResponse(niceStr) + "\n" + niceStr


    def closeSocket(self):
        self.clientSocket.close()
    def resetSocket(self):
        self.clientSocket.close()
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.serverName, self.serverPort))
        self.clientSocket.settimeout(1)



