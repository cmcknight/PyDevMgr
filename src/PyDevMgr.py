#!/usr/bin/env python3

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
        super().__init__(None, title='Python Dev Manager', size=wx.Size(300,600))

        panel = MainPanel(self)
        self.Bind(wx.EVT_BUTTON, self.__on_close, id=wx.ID_EXIT)
        self.Show()

    def __on_close(self, event):
        self.Destroy()

class PyDevMgrApp(wx.App):
    """
    PyDevMgrApp - Custom wxApp class
    """
    def __init__(self):
        super().__init__(redirect=False)

    """
    MacReopenApp - Allows minimized app to be restored from taskbar
    """
    def MacReopenApp(self):
        top = self.GetTopWindow()
        if top and top.IsIconized():
            top.Iconize(False)
        if top:
            top.Raise()



if __name__ == '__main__':
    # app = wx.App(redirect=False)
    app = PyDevMgrApp()
    frame = MainFrame()
    app.MainLoop()
