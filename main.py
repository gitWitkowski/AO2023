#!/usr/bin/env python
import wx
from MainFrame import MainFrame

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MainFrame(None) # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()