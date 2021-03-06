#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from controllers.salesList import SalesList
from helpers.sale import Sale_helper

class SalesList_view(wx.Panel):
    def __init__(self, parent, id):
        self.parent = parent
        self.list_sales_current = self.parent.list_sales_current
        self.helpers_sale = Sale_helper(self.parent)
        wx.Panel.__init__(self, parent, id)

        self.controller = SalesList(self.parent.pos)
        self.controller.get_sales()
        self.controller.get_total_products()
        self.controller.get_total_all()
                
        self.l_venta = wx.StaticText(self, -1, "Ventas")
        self.lc_saleslist = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.lc_saleslist.InsertColumn(0,'') 
        self.lc_saleslist.InsertColumn(1,'id')
        self.lc_saleslist.InsertColumn(2,'SKU')
        self.lc_saleslist.InsertColumn(3,'Venta')
        self.lc_saleslist.InsertColumn(4,'Productos')
        self.lc_saleslist.InsertColumn(5,'Total')
        self.lc_saleslist.SetColumnWidth(0, 50)
        self.lc_saleslist.SetColumnWidth(1, 50)
        self.lc_saleslist.SetColumnWidth(2, 130)
        self.lc_saleslist.SetColumnWidth(3, 210)
        self.lc_saleslist.SetColumnWidth(4, 100)
        self.lc_saleslist.SetColumnWidth(5, 200)
        
        self.list_sales()

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.details_sale, self.lc_saleslist)
        
        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.l_venta.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))

    def __do_layout(self):
        self.s_saleslist = wx.BoxSizer(wx.VERTICAL)
        self.s_saleslist.Add(self.l_venta, 0, wx.ALL, 10)
        self.s_saleslist.Add(self.lc_saleslist, 1, wx.EXPAND, 10)
        self.SetSizer(self.s_saleslist)
        self.s_saleslist.Fit(self)

    def list_sales(self):
	    """
	    Obtiene la lista de ventas por pos al iniciar el turno
	    y crea la lista que guardara la lista de ventas actuales
	    """
	    list_sale_current_temp = []
	    if not self.list_sales_current:
		    """
		    Cuando la venta se realiza al momento, sin tener ventas pendientes ni vendidas
		    """
		    for i in range(0, len(self.controller.sales)):
			    sku = unicode(self.controller.sales[i][1])
			    sale = unicode(self.controller.sales[i][2])
			    amount = unicode(self.controller.total_products[i]['amount__sum'])
			    total = unicode(self.controller.total[i])
			    ids = i+1
			    if  not self.list_sales_current:
				    self.list_sales_current.append({'id': ids,'sku': sku, 'sale': sale, 'amount': amount, 'total': total, 'products': []})
	    else:
		    print "self.controller.sales", self.controller.sales
		    for i in range(0, len(self.controller.sales)):
			    sku = unicode(self.controller.sales[i][1])
			    sale = unicode(self.controller.sales[i][2])
			    amount = unicode(self.controller.total_products[i]['amount__sum'])
			    total = unicode(self.controller.total[i])
			    ids = i+1
			    #print "self.list_sales_current", self.list_sales_current
			    for item in self.list_sales_current:
				    if item['id'] != ids and item['sku'] != '--': #and not item['total'] == total and not item['amount'] == int(amount):
					    """
					    Cuando la venta se realiza al momento, sin tener ventas pendientes listadas solo vendidas
					    """
					    try:
						    self.list_sales_current.index({'id': ids,'sku': sku, 'sale': sale, 'amount': amount, 'total': total, 'products': item['products']})
					    except:
						    try:
							    list_sale_current_temp.index({'id': ids,'sku': sku, 'sale': sale, 'amount': amount, 'total': total, 'products': item['products']})
						    except:
							    list_sale_current_temp.append({'id': ids,'sku': sku, 'sale': sale, 'amount': amount, 'total': total, 'products': item['products']})
				    elif item['sku'] == '--' and item['total'] == total and item['amount'] == int(amount):
					    """
					    Cuando la venta pendiente se termina de hacer con listado de ventas realizadas
					    """
					    self.list_sales_current.remove(item)
		    
		    for item in list_sale_current_temp:
			    self.list_sales_current.append(item)
		    
	    self.lc_saleslist.DeleteAllItems()

	    for item in self.list_sales_current:
		    index = self.lc_saleslist.InsertStringItem(0, '')
		    self.lc_saleslist.SetStringItem(index,1, unicode(item['id']))
		    self.lc_saleslist.SetStringItem(index,2, unicode(item['sku']))
		    self.lc_saleslist.SetStringItem(index,3, unicode(item['sale']))
		    self.lc_saleslist.SetStringItem(index,4, unicode(item['amount']))
		    self.lc_saleslist.SetStringItem(index,5, unicode(item['total']))

    def details_sale(self, evt):
	    currentItem = evt.m_itemIndex
	    current_id = int(self.helpers_sale.get_column_text(self.lc_saleslist, currentItem, 1))
	    self.parent.sale_id = current_id
	    self.helpers_sale.get_details_sale(self.list_sales_current, current_id)


