import wx
from viscaConector import ViscaConector
import translator
import time

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)

        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='set focus')

        self.infoBox=wx.StaticText(panel,label="0000")
        self.infoBox.SetLabel("0000")
        my_sizer.Add(self.infoBox, 0, wx.ALL| wx.CENTER,5)

        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        self.my_btn=my_btn;
        down_btn = wx.Button(panel, label="up")
        down_btn.Bind(wx.EVT_BUTTON, self.on_pressUp)
        my_sizer.Add(down_btn, 0, wx.ALL | wx.CENTER, 5)
        down_btn=wx.Button(panel, label="down")
        down_btn.Bind(wx.EVT_BUTTON, self.on_pressDown)
        my_sizer.Add(down_btn,0,wx.ALL | wx.CENTER, 5)
        update_btn=wx.Button(panel, label="update")
        update_btn.Bind(wx.EVT_BUTTON, self.updateText)
        my_sizer.Add(update_btn,0,wx.ALL | wx.CENTER, 5)



        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.currentValue=0
        self.vc=ViscaConector("192.168.1.152")
        self.Show()

        #

    def on_press(self, event):

        value = self.text_ctrl.GetValue()

        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
        (message,didError)=translator.stringToBytes(f"focus {value}")
        if not didError:
            self.vc.sendMessage(message)
            self.updateText()


    def on_pressUp(self,event):
        (message,temp)=translator.stringToBytes(f"focus {hex(self.currentValue+1)[2:].rjust(4,'0')}")
        #print(hex(self.currentValue+1+196608))
        #print(message)

        self.vc.sendMessage(message)
        print("did up")
        self.updateText()


    def on_pressDown(self,event):
        if self.currentValue==0:
            return
        (message,temp) = translator.stringToBytes(f"focus {hex(self.currentValue-1)[2:].rjust(4,'0')}")
        self.vc.sendMessage(message)
        print("did down")
        self.updateText()

    def updateText(self,event=9):
        (v,temp) = translator.stringToBytes("focusPos?")
        time.sleep(.1)
        resp=self.vc.sendMessage(v)
        print("in update")
        print("full response\n",resp)
        resp=resp.splitlines()[0]

        self.infoBox.SetLabel(resp)
        resp=resp.replace(" ","")
        print(resp)




        try:
            self.currentValue=int(resp,16)
        except ValueError:
            print("Value Error")
            if event <= 15:
                print("repeating update")
                self.updateText(event + 1)
                return
            pass




if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()