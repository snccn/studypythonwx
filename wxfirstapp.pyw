#!/usr/bin/env python
#code in utf-8
#date 2015 10 10
#author snccn

from wx import *
from time import ctime as time
from os import *

app = wx.PySimpleApp()
frame = wx.Frame(parent=None)
frame.SetToolTip(wx.ToolTip("this is frame"))
frame.SetPosition(wx.Point(0,0))
frame.SetSize(wx.Size(300,250))
frame.SetTitle("tesing python wx")
frame.Show(True)

menubar=wx.MenuBar()
_file=wx.Menu()
_edit=wx.Menu()
_help=wx.Menu()

# _file menu defination
_file.Append(101,'&open',"Open a new file")
_file.AppendSeparator()
_file.Append(102,'&save',"Save the file")
_file.AppendSeparator()
_file.Append(103,'&exit',"Exit NOW")

# _edit file defination
app.MainLoop()