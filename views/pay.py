#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Sat Dec  5 16:54:09 2009

import wx

from controllers.pay import Pay_controller

# begin wxGlade: extracode
# end wxGlade



class Pay_view(wx.Dialog):
    def __init__(self, parent, id):
        wx.Dialog.__init__(self, parent, id)

        self.parent = parent
        self.controller_pay = Pay_controller()
		    
        self.get_total()

        self.p_total = wx.Panel(self, -1)
        self.p_due = wx.Panel(self, -1)
        self.p_pay = wx.Panel(self, -1)
        self.bm_cash = wx.BitmapButton(self.p_pay, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/coins.png", wx.BITMAP_TYPE_ANY))
        self.bm_card = wx.BitmapButton(self.p_pay, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/credit_card.png", wx.BITMAP_TYPE_ANY))
        self.sl_pay = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)

        self.controller_pay.get_data_pay()
        self.cb_salesman = wx.ComboBox(self, -1, choices = self.controller_pay.choices_salesman, style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.cb_coins = wx.ComboBox(self, -1, choices= self.controller_pay.choices_coins, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.l_before = wx.StaticText(self, -1, "Pagado")
        self.l_vbefore = wx.StaticText(self, -1, "$00.00", style=wx.ALIGN_CENTRE)
        self.l_due = wx.StaticText(self.p_due, -1, "Faltante")
        self.l_vdue = wx.StaticText(self.p_due, -1, "$" + self.total)
        self.tc_total = wx.TextCtrl(self.p_total, -1, self.total)
        self.l_change = wx.StaticText(self.p_total, -1, "Cambio")
        self.l_vchange = wx.StaticText(self.p_total, -1, "$00.00")
        self.b_accept = wx.Button(self, -1, "aceptar")
        self.b_cancel = wx.Button(self, -1, "cancel")
        self.Center()
        self.get_paid()

        self.Bind(wx.EVT_BUTTON, self.close, id = self.b_cancel.GetId())
        self.Bind(wx.EVT_BUTTON, self.accept, id = self.b_accept.GetId())
        self.Bind(wx.EVT_TEXT, self.get_change, id = self.tc_total.GetId())


        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Pay_view.__set_properties
        self.SetTitle("Pago")
        self.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.bm_cash.SetSize(self.bm_cash.GetBestSize())
        self.bm_card.SetSize(self.bm_card.GetBestSize())
        self.p_pay.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.sl_pay.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.cb_salesman.SetSelection(-1)
        self.cb_coins.SetSelection(-1)
        self.l_before.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_vbefore.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_due.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_due.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_vdue.SetForegroundColour(wx.Colour(255, 0, 0))
        self.l_vdue.SetFont(wx.Font(25, wx.DECORATIVE, wx.NORMAL, wx.BOLD, 0, ""))
        self.p_due.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_total.SetMinSize((398, 52))
        self.tc_total.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.tc_total.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_change.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_vchange.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.p_total.SetBackgroundColour(wx.Colour(0, 255, 0))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Pay_view.__do_layout
        s_pay = wx.BoxSizer(wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_total = wx.BoxSizer(wx.VERTICAL)
        s_due = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        s_paymentforms = wx.BoxSizer(wx.HORIZONTAL)
        s_paymentforms.Add(self.bm_cash, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_paymentforms.Add(self.bm_card, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        self.p_pay.SetSizer(s_paymentforms)
        s_pay.Add(self.p_pay, 0, wx.EXPAND, 0)
        s_pay.Add(self.sl_pay, 0, wx.ALL|wx.EXPAND, 10)
        sizer_5.Add(self.cb_salesman, 0, wx.ALL, 10)
        sizer_5.Add(self.cb_coins, 0, wx.ALL, 10)
        sizer_5.Add(self.l_before, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_5.Add(self.l_vbefore, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        s_pay.Add(sizer_5, 0, wx.EXPAND, 0)
        s_due.Add(self.l_due, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)
        s_due.Add(self.l_vdue, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.p_due.SetSizer(s_due)
        s_pay.Add(self.p_due, 0, wx.EXPAND, 0)
        s_total.Add(self.tc_total, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 10)
        s_total.Add(self.l_change, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        s_total.Add(self.l_vchange, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.p_total.SetSizer(s_total)
        s_pay.Add(self.p_total, 0, wx.EXPAND, 0)
        s_buttons.Add(self.b_accept, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_buttons.Add(self.b_cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_pay.Add(s_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(s_pay)
        s_pay.Fit(self)
        self.Layout()
        # end wxGlade

    def accept(self, evt):
	    if self.parent.statusDue:
		    self.parent.l_due = wx.StaticText(self.parent.p_content.p_total, -1, "Faltante")
		    self.parent.l_vdue = wx.StaticText(self.parent.p_content.p_total, -1, "0.000")
		    self.parent.p_content.s_terms.Add(self.parent.l_due, 3, wx.ALIGN_RIGHT, 0)
		    self.parent.p_content.s_values.Add(self.parent.l_vdue, 3, wx.ALIGN_RIGHT, 0)
		    self.parent.p_content.Layout()
		    self.parent.statusDue = False

	    due = float(self.total) - float(self.tc_total.GetValue())
	    if due > 0:
		    self.parent.l_vdue.SetLabel(str(due))
	    else:
		    self.parent.l_vdue.SetLabel('0.000')

	    self.Close()

    def close(self, evt):
	    self.Close()

    def get_paid(self):
	    """
	    Obtiene lo pagodo hasta el momento
	    """
	    if not self.parent.statusDue:
		    paid = float(self.parent.p_content.l_vtotal.GetLabelText()) - float(self.parent.l_vdue.GetLabelText())
		    self.l_vbefore.SetLabel(str(paid))
	
    def get_total(self):
	    """
	    Obtiene el total a pagar y va cambiando conforme realicen pagos,
	    total o parcial, genera el faltante del pago.
	    """
	    if self.parent.statusDue:
	        self.total = self.parent.p_content.l_vtotal.GetLabelText()
	    elif float(self.parent.l_vdue.GetLabelText()) > 0:
		    self.total = self.parent.l_vdue.GetLabelText()
	    else:
		    self.parent.statusDue = False


    def get_change(self, evt):
	    payment = float(self.tc_total.GetValue())
	    change = payment - float(self.total)
	    if change > 0:
	        self.l_vchange.SetLabel(str(change))
	    else:
	        self.l_vchange.SetLabel(str('0'))

# end of class Pay_view


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dlg_pay = MyDialog(None, -1, "")
    app.SetTopWindow(dlg_pay)
    dlg_pay.Show()
    app.MainLoop()
