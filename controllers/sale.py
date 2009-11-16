#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
from japos.stockrooms.models import StockRoom

class Sale:
    def __init__(self):
        pass

    def get_tax_product(self, name, amount, price):
	    """
	    Formula para obtener el impuesto por producto
	    tax  = (taxPercentage / (100 - taxPercentage)) * price
	    """
	    data = StockRoom.objects.filter(product__name = name).values_list('tax__percentage')
	    taxPercentage = float(data[0][0])
	    tax = ((taxPercentage / (100 - taxPercentage)) * price) * amount
	    return tax