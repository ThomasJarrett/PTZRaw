from socket import *
from datetime import datetime
import re
import translator

import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    connectionSocket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


serverPort = 5678
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr=serverSocket.accept()
focus=(0,0,0,0)
while True:
    #connectionSocket, addr=serverSocket.accept()
    message=connectionSocket.recv(1024)
    print(message)
    message=str(message.hex())
    print(message)
    x=re.match("810104480(.)0(.)0(.)0(.)ff",message)
    if x==None:
        tup=focus
    else:
        tup=x.groups()
    focus=tup
    reply = "90500p0q0r0sff"
    subOuts=['p','q','r','s']
    index=0
    print(tup)
    for s in tup:
        reply=reply.replace(subOuts[index],str(s));
        index+=1
    (reply,temp)=translator.stringToBytes(reply)
    print(reply)

    out=reply
    print(reply)
    connectionSocket.send(out)



connectionSocket.close()

