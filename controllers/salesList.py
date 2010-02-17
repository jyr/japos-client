#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
from basemodel import Base_model

from django.db.models import Sum, Max
from japos.pos.models import Pos
from japos.openings.models import Opening
from japos.sales.models import Sale

class SalesList:
    def __init__(self, pos):
        self.basemodel = Base_model()
        self.opening_id = self.basemodel.get_opening_id()
        self.pos = pos
        self.get_id_pos()
        self.get_opening()
        self.data = Sale.objects.filter(opening__pos = self.pos_id).filter(opening__pk = self.opening_id)
        self.get_price_product_all()
        self.get_amount_product_all()
        self.get_subtotal_all()
        self.get_tax_product_all()
        self.get_tax_value_all()
        self.get_price_discount_all()
        self.get_sale_price()

    def get_id_pos(self):
	    pos_id  =  Pos.objects.get(name = self.pos)
	    self.pos_id = pos_id.pk

    def get_opening(self):
	    q = Opening.objects.all().aggregate(Max('pk')).values()
	    self.opening = q[0]
	
    def get_sales(self):
        """
            Listado de todas las ventas
        """
        self.sales = []
        self.sales = Sale.objects.filter(opening__pos = self.pos_id).filter(opening__pk = self.opening_id).values_list('pk', 'sku', 'date_created')
        
        return self.sales

    def get_total_products(self):
        """
            Obtiene el total de productos por venta
        """
        self.total_products = []
        
        for item in self.data:
            self.total_products.append(item.shopping_cart.aggregate(Sum('amount')))
            
        return self.total_products

    def get_price_product_all(self):
        """
            Obtiene el precio del almacen del producto vendido
        """
        self.price_product = []

        for item in self.data:
            self.price_product.append(item.shopping_cart.values_list('stock_room__price'))
        return self.price_product
    
    def get_amount_product_all(self):
        """
            Obtiene la cantidad por producto vendida
        """
        self.amount_product = []
        
        for item in self.data:
            self.amount_product.append(item.shopping_cart.values_list('amount'))
        
        return self.amount_product
    
    def get_subtotal_all(self):
        self.subtotal = []
        
        for i in range(0,len(self.amount_product)):
            subtotal=0
            for j in range(0,len(self.amount_product[i])):
                subtotal += self.amount_product[i][j][0]*self.price_product[i][j][0]
            self.subtotal.append(subtotal)
        return self.subtotal

    def get_price_discount_all(self):
        """
            Calcula el precio con descuento
        """
        value = []
        self.price_discount = []
                
        for item in self.data:
            value.append(item.shopping_cart.values_list('stock_room__discount__percentage'))

        for i in range(0,len(self.price_product)):
            tmp = 0.0
            for j in range(0, len(self.price_product[i])):
                if value[i][j][0]:
                    discount = (100.0 - float(value[i][j][0])) / 100.0
                    self.price_discount.append( self.price_product[i][j][0] * discount)
                else:
                    self.price_discount.append(0.00)
        return self.price_discount

    def get_tax_product_all(self):
        """
            Convierte el porcentaje del impuesto a decimal
        """
        self.tax_product = []
        value = []
                
        for item in self.data:
            value.append(item.shopping_cart.values_list('stock_room__tax__percentage'))

        for i in range(0, len(value)):
            for j in range(0, len(value[i])):
                if value[i][j][0]:
                    self.tax_product.append(float(value[i][j][0] /(100 - value[i][j][0])))
                else:
                    self.tax_product.append(0)
        return self.tax_product
    
    def get_tax_value_all(self):
        """
            Saca la cantidad en efectivo real del impuesto a pagar
        """
        self.tax_value = []
        
        for i in range(0, len(self.price_product)):
            tmp = 0.0
            for j in range(0, len(self.price_product[i])):
                tmp += self.tax_product[i] * self.price_product[i][j][0]
            self.tax_value.append(tmp)
    
    def get_sale_price(self):
        """
            Calcula el precio real de la venta cuando:
            - el producto tiene impuesto pero no descuento
            - tiene impuesto y descuento
            - no tiene ninguno de los 2
        """
        self.sale_price = {}
        tax = []
        discount = []

        for item in self.data:
            tax.append(item.shopping_cart.values_list('stock_room__tax__percentage'))
            discount.append(item.shopping_cart.values_list('stock_room__discount__percentage'))
        
        for i in range(0, len(self.price_product)):
            tmp = []
            for j in range(0, len(self.price_product[i])):
                if tax[i][j][0] and not discount[i][j][0]:
                    tmp.append(self.price_product[i][j][0] * ( self.tax_product[i] + 1))
                elif tax[i][j][0] and discount[i][j][0]:
                    value_discount = (100.0 - float(discount[i][j][0])) / 100.0
                    tmp.append( self.price_product[i][j][0] * value_discount)
                else:
                    tmp.append(self.price_product[i][j][0])
            self.sale_price[i]= tmp
        return self.sale_price
                    
        
    def get_total_all(self):
        """
            total de todas las ventas
        """
        discounts = []
        value_discount = []
        price = {}
        self.total = []
        
        for i in range(0,len(self.data)):
            discounts.append(self.data.values_list('discount__percentage')[i][0])
        
        for i in range(0, len(self.amount_product)):
            price_s = 0.0
            for j in range(0, len(self.amount_product[i])):
                if discounts[i]:
                    value_discount.append(float(discounts[i]/100))
                else:
                    value_discount.append(0.0)
                price_s += (self.sale_price[i][j]/1.0) * self.amount_product[i][j][0]
            price[i] = price_s

        for i in range(0, len(price)):
            self.total.append(price[i] * (1 - value_discount[i]))
        
        return self.total
        
        