#!/usr/bin/env python
# -*- coding: utf-8 -*-

from japos.stockrooms.models import StockRoom
from japos.sales.models import ShoppingCart, Sale as Sale_model
from japos.openings.models import Opening
from django.db.models import Max

class Base_model:
    def __init__(self):
        pass

    def get_cart_id(self):
	    q = ShoppingCart.objects.all().aggregate(Max('pk')).values()
	    return q[0]
    
    def get_opening_id(self):
	    q = Opening.objects.all().aggregate(Max('pk')).values()
	    return q[0]

    def get_sale_id(self):
	    q = Sale_model.objects.all().aggregate(Max('pk')).values()
	    return q[0]
