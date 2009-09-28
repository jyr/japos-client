import core
from django.db.models import Sum
from japos.sales.models import Sale

class SalesList:
    def __init__(self):
        pass
    
    def get_price_product(self, sale_id):
        """
            Obtiene el precio del producto vendido
        """
        self.price_product = []
        data = Sale.objects.get(pk = sale_id)

        self.price_product = data.shopping_cart.values_list('stock_room__price')

        print self.price_product
    
    def get_amount_product(self, sale_id):
        """
            Obtiene la cantidad por producto vendida
        """
        self.amount_product = []
        
        data = Sale.objects.get(pk = sale_id)
        
        self.amount_product = data.shopping_cart.values_list('amount')
        
        print self.amount_product
    
    def get_subtotal(self):
        """
            Calcula el subtotal de la venta
        """
        self.subtotal = 0
        
        for i in range(0,len(self.amount_product)):
            self.subtotal += (self.amount_product[i][0]*self.price_product[i][0])
        print "subtotal :%f" %(self.subtotal)
        
    def get_total(self):
        
        print self.total_products