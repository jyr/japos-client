#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Tue Sep 22 14:48:23 2009

import wx

# begin wxGlade: extracode
# end wxGlade



class Login(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Login.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.p_data = wx.Panel(self, -1)
        self.s_username_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.s_password_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.s_connect_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.s_data_staticbox = wx.StaticBox(self.p_data, -1, "")
        self.p_header = wx.Panel(self, -1)
        self.img_logo = wx.StaticBitmap(self.p_header, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/logo.png", wx.BITMAP_TYPE_ANY))
        self.l_japos = wx.StaticText(self.p_header, -1, "JAPOS", style=wx.ALIGN_CENTRE)
        self.l_username = wx.StaticText(self.p_data, -1, "Username: ")
        self.cb_username = wx.ComboBox(self.p_data, -1, choices=[], style=wx.CB_DROPDOWN)
        self.l_password = wx.StaticText(self.p_data, -1, "Password: ")
        self.tc_password = wx.TextCtrl(self.p_data, -1, "")
        self.b_login = wx.Button(self.p_data, -1, "Login")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Login.__set_properties
        self.SetTitle("Login")
        self.l_japos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_japos.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.p_header.SetBackgroundColour(wx.Colour(47, 47, 47))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Login.__do_layout
        s_login = wx.BoxSizer(wx.VERTICAL)
        s_data = wx.StaticBoxSizer(self.s_data_staticbox, wx.VERTICAL)
        s_connect = wx.StaticBoxSizer(self.s_connect_staticbox, wx.HORIZONTAL)
        s_password = wx.StaticBoxSizer(self.s_password_staticbox, wx.HORIZONTAL)
        s_username = wx.StaticBoxSizer(self.s_username_staticbox, wx.HORIZONTAL)
        s_header = wx.BoxSizer(wx.VERTICAL)
        s_header.Add(self.img_logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_header.Add(self.l_japos, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.p_header.SetSizer(s_header)
        s_login.Add(self.p_header, 1, wx.EXPAND, 0)
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
        # end wxGlade

# end of class Login


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    f_login = Login(None, -1, "")
    app.SetTopWindow(f_login)
    f_login.Show()
    app.MainLoop()
