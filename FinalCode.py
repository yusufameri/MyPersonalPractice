import wx

__author__ = 'yna1'


class FinalCode(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, "This is the param for the Frame Title", size=(400, 400))

        #panel
        panel = wx.Panel(self)

        #Box
        box =



if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = FinalCode(parent=None,id=-1)
    frame.Show()
    app.MainLoop()