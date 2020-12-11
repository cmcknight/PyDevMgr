import os
import glob
import wx
import wx.grid
from MainPanel import MainPanel

class MainFrame(wx.Frame):
    """
    Main frame for the PyDevMgr application
    """
    def __init__(self):
        super().__init__(None, title='pylaunch', style=wx.CAPTION, size=wx.Size(300,600))


        panel = MainPanel(self)
        self.Bind(wx.EVT_BUTTON, self.__on_close, id=wx.ID_EXIT)
        self.Show()

    def __on_close(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
