#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from views.leftPanel import LeftPanel_view
from views.rightPanel import RightPanel_view

class Main(wx.Frame):
    def __init__(self, parent, id):
	    self.list_sales_current = []
	    self.details_sale = None
	    self.valid = False

	    wx.Frame.__init__(self, parent, id)
	    self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
	    self.wp_left = LeftPanel_view(self.splitter, -1)
	    self.wp_right = RightPanel_view(self.splitter, -1, self.list_sales_current, self.details_sale, self.valid)
	    self.__set_properties()
	    self.__do_layout()

    def __set_properties(self):
        self.SetTitle("Principal")
        self.wp_left.SetMinSize((341, 641))
        self.wp_left.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.wp_right.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        s_main = wx.BoxSizer(wx.HORIZONTAL)
        self.splitter.SplitVertically(self.wp_left, self.wp_right, 312)
        s_main.Add(self.splitter, 1, wx.ALL|wx.EXPAND, 0)
        self.SetSizer(s_main)
        s_main.Fit(self)
        self.Layout()
