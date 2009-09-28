#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Sun Sep 27 17:21:35 2009

import wx

# begin wxGlade: extracode
# end wxGlade



class SaleView(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SaleView.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.p_toolbarinf = wx.Panel(self, -1, style=wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL)
        self.p_total = wx.Panel(self, -1)
        self.l_sale = wx.StaticText(self, -1, "Venta 2009-22")
        self.lc_sale = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.l_subtotal = wx.StaticText(self.p_total, -1, "Subtotal:")
        self.l_tax = wx.StaticText(self.p_total, -1, "Impuesto:")
        self.l_total = wx.StaticText(self.p_total, -1, "Total:")
        self.l_vsubtotal = wx.StaticText(self.p_total, -1, "0.000")
        self.l_vstax = wx.StaticText(self.p_total, -1, "0.000")
        self.l_vtotal = wx.StaticText(self.p_total, -1, "0.000")
        self.bitmap_button_2 = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/exit.png", wx.BITMAP_TYPE_ANY))
        self.static_line_1 = wx.StaticLine(self.p_toolbarinf, -1)
        self.text_ctrl_2 = wx.TextCtrl(self.p_toolbarinf, -1, "")
        self.bitmap_button_3 = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/delete.png", wx.BITMAP_TYPE_ANY))
        self.static_line_1_copy_1 = wx.StaticLine(self.p_toolbarinf, -1)
        self.bitmap_button_4 = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/pay.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SaleView.__set_properties
        self.l_sale.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_subtotal.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_tax.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_total.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_vtotal.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        self.static_line_1.SetMinSize((1, 70))
        self.text_ctrl_2.SetMinSize((450, 30))
        self.bitmap_button_3.SetSize(self.bitmap_button_3.GetBestSize())
        self.static_line_1_copy_1.SetMinSize((1, 70))
        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.p_toolbarinf.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SaleView.__do_layout
        s_sale = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.FlexGridSizer(1, 6, 0, 0)
        s_total = wx.BoxSizer(wx.HORIZONTAL)
        s_values = wx.BoxSizer(wx.VERTICAL)
        s_terms = wx.BoxSizer(wx.VERTICAL)
        s_sale.Add(self.l_sale, 0, wx.ALL, 10)
        s_sale.Add(self.lc_sale, 1, wx.EXPAND, 0)
        s_terms.Add(self.l_subtotal, 0, wx.ALIGN_RIGHT, 0)
        s_terms.Add(self.l_tax, 0, wx.ALIGN_RIGHT, 0)
        s_terms.Add(self.l_total, 0, wx.ALIGN_RIGHT, 0)
        s_total.Add(s_terms, 1, 0, 0)
        s_values.Add(self.l_vsubtotal, 0, wx.ALIGN_RIGHT, 0)
        s_values.Add(self.l_vstax, 0, wx.ALIGN_RIGHT, 0)
        s_values.Add(self.l_vtotal, 0, wx.ALIGN_RIGHT, 0)
        s_total.Add(s_values, 1, wx.EXPAND, 0)
        self.p_total.SetSizer(s_total)
        s_sale.Add(self.p_total, 0, wx.ALL|wx.EXPAND, 10)
        sizer_7.Add(self.bitmap_button_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.static_line_1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_7.Add(self.text_ctrl_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.bitmap_button_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.static_line_1_copy_1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_7.Add(self.bitmap_button_4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        self.p_toolbarinf.SetSizer(sizer_7)
        sizer_7.AddGrowableRow(0)
        sizer_7.AddGrowableCol(1)
        sizer_7.AddGrowableCol(2)
        sizer_7.AddGrowableCol(3)
        s_sale.Add(self.p_toolbarinf, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(s_sale)
        s_sale.Fit(self)
        # end wxGlade

# end of class SaleView


