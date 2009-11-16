#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class Sale_helper:
    """
    Crea el proceso de venta, agrega productos seleccionados
    desde el panel del listado de productos al panel de venta,
    ademas de que genera el total por producto y total de venta
    """
	
    def __init__(self, getparent, controller_sale):
	    self.GetParent = getparent
	    self.controller_sale = controller_sale

    def get_column_text(self, lc, index, col):
	    """
	    Obtiene el valor de la columna del item seleccionado
	    """
	    item = lc.GetItem(index, col)
	    return item.GetText()

    def set_column_text(self, lc, index, col, value):
	    """
	    Asigna un valor a la columna del item seleccionado
	    """
	    lc.SetStringItem(index, col, value)

    def get_total(self, lc, index, col, amount, price):
	    total = amount * float(price)
	    lc.SetStringItem(index, col, str(total))

    def get_subtotal(self, lc):
	    self.subtotal = self.GetParent.wp_right.p_content.l_vsubtotal
	    count = int(lc.GetItemCount())
	    subtotal = 0

	    for i in range(0, count):
		    subtotal += float(self.get_column_text(lc, i, 3))

	    self.subtotal.SetLabel(str(subtotal))
	    return subtotal

    def get_tax_total(self, lc):
	    self.taxtotal = self.GetParent.wp_right.p_content.l_vstax
	    count = int(lc.GetItemCount())
	    totalTax = 0

	    for i in range(0, count):
		    name = self.get_column_text(lc, i, 0)
		    amount = int(self.get_column_text(lc, i, 1))
		    price = float(self.get_column_text(lc, i, 2))
		    totalTax += self.controller_sale.get_tax_product(name, amount, price)

	    self.taxtotal.SetLabel(str(totalTax))
	    return totalTax

    def get_total_sale(self, totalTax, subtotal):
	    self.saletotal = self.GetParent.wp_right.p_content.l_vtotal
	    total = totalTax + subtotal
	    self.saletotal.SetLabel(str(total))

    def insert_product(self,currentIndex, name, price):
	    self.lc_sale = self.GetParent.wp_right.p_content.lc_sale
	    foundIndex = self.search_product(name)
	    count = self.lc_sale.GetItemCount()

	    if count == 0:
	        index = self.lc_sale.InsertStringItem(0,name)
	        self.lc_sale.SetStringItem(index, 1, "1")
	        self.lc_sale.SetStringItem(index, 2, price)
	        self.lc_sale.SetStringItem(index, 3, price)
	        amount = 1
	    elif foundIndex == -1:
	        index = self.lc_sale.InsertStringItem(0,name)
	        self.lc_sale.SetStringItem(index, 1, "1")
	        self.lc_sale.SetStringItem(index, 2, price)
	        self.lc_sale.SetStringItem(index, 3, price)
	        amount = 1
	    else:
	            amount = int(self.get_column_text(self.lc_sale, foundIndex, 1)) + 1
	            self.set_column_text(self.lc_sale, foundIndex, 1, str(amount))
	            self.get_total(self.lc_sale, foundIndex, 3, amount, price)

	    subtotal = self.get_subtotal(self.lc_sale)
	    taxTotal = self.get_tax_total(self.lc_sale)
	    self.get_total_sale(taxTotal, subtotal)

    def search_product(self, name):
	    foundIndex = self.lc_sale.FindItem(-1, name, True)
	    return foundIndex

    def get_products_sale(self, current_id):
	    """
	    Obtiene venta actual con sus productos, para agregarla
	    a la lista de ventas actuales
	    """
	    self.lc_sale = self.GetParent.p_content.lc_sale
	    self.saletotal = self.GetParent.p_content.l_vtotal
	    count = int(self.lc_sale.GetItemCount())
	    products_sale_current = []
	    amountSale = 0
	    
	    if count:
	        for i in range(0, count):
		        amountSale += int(self.get_column_text(self.lc_sale, i, 1))
		        products_sale_current.append({'name': self.get_column_text(self.lc_sale, i, 0), 'amount': int(self.get_column_text(self.lc_sale, i, 1)),  'price': float(self.get_column_text(self.lc_sale, i, 2)), 'total': float(self.get_column_text(self.lc_sale, i, 3))})
		
	        sale_current  = {'id': current_id,'sku': '--', 'sale': '--', 'amount': amountSale, 'total': self.saletotal.GetLabel(), 'products': products_sale_current}
	    else:
		    sale_current = None

	    return sale_current