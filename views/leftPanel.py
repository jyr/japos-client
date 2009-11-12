#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Sat Sep 26 16:41:45 2009

import wx
from controllers.leftPanel import Stock
from views.rightPanel import RightPanel_view
from views.sale import Sale_view

# begin wxGlade: extracode
# end wxGlade



class LeftPanel_view(wx.Panel):
    def __init__(self, parent, id):
        self.parent = parent
        self.GetParent = self.parent.GetParent()
        self.controller = Stock()
        self.controller.get_stock()
        
        wx.Panel.__init__(self, parent, id)
        self.p_info = wx.Panel(self, -1, style=wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL)
        self.notebook = wx.Notebook(self, -1, style=0)
        self.notebook_panel = wx.Panel(self.notebook, -1)
        self.bm_logo = wx.StaticBitmap(self, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/09_64x64.png", wx.BITMAP_TYPE_ANY))
        self.l_japos = wx.StaticText(self, -1, "JAPOS")
        self.tc_search = wx.TextCtrl(self.notebook_panel, -1, "", style=wx.TE_PROCESS_ENTER)
        self.l_search = wx.StaticText(self.notebook_panel, -1, "Search...")
        
        self.lc_products = wx.ListCtrl(self.notebook_panel, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.lc_products.InsertColumn(0,'Nombre') 
        self.lc_products.InsertColumn(1,'Precio')
        self.lc_products.InsertColumn(2,'Disponible')
        self.lc_products.SetColumnWidth(0, 150)
        self.lc_products.SetColumnWidth(1, 50)
        self.lc_products.SetColumnWidth(2, 85)

        self.OnList()
            
        self.l_info = wx.StaticText(self, -1, "Informacion del producto:")
        self.bm_product = wx.StaticBitmap(self.p_info, -1, wx.Bitmap("/Users/jyr/Desarrollo/git-projects/japos-client/img/product.png", wx.BITMAP_TYPE_ANY))
        self.l_name = wx.StaticText(self.p_info, -1, "Nombre")
        self.l_available = wx.StaticText(self.p_info, -1, "Disponible: ")
        self.l_barcode = wx.StaticText(self.p_info, -1, "codigo")
        self.l_stock = wx.StaticText(self.p_info, -1, "Existencia: 16")
        self.sl_1 = wx.StaticLine(self.p_info, -1)
        self.l_psale = wx.StaticText(self.p_info, -1, "Precio venta:")
        self.l_vsale = wx.StaticText(self.p_info, -1, "0")
        self.l_discount = wx.StaticText(self.p_info, -1, "Descuento:")
        self.l_vdiscount = wx.StaticText(self.p_info, -1, "0")
        self.l_pbuy = wx.StaticText(self.p_info, -1, "Precio compra:")
        self.l_vbuy = wx.StaticText(self.p_info, -1, "0")
        self.l_tax = wx.StaticText(self.p_info, -1, "Impuesto:")
        self.l_vtax = wx.StaticText(self.p_info, -1, "0")
        self.sl_2 = wx.StaticLine(self.p_info, -1)
        self.l_description = wx.StaticText(self.p_info, -1, "Descripcion del producto aqui")
        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.lc_products)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated, self.lc_products)
        self.tc_search.Bind(wx.EVT_TEXT_ENTER, self.OnSearch)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: LeftPanel_view.__set_properties
        self.l_japos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_japos.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_search.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_info.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_info.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_name.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_available.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_barcode.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_stock.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_psale.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_vsale.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_discount.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_vdiscount.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_pbuy.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_vbuy.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_tax.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_vtax.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_info.SetBackgroundColour(wx.Colour(255, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: LeftPanel_view.__do_layout
        s_left = wx.BoxSizer(wx.VERTICAL)
        s_info = wx.BoxSizer(wx.VERTICAL)
        gs_row2 = wx.FlexGridSizer(2, 4, 0, 0)
        s_info_nombre = wx.BoxSizer(wx.HORIZONTAL)
        gs_row1 = wx.FlexGridSizer(2, 2, 0, 0)
        s_products = wx.BoxSizer(wx.VERTICAL)
        s_left.Add(self.bm_logo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        s_left.Add(self.l_japos, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        s_products.Add(self.tc_search, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        s_products.Add(self.l_search, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 10)
        s_products.Add(self.lc_products, 1, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 10)
        self.notebook_panel.SetSizer(s_products)
        self.notebook.AddPage(self.notebook_panel, "Productos")
        s_left.Add(self.notebook, 2, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 10)
        s_left.Add(self.l_info, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        s_info_nombre.Add(self.bm_product, 0, wx.LEFT|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5)
        gs_row1.Add(self.l_name, 0, wx.RIGHT|wx.EXPAND, 10)
        gs_row1.Add(self.l_available, 0, wx.RIGHT|wx.ALIGN_RIGHT, 15)
        gs_row1.Add(self.l_barcode, 0, wx.RIGHT|wx.EXPAND, 15)
        gs_row1.Add(self.l_stock, 0, wx.RIGHT|wx.ALIGN_RIGHT, 15)
        gs_row1.AddGrowableCol(0)
        gs_row1.AddGrowableCol(2)
        s_info_nombre.Add(gs_row1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10)
        s_info.Add(s_info_nombre, 0, wx.EXPAND, 0)
        s_info.Add(self.sl_1, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 10)
        gs_row2.Add(self.l_psale, 0, 0, 10)
        gs_row2.Add(self.l_vsale, 0, 0, 10)
        gs_row2.Add(self.l_discount, 0, 0, 10)
        gs_row2.Add(self.l_vdiscount, 0, wx.RIGHT|wx.ALIGN_RIGHT, 10)
        gs_row2.Add(self.l_pbuy, 0, 0, 0)
        gs_row2.Add(self.l_vbuy, 0, 0, 0)
        gs_row2.Add(self.l_tax, 0, 0, 0)
        gs_row2.Add(self.l_vtax, 0, 0, 0)
        gs_row2.AddGrowableCol(1)
        s_info.Add(gs_row2, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        s_info.Add(self.sl_2, 0, wx.ALL|wx.EXPAND, 10)
        s_info.Add(self.l_description, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 10)
        self.p_info.SetSizer(s_info)
        s_left.Add(self.p_info, 0, wx.ALL|wx.EXPAND, 10)
        self.SetSizer(s_left)
        s_left.Fit(self)
        # end wxGlade

    def OnSearch(self, evt):
        self.lc_products.DeleteAllItems()
        name = self.tc_search.GetValue()
        self.controller.get_stock(name)
        self.OnList()

    def OnList(self):
        for data in self.controller.values:
            index = self.lc_products.InsertStringItem(0, data[0])
            self.lc_products.SetStringItem(index,1, data[1])
            self.lc_products.SetStringItem(index,2, data[2])
            
    def OnItemSelected(self, evt):
	    """
	    Selecciona un producto y muestra su informacion a detalle
	    """
	    self.currentItem = evt.m_itemIndex
	    name = self.lc_products.GetItemText(self.currentItem)
	    self.OnSetInfoProduct(name)

    def OnItemActivated(self, evt):
	    """
	    Agrega un producto a la venta, cuando presionan enter sobre el producto
	    o al dar doble click sobre el.
	    """
	    if self.GetParent.wp_right.statusSale:
		    print "Agregando el producto..."
	    else:
			print "Crear venta"

    def OnSetInfoProduct(self, name):
        self.controller.get_info_product(name)
        self.p_info.Layout()
        self.l_name.SetLabel(self.controller.info_product.product.name)
        self.l_available.SetLabel(" Disponible "+str(self.controller.info_product.product.stock))
        self.l_barcode.SetLabel(str(self.controller.info_product.product.barcode))
        self.l_stock.SetLabel(" Existencia " + str(self.controller.info_product.stock))
        self.l_vsale.SetLabel(str(self.controller.info_product.price))
        self.l_vdiscount.SetLabel(str(self.controller.info_product.product.discount))
        self.l_vbuy.SetLabel(str(self.controller.info_product.product.purchase_price))
        self.l_vtax.SetLabel(str(self.controller.info_product.tax))
        self.l_description.SetLabel(str(self.controller.info_product.product.description))
# end of class LeftPanel_view


