#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from platform import Platform
import wx.lib.mixins.listctrl  as  listmix
from helpers.sale import Sale_helper
from views.pay import Pay_view
from views.auth import Auth_view
from views.discount import Discount_view


class SaleListCtrl(wx.ListCtrl, listmix.TextEditMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.TextEditMixin.__init__(self)
        
        self.col_locs = [0]

    def OpenEditor(self, col, row):
        if col == 1:
            b = listmix.TextEditMixin.OpenEditor(self, col, row)

class Sale_view(wx.Panel):
    def __init__(self, parent, id):
        self.parent = parent
        img_leave = Platform("/img/toolbars/exit.png")
        img_delete = Platform("/img/toolbars/delete.png")
        img_printer = Platform("/img/toolbars/printer.png")
        img_discount = Platform("/img/toolbars/discount.png")
        img_pay = Platform("/img/toolbars/pay.png")

        self.helpers_sale = Sale_helper(self.parent)

        wx.Panel.__init__(self, parent, id)
        self.p_toolbarinf = wx.Panel(self, -1, style=wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL)
        self.p_total = wx.Panel(self, -1)
        self.l_sale = wx.StaticText(self, -1, "Venta 2009-22")
        self.lc_sale = SaleListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.lc_sale.InsertColumn(0, "Name")
        self.lc_sale.SetColumnWidth(0, 480)
        self.lc_sale.InsertColumn(1, "Amount")
        self.lc_sale.SetColumnWidth(1, 100)
        self.lc_sale.InsertColumn(2, "Price")
        self.lc_sale.SetColumnWidth(2, 150)
        self.lc_sale.InsertColumn(3, "Total")
        self.lc_sale.SetColumnWidth(3, 150)

        self.l_subtotal = wx.StaticText(self.p_total, -1, "Subtotal:")
        self.l_tax = wx.StaticText(self.p_total, -1, "Impuesto:")
        self.l_total = wx.StaticText(self.p_total, -1, "Total:")
        self.l_vsubtotal = wx.StaticText(self.p_total, -1, "0.000")
        self.l_vstax = wx.StaticText(self.p_total, -1, "0.000")
        self.l_vtotal = wx.StaticText(self.p_total, -1, "0.000")
        self.bm_leave = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap(img_leave.string, wx.BITMAP_TYPE_ANY))
        self.static_line_1 = wx.StaticLine(self.p_toolbarinf, -1)
        self.tc_search = wx.TextCtrl(self.p_toolbarinf, -1, "")
        self.bm_delete = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap(img_delete.string, wx.BITMAP_TYPE_ANY))
        self.static_line_1_copy_1 = wx.StaticLine(self.p_toolbarinf, -1)
        self.bm_printer = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap(img_printer.string, wx.BITMAP_TYPE_ANY))
        self.bm_discount = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap(img_discount.string, wx.BITMAP_TYPE_ANY))
        self.bm_pay = wx.BitmapButton(self.p_toolbarinf, -1, wx.Bitmap(img_pay.string, wx.BITMAP_TYPE_ANY))

        self.Bind(wx.EVT_BUTTON, self.cancel, id = self.bm_delete.GetId())
        self.Bind(wx.EVT_BUTTON, self.leave, id = self.bm_leave.GetId())
        self.Bind(wx.EVT_BUTTON, self.printer, id = self.bm_printer.GetId())
        self.Bind(wx.EVT_BUTTON, self.discount, id = self.bm_discount.GetId())
        self.Bind(wx.EVT_BUTTON, self.pay, id = self.bm_pay.GetId())
        #self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.delete_product, self.lc_sale)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.delete_product, self.lc_sale)       

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.l_sale.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_subtotal.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_tax.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_total.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_vtotal.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.bm_leave.SetSize(self.bm_leave.GetBestSize())
        self.static_line_1.SetMinSize((1, 70))
        self.tc_search.SetMinSize((350, 30))
        self.bm_delete.SetSize(self.bm_delete.GetBestSize())
        self.static_line_1_copy_1.SetMinSize((1, 70))
        self.bm_printer.SetSize(self.bm_pay.GetBestSize())
        self.bm_discount.SetSize(self.bm_pay.GetBestSize())
        self.bm_pay.SetSize(self.bm_pay.GetBestSize())
        self.p_toolbarinf.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))

    def __do_layout(self):
        self.s_sale = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.FlexGridSizer(1, 8, 0, 0)
        self.s_total = wx.BoxSizer(wx.HORIZONTAL)
        self.s_values = wx.BoxSizer(wx.VERTICAL)
        self.s_terms = wx.BoxSizer(wx.VERTICAL)
        self.s_sale.Add(self.l_sale, 0, wx.ALL, 10)
        self.s_sale.Add(self.lc_sale, 1, wx.EXPAND, 0)
        self.s_terms.Add(self.l_subtotal, 0, wx.ALIGN_RIGHT, 0)
        self.s_terms.Add(self.l_tax, 0, wx.ALIGN_RIGHT, 0)
        self.s_terms.Add(self.l_total, 0, wx.ALIGN_RIGHT, 0)
        self.s_total.Add(self.s_terms, 1, 0, 0)
        self.s_values.Add(self.l_vsubtotal, 0, wx.ALIGN_RIGHT, 0)
        self.s_values.Add(self.l_vstax, 0, wx.ALIGN_RIGHT, 0)
        self.s_values.Add(self.l_vtotal, 0, wx.ALIGN_RIGHT, 0)
        self.s_total.Add(self.s_values, 1, wx.EXPAND, 0)
        self.p_total.SetSizer(self.s_total)
        self.s_sale.Add(self.p_total, 0, wx.ALL|wx.EXPAND, 10)
        sizer_7.Add(self.bm_leave, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.static_line_1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_7.Add(self.tc_search, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.bm_delete, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.static_line_1_copy_1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_7.Add(self.bm_printer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.bm_discount, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.bm_pay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        self.p_toolbarinf.SetSizer(sizer_7)
        sizer_7.AddGrowableRow(0)
        sizer_7.AddGrowableCol(1)
        sizer_7.AddGrowableCol(2)
        sizer_7.AddGrowableCol(3)
        self.s_sale.Add(self.p_toolbarinf, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(self.s_sale)
        self.s_sale.Fit(self)

    def cancel(self, evt):
	    """
	    Cierra la venta actual, no la cancela que es diferente.
	    Solamente nunca ejecuta el evento de venta
	    """
	    self.parent.statusSalePending = False
	    self.parent.statusDue = True
	    self.parent.statusDiscount = True
	    self.parent.cancel_sale(None)

    def leave(self, evt):
	    """
	    Salir de la venta sin eliminar los productos, la
	    guarda temporalmente la venta pero no la registra 
	    hasta que se pague.
	    """
	    current_id =  len(self.parent.list_sales_current) + 1
	    sale_current = self.helpers_sale.get_products_sale(current_id)
	    print "SALE CURRENT", sale_current
	    self.parent.statusSalePending = False
	    self.parent.statusDue = True
	    self.parent.statusDiscount = True
	    self.parent.cancel_sale(sale_current)

    def pay(self, evt):
	    """
	    Muestra el dialogo de pago, en dado caso que el faltante sea igual
	    a cero ya no lo muestra, eso significa que el pago fue realizado
	    """
	    if self.lc_sale.GetItemCount() > 0:
		    if self.parent.statusDue:
			    self.pay = Pay_view(self.parent, -1)
			    self.pay.ShowModal()
		    elif float(self.parent.l_vdue.GetLabelText()) > 0 :
			    self.pay = Pay_view(self.parent, -1)
			    self.pay.ShowModal()

    def discount(self, evt):
	    """
	    Genera el descuento y lo aplica, pero debe ser autorizado
	    por un auditor
	    """
	    if self.lc_sale.GetItemCount() > 0 and self.parent.statusDiscount:
		    print "due", self.parent.statusDue
		    if self.parent.statusDue or self.parent.statusDiscount:
			    self.auth = Auth_view(self.parent, -1)
			    self.auth.ShowModal()

		    if self.parent.valid:
			    self.apply_discount()
		    #else:
			#    print "validfalse"
			#    print self.parent.valid

		
    def apply_discount(self):
	    self.discount = Discount_view(None, -1)
	    self.discount.ShowModal()
	    p = float(self.discount.cb_percentage.GetValue())
	    t = float(self.l_vtotal.GetLabel())
	    self.l_discount = wx.StaticText(self.p_total, -1, "Descuento")
	    v = (t * p) / 100
	    total = float(t) - v
	    self.l_vtotal.SetLabel(str(total))
	    self.l_vdiscount = wx.StaticText(self.p_total, -1, self.discount.cb_percentage.GetValue() + "%")
	    self.s_terms.Insert(2, self.l_discount, 0, wx.ALIGN_RIGHT, 0)
	    self.s_values.Insert(2, self.l_vdiscount, 0, wx.ALIGN_RIGHT, 0)
	    self.parent.p_content.Layout()
	    self.parent.statusDiscount = False

    def printer(self, evt ):
	    """
	    Impresion del ticket de venta
	    """
	    pass

    def delete_product(self, evt):
	    currentItem = evt.m_itemIndex
	    amount  = int(evt.GetItem().Text)
	    print amount
	    self.helpers_sale.update_sale_info(self.lc_sale, currentItem, amount)
	    if amount == 0:
		    index = self.lc_sale.GetFocusedItem()
		    self.lc_sale.DeleteItem(index)
		
	    #new = self.lc_sale.GetCacheTo()
	    #amount = self.helpers_sale.get_column_text(self.lc_sale, new, 1)
	    #print amount
# end of class Sale_view


