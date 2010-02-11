#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from controllers.sale import Sale

class Sale_helper:
    """
    Crea el proceso de venta, agrega productos seleccionados
    desde el panel del listado de productos al panel de venta,
    ademas de que genera el total por producto y total de venta

    GetParent = rightPanel
    """
	
    def __init__(self, getparent):
	    self.GetParent = getparent
	    self.controller_sale = Sale()

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

    def get_subtotal(self, lc, l_vsubtotal):
	    self.subtotal = l_vsubtotal
	    count = int(lc.GetItemCount())
	    subtotal = 0

	    for i in range(0, count):
		    subtotal += float(self.get_column_text(lc, i, 3))

	    self.subtotal.SetLabel(str(subtotal))
	    return subtotal

    def get_tax_total(self, lc, l_vstax):
	    self.taxtotal = l_vstax
	    count = int(lc.GetItemCount())
	    totalTax = 0

	    for i in range(0, count):
		    name = self.get_column_text(lc, i, 0)
		    amount = int(self.get_column_text(lc, i, 1))
		    price = float(self.get_column_text(lc, i, 2))
		    totalTax += self.controller_sale.get_tax_product(name, amount, price)

	    self.taxtotal.SetLabel(str(totalTax))
	    return totalTax

    def get_total_sale(self, totalTax, subtotal, l_vtotal):
	    self.saletotal = l_vtotal
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

	    subtotal = self.get_subtotal(self.lc_sale, self.GetParent.wp_right.p_content.l_vsubtotal)
	    taxTotal = self.get_tax_total(self.lc_sale, self.GetParent.wp_right.p_content.l_vstax)
	    self.get_total_sale(taxTotal, subtotal, self.GetParent.wp_right.p_content.l_vtotal)

    def update_sale_info(self, lc, currentIndex, amount):
	    price = self.get_column_text(lc, currentIndex,2)
	    self.set_column_text(lc, currentIndex, 1, str(amount))
	    self.get_total(lc, currentIndex, 3, amount, price)
	    subtotal = self.get_subtotal(lc, self.GetParent.p_content.l_vsubtotal)
	    taxTotal = self.get_tax_total(lc, self.GetParent.p_content.l_vstax)

	    self.get_total_sale(taxTotal, subtotal, self.GetParent.p_content.l_vtotal)
	    sale_current = self.get_products_sale(currentIndex)
	    if subtotal == 0:
		    self.GetParent.list_sales_current[self.GetParent.sale_id-1].clear()
		    self.GetParent.list_sales_current.remove({})

    def search_product(self, name):
	    foundIndex = self.lc_sale.FindItem(-1, name, True)
	    return foundIndex

    def get_products_sale(self, current_id):
	    """
	    Obtiene venta actual con sus productos, para agregarla
	    a la lista de ventas actuales, tambien evita que una venta
	    pendiente se agregue otra vez a la lista de ventas actuales
	    """
	    self.lc_sale = self.GetParent.p_content.lc_sale
	    self.saletotal = self.GetParent.p_content.l_vtotal
	
	    count = int(self.lc_sale.GetItemCount())
	    products_sale_current = []
	    amountSale = 0
	    print count, self.GetParent.statusSale, self.GetParent.statusSalePending
	    if (count and self.GetParent.statusSale) or self.GetParent.statusSalePending:
	        for i in range(0, count):
		        amountSale += int(self.get_column_text(self.lc_sale, i, 1))
		        products_sale_current.append({'name': self.get_column_text(self.lc_sale, i, 0), 'amount': int(self.get_column_text(self.lc_sale, i, 1)),  'price': float(self.get_column_text(self.lc_sale, i, 2)), 'total': float(self.get_column_text(self.lc_sale, i, 3))})

	        if self.GetParent.statusSalePending:
		        """
		        Actualiza los detalles de una venta pendiente y 
		        tambien actualiza la lista de ventas actuales con
		        los datos actualizado de la venta pendiente seleccionada
		        """
		        tmp = []
		        for item in self.GetParent.list_sales_current:
				    if item['id'] == self.GetParent.sale_id:
					    item['total'] = self.saletotal.GetLabel()
					    item['amount'] = amountSale
					    item['products'] = products_sale_current
				    tmp.append(item)
		        self.GetParent.list_sales_current = tmp
		        sale_current = None
	        else:
			    sale_current  = {'id': current_id,'sku': '--', 'sale': '--', 'amount': amountSale, 'total': self.saletotal.GetLabel(), 'products': products_sale_current}
	    else:
		    sale_current = None

	    return sale_current

    def get_details_sale(self, list_sales_current, current_id):
	    for item in list_sales_current:
		    if item['id'] == current_id:
			    self.GetParent.details_sale = item['products']
	    self.GetParent.close_sale_list()