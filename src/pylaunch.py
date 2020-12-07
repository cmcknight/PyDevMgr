import os
import glob
import wx
import wx.grid
from MainPanel import MainPanel

class MainFrame(wx.Frame):
    def __init__(self):
        flags = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        super().__init__(None, title='pylaunch', style=flags, size=wx.Size(400,600))
        panel = MainPanel(self)
        self.Bind(wx.EVT_BUTTON, self.__on_close, id=wx.ID_EXIT)
        self.Show()

    def __on_close(self, event):
        print("MainFrame.__on_close")
        self.Destroy()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
