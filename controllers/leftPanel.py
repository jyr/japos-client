#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
from django.db.models import Q
from japos.stockrooms.models import StockRoom

class Stock:
    
    def __init__(self):
        pass
    
    def get_stock(self, pos, search = None):
        self.values = []
        
        if search:
            data = StockRoom.objects.filter(pos__name = pos).filter(
                    Q(product__name__contains = search) |
                    Q(product__barcode__contains = search)
                ).values_list('pk','product__name', 'price', 'stock')
        else:
            data = StockRoom.objects.filter(pos__name = pos).values_list('pk','product__name', 'price', 'stock')
        
        for item in data:
            self.values.append((unicode(item[1]), unicode(item[2]), unicode(item[3])))

        return self.values
    
    def get_info_product(self, name):
        self.info_product = StockRoom.objects.get(product__name = name)
        
        return self.info_product
        
    