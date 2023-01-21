import viscaConector
from viscaConector import ViscaConector
import translator

currentIP = "192.168.1.153"
vc = ViscaConector(currentIP)


def changeIP():
    newIP = input("enter new IP: ")
    global vc
    if newIP == "ptz1":
        newIP = "192.168.1.152"
    elif newIP == "ptz2":
        newIP = "192.168.1.153"
    global currentIP
    currentIP = newIP
    vc.closeSocket()
    vc = ViscaConector(newIP)
    return


while True:
    message, didError = translator.getInput()
    if didError:

        if message == "q":
            break
        elif message == "change":
            changeIP()
        elif message == "ip?":
            print(currentIP)
        elif message == "pass":
            output = vc.doResponse()
            print(output)

        print("input wrong")

    if not didError:
        output = vc.sendMessage(message)
        print(output)
vc.closeSocket()