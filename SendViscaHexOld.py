
from socket import *
import translator
#from pip._vendor.distlib.compat import raw_input
import sys







serverName= '192.168.1.152'
serverPort=5678

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#clientSocket=socket(AF_INET, SOCK_DGRAM)
#message=raw_input('Inuput lowercase sentence:')
me=b'8101043f0200ff'
#message=b'0xffa010'
me=b'\x81\x01\x04\x3f\x02\x00\xff'

def sendMessage(message):
    clientSocket.send(message)
    clientSocket.settimeout(1)
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:')
    returnStr=str(modifiedSentence.hex())
    niceStr=""
    for i in range(0,int(len(returnStr)),2):
        niceStr+=returnStr[i:i+2]
        niceStr+=" "
    return translator.translateResponse(niceStr)+"\n"+niceStr

#print(type(message))
#clientSocket.sendto()
while True:
    message=translator.getInput()
    clientSocket.send(message)
    clientSocket.settimeout(1)
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:')
    returnStr=str(modifiedSentence.hex())
    niceStr=""
    for i in range(0,int(len(returnStr)),2):
        niceStr+=returnStr[i:i+2]
        niceStr+=" "
    print(translator.translateResponse(niceStr))
    print(niceStr)




#modifiedSentence = clientSocket.recv(1024)
#print('From Server:', modifiedSentence)
clientSocket.close()


#s=input("Input hexadecimal value: ")
#s = int(s.replace(" ",""),16)
#print(hex(s))
#message=hex(s)

#print(type(message.endcode()))

#clientSocket.sendto(message,(serverName,serverPort))
#modifiedMessage, serverAddress=clientSocket.recvfrom(2048)
#print(modifiedMessage)
#clientSocket.close()
