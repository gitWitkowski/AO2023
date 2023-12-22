# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class GUI
###########################################################################

class GUI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OCR", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,300 ), wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.wxPanel_image = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.wxPanel_image.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer2.Add( self.wxPanel_image, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer4.SetMinSize( wx.Size( 200,300 ) )
		self.wxButton_loadFile = wx.Button( self, wx.ID_ANY, u"Wczytaj obraz", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.wxButton_loadFile, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.wxButton_OCR = wx.Button( self, wx.ID_ANY, u"OCR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.wxButton_OCR, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.textCtrl_outputText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.textCtrl_outputText.SetMinSize( wx.Size( -1,150 ) )

		bSizer4.Add( self.textCtrl_outputText, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.wxButton_copy = wx.Button( self, wx.ID_ANY, u"Skopiuj tekst", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.wxButton_copy, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.wxButton_loadFile.Bind( wx.EVT_BUTTON, self.wxButton_loadFileOnButtonClick )
		self.wxButton_OCR.Bind( wx.EVT_BUTTON, self.wxButton_OCROnButtonClick )
		self.wxButton_copy.Bind( wx.EVT_BUTTON, self.wxButton_copyOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def wxButton_loadFileOnButtonClick( self, event ):
		event.Skip()

	def wxButton_OCROnButtonClick( self, event ):
		event.Skip()

	def wxButton_copyOnButtonClick( self, event ):
		event.Skip()


