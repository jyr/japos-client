#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
from basemodel import Base_model

from japos.stockrooms.models import StockRoom
from japos.sales.models import ShoppingCart, Sale as Sale_model
from japos.openings.models import Opening
from django.db.models import Max

class Sale:
    def __init__(self):
        self.basemodel = Base_model()

    def get_tax_product(self, name, amount, price):
	    """
	    Formula para obtener el impuesto por producto
	    tax  = (taxPercentage / (100 - taxPercentage)) * price
	    """
	    data = StockRoom.objects.filter(product__name = name).values_list('tax__percentage')
	    taxPercentage = float(data[0][0])
	    tax = ((taxPercentage / (100 - taxPercentage)) * price) * amount
	    return tax

    def add_shopping_cart(self, name, amount, pos):
	    stock = StockRoom.objects.filter(pos__name = pos).get(product__name = name)
	    cart = ShoppingCart(stock_room_id = stock.id)
	    cart.amount = amount
	    cart.save()

	    sale_id = self.basemodel.get_sale_id()
	    cart_id = self.basemodel.get_cart_id()

	    sale = Sale_model.objects.get(pk = sale_id)
	    sale.shopping_cart.add(cart_id)
	    sale.save()

    def create_sale(self):
	    opening_id = self.basemodel.get_opening_id()
	    sale = Sale_model(opening_id = opening_id)
	    
	    try:
		    sale_id = self.basemodel.get_sale_id() + 1
	    except:
		    sale_id = 1
		
	    sale.sku = str(sale_id)
	    sale.save()
	