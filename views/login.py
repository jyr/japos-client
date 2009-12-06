#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from openings import Opening_view

from controllers.login import Login
# begin wxGlade: extracode
# end wxGlade



class Login_view(wx.Frame):
    def __init__(self, parent, id):
        # begin wxGlade: Login.__init__
        wx.Frame.__init__(self,  parent, id, style=wx.DEFAULT_FRAME_STYLE ^(wx.MAXIMIZE_BOX))

        self.controller = Login()
        
        self.p_data = wx.Panel(self, -1)
        self.s_username_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.s_password_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.s_connect_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.s_data_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.p_header = wx.Panel(self, -1)
        self.img_logo = wx.StaticBitmap(self.p_header, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/logo.png", wx.BITMAP_TYPE_ANY))
        self.l_japos = wx.StaticText(self.p_header, -1, "JAPOS", style=wx.ALIGN_CENTRE)
        self.static_line_1 = wx.StaticLine(self.p_header, -1, style=wx.LI_VERTICAL)
        self.l_username = wx.StaticText(self.p_data, -1, "Username: ")
        self.cb_username = wx.ComboBox(self.p_data, -1, choices=[], style=wx.CB_DROPDOWN)
        self.l_password = wx.StaticText(self.p_data, -1, "Password: ")
        self.tc_password = wx.TextCtrl(self.p_data, -1, "", style=wx.TE_PASSWORD)
        self.b_login = wx.Button(self.p_data, -1, "Login")
        
        self.Bind(wx.EVT_BUTTON, self.OnAuth, id = self.b_login.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Login.__set_properties
        self.SetTitle("Login")
        self.l_japos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_japos.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.static_line_1.SetMinSize((251, 1))
        self.static_line_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.p_header.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.l_username.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_password.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Login.__do_layout
        self.s_login = s_login = wx.BoxSizer(wx.VERTICAL)
        s_data = wx.StaticBoxSizer(self.s_data_staticbox, wx.VERTICAL)
        s_connect = wx.StaticBoxSizer(self.s_connect_staticbox, wx.HORIZONTAL)
        s_password = wx.StaticBoxSizer(self.s_password_staticbox, wx.HORIZONTAL)
        s_username = wx.StaticBoxSizer(self.s_username_staticbox, wx.HORIZONTAL)
        s_header = wx.BoxSizer(wx.VERTICAL)
        s_header.Add(self.img_logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_header.Add(self.l_japos, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        s_header.Add(self.static_line_1, 0, wx.ALL|wx.EXPAND, 5)
        self.p_header.SetSizer(s_header)
        s_login.Add(self.p_header, 0, wx.EXPAND, 0)
        s_username.Add(self.l_username, 0, 0, 0)
        s_username.Add(self.cb_username, 1, 0, 0)
        s_data.Add(s_username, 1, wx.EXPAND, 0)
        s_password.Add(self.l_password, 0, 0, 0)
        s_password.Add(self.tc_password, 1, 0, 0)
        s_data.Add(s_password, 1, wx.EXPAND, 0)
        s_connect.Add(self.b_login, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1)
        s_data.Add(s_connect, 1, wx.EXPAND, 0)
        self.p_data.SetSizer(s_data)
        s_login.Add(self.p_data, 1, wx.EXPAND, 0)
        self.SetSizer(s_login)
        s_login.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnAuth(self, evt):
		username = self.cb_username.GetValue().encode('utf-8')
		password = self.tc_password.GetValue().encode('utf-8')
		try:
			self.valid = self.controller.auth(username, password)
			if self.valid:
				self.p_data.Destroy()
				self.p_header.Destroy()
				opening = Opening_view(self, -1)
			else:
				self.controller.error()
		except: #japos.crews.models.DoesNotExist:
			self.controller.error()
        
def main():
    app = wx.PySimpleApp(0)
    f_login = Login_view(None, -1)
    f_login.Show()
    app.MainLoop()
# end of class Login