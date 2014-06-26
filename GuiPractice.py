import wx

# ---------------------------------------------------------------------------

class bucky(wx.Frame):
    def __init__(self, parent, id):

        #FRAME
        wx.Frame.__init__(self, parent, id, "This is the param for the Frame Title", size=(300, 200)) #calls the
        #PANEL
        panel = wx.Panel(self)
        #BUTTON
        button = wx.Button(panel, label="exit", pos=(130, 10), size=(60, 30))
        self.Bind(wx.EVT_BUTTON, self.closeButton, button)
        self.Bind(wx.EVT_CLOSE, self.closeWindow)

        ##MENUBAR
        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        first.Append(wx.NewId(), "New Window", "This is a new window")
        first.Append(wx.NewId(), "Open...", "This will open a new window")

        menubar.Append(first, "File")
        menubar.Append(second, "Edit")

        self.SetMenuBar(menubar) #sets the menubar of the frame object

        #MESSAGE DIALOG       parent- The statement                              - Title of the frame  - type of box (question)
        box = wx.MessageDialog(None,'This is the statement param. Ans yes or no?',"Title of the box",wx.YES_NO)
        answer = box.ShowModal()
        box.Destroy() #destroys the box

        #TEXT BOX FOR INPUT
        box2 = wx.TextEntryDialog(None,"This is the question?","This is the title of the Frame","DEFAULT TEXT")
        if box2.ShowModal()==wx.ID_OK:
            answer = box2.GetValue
            print "You pressed OK"

        #List for Input
        box3 = wx.SingleChoiceDialog(None,"What is your favorite food","Title", ["Tuna","Beef","Chicken"])
        if box3.ShowModal()==wx.ID_OK:
            answer = box3.GetStringSelection
            print "You pressed OK"
        elif box3.ShowModal()==wx.ID_CANCEL:
            print "YOU PRESSED CANCLE"

#-----------------------------------------------------------------------------------------------------------------#
    def closeButton(self, event):
        #self.Close(True)
        print("hello")


    def closeWindow(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = bucky(parent=None,id=-1)
    frame.Show()
    app.MainLoop()






