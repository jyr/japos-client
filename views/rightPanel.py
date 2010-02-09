#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Sep 27 18:58:23 2009

import wx

from views.salesList import SalesList_view
from views.sale import Sale_view
from helpers.sale import Sale_helper

# begin wxGlade: extracode
# end wxGlade



class RightPanel_view(wx.Panel):
    def __init__(self, parent, id, list_sales_current, details_sale):
        # begin wxGlade: RightPanel_view.__init__
        self.statusSale = False
        self.statusSalePending = False
        self.statusDue = True
        self.statusDiscount = True
        self.sale_id = 0 
        self.valid = False
        self.parent = parent

        self.helpers_sale = Sale_helper(self.parent)
        self.list_sales_current = list_sales_current
        self.details_sale = details_sale

        wx.Panel.__init__(self, parent, id)
        self.p_maintoolbar = wx.Panel(self, -1, style=wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL)
        self.bm_opening = wx.BitmapButton(self.p_maintoolbar, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/opening.png", wx.BITMAP_TYPE_ANY))
        self.sl_1 = wx.StaticLine(self.p_maintoolbar, -1)
        self.tc_searchsale = wx.TextCtrl(self.p_maintoolbar, -1, "")
        self.bm_addsale = wx.BitmapButton(self.p_maintoolbar, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/add.png", wx.BITMAP_TYPE_ANY))
        self.sl_2 = wx.StaticLine(self.p_maintoolbar, -1)
        self.bm_cancel = wx.BitmapButton(self.p_maintoolbar, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/cancellation.png", wx.BITMAP_TYPE_ANY))
        self.p_content = SalesList_view(self, -1)

        self.Bind(wx.EVT_BUTTON, self.new_sale, id = self.bm_addsale.GetId())
        self.Bind(wx.EVT_BUTTON, self.cancel_sale, id = self.bm_cancel.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: RightPanel_view.__set_properties
        self.bm_opening.SetSize(self.bm_opening.GetBestSize())
        self.sl_1.SetMinSize((1, 70))
        self.tc_searchsale.SetMinSize((450, 30))
        self.bm_addsale.SetSize(self.bm_addsale.GetBestSize())
        self.sl_2.SetMinSize((1, 70))
        self.bm_cancel.SetSize(self.bm_cancel.GetBestSize())
        self.p_maintoolbar.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RightPanel_view.__do_layout
        self.s_right = wx.BoxSizer(wx.VERTICAL)
        s_maintoolbar = wx.FlexGridSizer(1, 6, 0, 0)
        s_maintoolbar.Add(self.bm_opening, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_maintoolbar.Add(self.sl_1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        s_maintoolbar.Add(self.tc_searchsale, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_maintoolbar.Add(self.bm_addsale, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_maintoolbar.Add(self.sl_2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        s_maintoolbar.Add(self.bm_cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        self.p_maintoolbar.SetSizer(s_maintoolbar)
        s_maintoolbar.AddGrowableRow(0)
        s_maintoolbar.AddGrowableCol(1)
        s_maintoolbar.AddGrowableCol(2)
        s_maintoolbar.AddGrowableCol(3)
        self.s_right.Add(self.p_maintoolbar, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.s_right.Add(self.p_content, 1, wx.EXPAND, 10)
        self.SetSizer(self.s_right)
        self.s_right.Fit(self)

    def new_sale(self, evt):
	    self.statusSale = True
	    self.statusDue = True
	    self.statusDiscount = True
	
	    self.bm_addsale.Disable()
	    self.p_content.Destroy()
	    self.p_content = Sale_view(self, -1)
	    self.s_right.Add(self.p_content, 1, wx.EXPAND, 10)
	    self.Layout()

    def close_sale_list(self):
	    self.bm_addsale.Disable()
	    wx.CallAfter(self.set_details_sale)

    def set_details_sale(self):
	    """
	    Elimina el panel que contiene la lista de ventas
	    actuales y carga la informacion de la venta selecciona
	    al panel de venta.
	    """
	    self.statusSale = False
	    self.statusSalePending = True
	    self.p_content.Destroy()
	    self.p_content = Sale_view(self, -1)
	    self.s_right.Add(self.p_content, -1, wx.EXPAND, 10)
	    self.Layout()

	    lc = self.p_content.lc_sale	
	    for item in self.details_sale:
		    index = lc.InsertStringItem(0, unicode(item['name']))
		    lc.SetStringItem(index,1, unicode(item['amount']))
		    lc.SetStringItem(index,2, unicode(item['price']))
		    lc.SetStringItem(index,3, unicode(item['total']))

	    subtotal = self.helpers_sale.get_subtotal(lc, self.p_content.l_vsubtotal)
	    taxTotal = self.helpers_sale.get_tax_total(lc, self.p_content.l_vstax)
	    self.helpers_sale.get_total_sale(taxTotal, subtotal, self.p_content.l_vtotal)
	
    def cancel_sale(self, sale_current):
	    self.bm_addsale.Enable()
	    self.statusSale = False
	    self.p_content.Destroy()
	    self.p_content = SalesList_view(self, -1)
	    self.s_right.Add(self.p_content, 1, wx.EXPAND, 10)
	    self.get_sale_list(sale_current)
	    self.Layout()

    def pay_close(self):
	    """
	    Se usa para cerrar el dialogo una vez que el pago se completo
	    """
	    self.bm_addsale.Enable()
	    #self.statusSale = False
	    #self.statusDue = True
	    #self.statusDiscount = True
	    self.p_content.Destroy()
	    self.p_content = SalesList_view(self, -1)
	    self.s_right.Add(self.p_content, 1, wx.EXPAND, 10)
	    self.get_sale_list(None)
	    self.Layout()
		

    def get_sale_list(self, sale_current):
	    """
	    Obtiene la lista de ventas con productos pagadas o pendientes
	    que es el resultado de la lista actual mas una venta pagada o pendiente.
	    Si sale_current es None regresara las ventas pagadas solamente.
	    """
	    if sale_current:
		    self.p_content.list_sales_current.append(sale_current)
		    self.set_sale_list(self.p_content.list_sales_current)
	    else:
		    self.set_sale_list(self.p_content.list_sales_current)
		
    def set_sale_list(self, sales_current):
	    """
	    Actualiza la lista de ventas actuales
	    """
	    for item in sales_current:
		    index = self.p_content.lc_saleslist.InsertStringItem(0, '')
		    self.p_content.lc_saleslist.SetStringItem(index,1, unicode(item['id']))
		    self.p_content.lc_saleslist.SetStringItem(index,2, unicode(item['sku']))
		    self.p_content.lc_saleslist.SetStringItem(index,3, unicode(item['sale']))
		    self.p_content.lc_saleslist.SetStringItem(index,4, unicode(item['amount']))
		    self.p_content.lc_saleslist.SetStringItem(index,5, unicode(item['total']))
	    
        # end wxGlade

# end of class RightPanel_view


class MainToolBar(wx.ToolBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainToolBar.__init__
        kwds["style"] = wx.TB_DOCKABLE|wx.TB_3DBUTTONS|wx.TB_TEXT
        wx.ToolBar.__init__(self, *args, **kwds)
        self.AddLabelTool(wx.NewId(), "Abrir turno", wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/opening.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddSeparator()
        self.AddLabelTool(wx.NewId(), "buscar venta", wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/opening.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddSeparator()
        self.AddLabelTool(wx.NewId(), "Nueva venta", wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/add.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.AddLabelTool(wx.NewId(), "Cancelar", wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/toolbars/cancellation.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainToolBar.__set_properties
        self.SetMargins((0, 0))
        self.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainToolBar.__do_layout
        pass
        # end wxGlade

# end of class MainToolBar


