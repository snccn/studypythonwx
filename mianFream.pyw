#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date 2015 10 10
#author snccn
#filename: wxwithnevigaterbar.pyw
# version alpha 0.01
from wx import *
from time import ctime as tm
from sender import *
class nevigat(wx.Frame):
	def __init__(self,parent,ID,title):
		wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(200,150))
		self.SetSize(wx.Size (400,300))
		menubar=wx.MenuBar()
		panel=wx.Panel(self,-1)
		box=wx.BoxSizer(wx.HORIZONTAL)
		box2=wx.BoxSizer(wx.HORIZONTAL)
		# main menubar defionation
		File=wx.Menu()
		Edit=wx.Menu()
		Help=wx.Menu()
		# File define
		File.Append(101,'&Open',"Open a new file")
		File.Append(102,'&Save',"Save the file")
		File.AppendSeparator()
		File.Append(104,'&Exit',"Quit Now")
		# edit define
		Edit.Append(201,'&Add',"Add elements")
		Edit.Append(202,'&Copy',"Copy from other please")
		Edit.Append(203,'&Flitter',"Cut result with re")
		Edit.AppendSeparator()
		Edit.Append(205,'&Clear',"Clear the result panel")

		# Help define
		Help.Append(301,'&About',"about us")
		# navigaat main define
		menubar.Append(File,'&File')
		menubar.Append(Edit,'&Edit')
		menubar.Append(Help,'&Help')
		# button define
		# box.Add(wx.Button(panel,-1,'Copy',(0,0)),1)
		# box.Add(wx.Button(panel,-1,'Flitter',(0,40)),1)
		# box.Add(wx.Button(panel,-1,'Tools',(0,80)),1)
		panel.SetSizer(box)
		self.Center()
		# static text define
		wx.StaticText(panel,-1,'Strings:',pos=(50,24))
		self.text1=wx.TextCtrl(panel,-1,'',pos=(100,23))
		self.SetMenuBar(menubar)
		# button to exec script
		self.button1=wx.Button(panel,-1,'Run',(230,20))
		self.button1.Bind(wx.EVT_BUTTON,self.OnClick,self.button1)
		# textblank defines
		self.textaera=wx.TextCtrl(self,-1,u'',size=(300,100),pos=(38,80),style=(wx.TE_MULTILINE))
		self.textaera.SetInsertionPoint(0)
		# self.textaera.Bind(wx.EVT_KEY_UP,self.OnSelectAll)
		# event settings to solve the menu actions
		wx.EVT_MENU(self,101,self.Open)
		wx.EVT_MENU(self,102,self.Save)
		wx.EVT_MENU(self,104,self.OnExit)
		wx.EVT_MENU(self,201,self.Add)
		wx.EVT_MENU(self,202,self.Flitter)
		wx.EVT_MENU(self,301,self.About)
		wx.EVT_MENU(self,205,self.Clear)
		# define the import things
		self.database=sender()
	def Open(self,event):
		self.database.select_data(str(1))
		self.textaera.SetValue(str(self.database.select_data(str(1))))
		pass
	def Save(self,event):
		pass
	def Add(self,event):
		pass
	def Flitter(self,event):
		pass
	def OnExit(self,event):
		self.Close()
	def About(self,event):
		dlg=wx.MessageDialog(None,u"transport strings with http \n alpha 0.01 !",u"About us",wx.YES_NO|wx.ICON_QUESTION)
		if dlg.ShowModal()==wx.ID_YES:
			pass
		dlg.Destroy()
	def OnSelectAll(self,event):
		if(event.GetKeyCode()==65 and event.ControlDown()):
			self.textaera.SelectAll()
	def OnClick(self,event):
		self.textaera.AppendText(tm()+' '+self.text1.GetValue())
		self.textaera.AppendText('\n')
		pass
	def Clear(self,event):
		self.textaera.Clear()
		pass
class MyApp(wx.App):
	def OnInit(self):
		frame=nevigat(None,-1,"My app")
		frame.Show(True)
		return True
app=MyApp(0)
app.MainLoop()