__author__ = 'yna1'
import wx
class MainGui(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"This is the Title",size = (200,150))
        panel = wx.Panel(self)

        #ComboBox
        sampleList  = ['Si','Cu','Ta','TaOx','NiFe','CoFe','TrMn']
        global comboBox
        comboBox= wx.ComboBox(panel,500, "default value",pos = (15, 10),
                         size =(160, -1), choices = sampleList,
                         style = wx.CB_DROPDOWN,

                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        comboBox.SetEditable(False)
        print comboBox

        button = wx.Button(panel,501,label = "Click to Confirm",pos = (15,50),size = (160,-1))
        self.Bind(wx.EVT_COMBOBOX, self.printLItem, comboBox)



    def appendToList(item):
        list.append(item)

    #Combobox event
    def printLItem(self,event):
        print " working"
        if hasattr(event, 'getValue'):
            print "it has the attribute"

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MainGui(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
