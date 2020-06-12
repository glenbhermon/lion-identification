# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LeoSpy", pos = wx.DefaultPosition, size = wx.Size( 920,538 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Select Image", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem1.SetBitmap( wx.Bitmap( u"Save image 20.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Zoom", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem2.SetBitmap( wx.Bitmap( u"Zoom 20.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Calculate", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem3.SetBitmap( wx.Bitmap( u"calculate 20.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.m_menuItem3 )
		
		self.m_menuItem8 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Compare", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem8.SetBitmap( wx.Bitmap( u"compare 20.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.m_menuItem8 )
		
		self.m_menuItem9 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Clear", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem9.SetBitmap( wx.Bitmap( u"Clear 20.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.m_menuItem9 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem10 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem10.SetBitmap( wx.Bitmap( u"Save 20.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.m_menuItem10 )
		
		self.m_menubar1.Append( self.m_menu2, u"File" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About Us", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Credits", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem5 )
		
		self.m_menubar1.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_bitmap21, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Save as :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer11.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer11, 0, wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_radioBtn2 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Right Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_radioBtn2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Left Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_radioBtn4, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer10.Add( bSizer12, 0, 0, 5 )
		
		
		bSizer121.Add( bSizer10, 0, 0, 5 )
		
		
		bSizer2.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_bpButton1 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"Select 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_bpButton1.SetBitmapPressed( wx.Bitmap( u"Select 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton1.SetBitmapFocus( wx.Bitmap( u"Select 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton1.SetBitmapCurrent( wx.Bitmap( u"Select 50.png", wx.BITMAP_TYPE_ANY ) )
		gSizer1.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer9.Add( gSizer1, 0, 0, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_bpButton5 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"Zoom 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_bpButton5.SetBitmapPressed( wx.Bitmap( u"Zoom 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton5.SetBitmapFocus( wx.Bitmap( u"Zoom 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton5.SetBitmapCurrent( wx.Bitmap( u"Zoom 50.png", wx.BITMAP_TYPE_ANY ) )
		gSizer2.Add( self.m_bpButton5, 0, wx.ALL, 5 )
		
		self.m_bpButton6 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"Calculate 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_bpButton6.SetBitmapPressed( wx.Bitmap( u"Calculate 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton6.SetBitmapFocus( wx.Bitmap( u"Calculate 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton6.SetBitmapCurrent( wx.Bitmap( u"Calculate 50.png", wx.BITMAP_TYPE_ANY ) )
		gSizer2.Add( self.m_bpButton6, 0, wx.ALL, 5 )
		
		self.m_bpButton7 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"Compare 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_bpButton7.SetBitmapPressed( wx.Bitmap( u"Compare 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton7.SetBitmapFocus( wx.Bitmap( u"Compare 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton7.SetBitmapCurrent( wx.Bitmap( u"Compare 50.png", wx.BITMAP_TYPE_ANY ) )
		gSizer2.Add( self.m_bpButton7, 0, wx.ALL, 5 )
		
		self.m_bpButton8 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"Save 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_bpButton8.SetBitmapPressed( wx.Bitmap( u"Save 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton8.SetBitmapFocus( wx.Bitmap( u"Save 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton8.SetBitmapCurrent( wx.Bitmap( u"Save 50.png", wx.BITMAP_TYPE_ANY ) )
		gSizer2.Add( self.m_bpButton8, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( gSizer2, 0, 0, 5 )
		
		
		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_bpButton4 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"Clear 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.m_bpButton4.SetBitmapPressed( wx.Bitmap( u"Clear 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton4.SetBitmapFocus( wx.Bitmap( u"Clear 50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton4.SetBitmapCurrent( wx.Bitmap( u"Clear 50.png", wx.BITMAP_TYPE_ANY ) )
		bSizer4.Add( self.m_bpButton4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer5.Add( bSizer4, 0, 0, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		self.m_textCtrl2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_textCtrl2.SetForegroundColour( wx.Colour( 128, 0, 255 ) )
		self.m_textCtrl2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer13.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.onBrowse, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.onZoom, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.calculate, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.compare, id = self.m_menuItem8.GetId() )
		self.Bind( wx.EVT_MENU, self.reset, id = self.m_menuItem9.GetId() )
		self.Bind( wx.EVT_MENU, self.save_cal, id = self.m_menuItem10.GetId() )
		self.m_bitmap21.Bind( wx.EVT_LEFT_DOWN, self.someListener )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.onBrowse )
		self.m_bpButton5.Bind( wx.EVT_BUTTON, self.onZoom )
		self.m_bpButton6.Bind( wx.EVT_BUTTON, self.calculate )
		self.m_bpButton7.Bind( wx.EVT_BUTTON, self.compare )
		self.m_bpButton8.Bind( wx.EVT_BUTTON, self.save_cal )
		self.m_bpButton4.Bind( wx.EVT_BUTTON, self.reset )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onBrowse( self, event ):
		event.Skip()
	
	def onZoom( self, event ):
		event.Skip()
	
	def calculate( self, event ):
		event.Skip()
	
	def compare( self, event ):
		event.Skip()
	
	def reset( self, event ):
		event.Skip()
	
	def save_cal( self, event ):
		event.Skip()
	
	def someListener( self, event ):
		event.Skip()
	
	
	
	
	
	
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Zoom and Crop", pos = wx.DefaultPosition, size = wx.Size( 716,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer6.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton9 = wx.Button( self, wx.ID_ANY, "Crop" , wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )

		#self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"Crop 40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		#self.m_bpButton9.SetBitmapCurrent( wx.Bitmap( u"Crop 50.png", wx.BITMAP_TYPE_ANY ) )
		bSizer7.Add( self.m_bpButton9, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7, 0, 0, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"SaveZoom", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem7 )
		
		self.m_menubar2.Append( self.m_menu3, u"File" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.OnSavePNG )
		self.Bind( wx.EVT_MENU, self.OnSavePNG, id = self.m_menuItem7.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSavePNG( self, event ):
		event.Skip()
	
	

