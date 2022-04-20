import viscaConector
from viscaConector import ViscaConector
import translator
vc=ViscaConector("192.168.1.152")


def changeIP():
    newIP=input("enter new IP: ")
    global vc
    vc.closeSocket()
    vc=ViscaConector(newIP)
    return

while True:
    message, didError = translator.getInput()
    if didError:
        print("input wrong")
        if message=="q":
            break
        if message=="change":
            changeIP()

    if not didError:
        output=vc.sendMessage(message)
        print(output)
vc.closeSocket()