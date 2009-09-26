#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Fri Sep 25 15:16:33 2009

import wx

from stockrooms import Main

from controllers.openings import Opening

# begin wxGlade: extracode
# end wxGlade


class OpeningView(wx.Panel):
    def __init__(self,  parent, id):
        # begin wxGlade: Opening.__init__
        wx.Panel.__init__(self,  parent, id)

        self.controller = Opening()
        self.parent = parent
        
        self.p_inputs = wx.Panel(self, -1)
        self.p_header = wx.Panel(self, -1)
        self.img_logo = wx.StaticBitmap(self.p_header, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/logo.png", wx.BITMAP_TYPE_ANY))
        self.l_opening = wx.StaticText(self.p_header, -1, "Abrir turno", style=wx.ALIGN_CENTRE)
        self.static_line_1 = wx.StaticLine(self.p_header, -1, style=wx.LI_VERTICAL)

        self.controller.get_data_opening(1)
        self.l_pos = wx.StaticText(self.p_inputs, -1, "Point Of Sale")
        self.cb_pos = wx.ComboBox(self.p_inputs, -1, choices=self.controller.choices, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        
        self.controller.get_data_opening(2)
        self.l_cashier = wx.StaticText(self.p_inputs, -1, "Cashier")
        self.cb_cashier = wx.ComboBox(self.p_inputs, -1, choices=self.controller.choices, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        
        self.controller.get_data_opening(3)
        self.l_auditor = wx.StaticText(self.p_inputs, -1, "Auditor")
        self.cb_auditor = wx.ComboBox(self.p_inputs, -1, choices=self.controller.choices, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        
        self.l_initialfund = wx.StaticText(self.p_inputs, -1, "Initial Fund")
        self.tc_initialfund = wx.TextCtrl(self.p_inputs, -1, "")
        self.b_open = wx.Button(self.p_inputs, wx.ID_OPEN, "")
        
        self.Bind(wx.EVT_BUTTON, self.OnCreateOpening, id = self.b_open.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Opening.__set_properties
        self.l_opening.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_opening.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.static_line_1.SetMinSize((251, 1))
        self.static_line_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.p_header.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.l_pos.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cb_pos.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cb_pos.SetSelection(-1)
        self.l_cashier.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cb_cashier.SetSelection(-1)
        self.l_auditor.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.cb_auditor.SetSelection(-1)
        self.l_initialfund.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Opening.__do_layout
        s_opening = wx.BoxSizer(wx.VERTICAL)
        gs_inputs = wx.GridSizer(5, 2, 0, 0)
        s_header = wx.BoxSizer(wx.VERTICAL)
        s_header.Add(self.img_logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_header.Add(self.l_opening, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        s_header.Add(self.static_line_1, 0, wx.ALL|wx.EXPAND, 5)
        self.p_header.SetSizer(s_header)
        s_opening.Add(self.p_header, 0, wx.EXPAND, 0)
        gs_inputs.Add(self.l_pos, 0, wx.EXPAND, 5)
        gs_inputs.Add(self.cb_pos, 0, wx.EXPAND, 5)
        gs_inputs.Add(self.l_cashier, 0, 0, 5)
        gs_inputs.Add(self.cb_cashier, 0, wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5)
        gs_inputs.Add(self.l_auditor, 0, 0, 5)
        gs_inputs.Add(self.cb_auditor, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5)
        gs_inputs.Add(self.l_initialfund, 0, 0, 5)
        gs_inputs.Add(self.tc_initialfund, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        gs_inputs.Add(self.b_open, 1, wx.ALL|wx.ALIGN_RIGHT, 6)
        self.p_inputs.SetSizer(gs_inputs)
        s_opening.Add(self.p_inputs, 0, wx.ALL|wx.EXPAND, 10)
        self.SetSizer(s_opening)
        s_opening.Fit(self)
        # end wxGlade
        
    def OnCreateOpening(self, evt):
        self.main = Main(None, -1)
        self.main.Show()
        self.parent.Close()
        

# end of class Opening

