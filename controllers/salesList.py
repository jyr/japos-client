import core
from django.db.models import Sum
from japos.sales.models import Sale

class SalesList:
    def __init__(self):
        pass
    
    def get_sales(self):
        """
            Listado de todas las ventas
        """
        self.sales = []
        data = Sale.objects.values_list('pk', 'sku', 'date_created')
        
        for item in data:
            self.sales.append(item)
        print self.sales
        return self.sales

    def get_total_products(self):
        """
            Obtiene el total de productos por venta
        """
        self.total_products = []
        data = Sale.objects.all()
        
        for item in data:
            self.total_products.append(item.shopping_cart.aggregate(Sum('amount')))
        print self.total_products
        self.total_products

    def get_price_product_all(self):
        """
            Obtiene el precio del almacen del producto vendido
        """
        self.price_product = []
        data = Sale.objects.all()

        for item in data:
            self.price_product.append(item.shopping_cart.values_list('stock_room__price'))

        print self.price_product
    
    def get_amount_product_all(self):
        """
            Obtiene la cantidad por producto vendida
        """
        self.amount_product = []
        
        data = Sale.objects.all()
        
        for item in data:
            self.amount_product.append(item.shopping_cart.values_list('amount'))
        
        print self.amount_product
    
    def get_subtotal_all(self):
        self.subtotal = []
        
        for i in range(0,len(self.amount_product)):
            subtotal=0
            for j in range(0,len(self.amount_product[i])):
                subtotal += self.amount_product[i][j][0]*self.price_product[i][j][0]
            self.subtotal.append(subtotal)
        print self.subtotal

    def get_price_discount_all(self):
        """
            Calcula el precio con descuento
        """
        value = []
        self.price_discount = []
        data = Sale.objects.all()
        
        for item in data:
            value.append(item.shopping_cart.values_list('stock_room__discount__percentage'))
        print value
        for i in range(0,len(self.price_product)):
            for j in range(0, len(self.price_product[i])):
                if value[i][j][0]:
                    print value[i][j][0]
                    print self.price_product[i][j][0]
                    discount = (100.0 - float(value[i][j][0])) / 100.0
                    total = (self.amount_product[i][j][0] * self.price_product[i][j][0])
                    self.price_discount.append( total * discount)
                else:
                    self.price_discount.append(0.00)
        print self.price_discount

    def get_tax_product_all(self):
        """
            Convierte el porcentaje del impuesto a decimal
        """
        self.tax_product = []
        value = []
        
        data = Sale.objects.all()
        
        for item in data:
            value.append(item.shopping_cart.values_list('stock_room__tax__percentage'))
        print value
        for i in range(0, len(value)):
            for j in range(0, len(value[i])):
                if value[i][j][0]:
                    self.tax_product.append(float(value[i][j][0] /(100 - value[i][j][0])))
                else:
                    self.tax_product.append(0)
        print self.tax_product
    
    def get_tax_value_all(self):
        """
            Saca la cantidad en efectivo real del impuesto a pagar
        """
        self.tax_value = []
        
        for i in range(0, len(self.price_product)):
            for j in range(0, len(self.price_product[i])):
                self.tax_value.append(self.tax_product[i] * self.price_product[i][j][0])
                
        print self.tax_value
        
    def get_total_all(self):
        
        print self.total_products