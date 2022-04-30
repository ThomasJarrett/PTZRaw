import viscaConector
from viscaConector import ViscaConector
import translator
vc=ViscaConector("192.168.1.153")


def changeIP():
    newIP=input("enter new IP: ")
    global vc
    vc.closeSocket()
    vc=ViscaConector(newIP)
    return

while True:
    message, didError = translator.getInput()
    if didError:

        if message=="q":
            break
        if message=="change":
            changeIP()
        if message=="pass":
            output=vc.doResponse()
            print(output)
        print("input wrong")

    if not didError:
        output=vc.sendMessage(message)
        print(output)
vc.closeSocket()