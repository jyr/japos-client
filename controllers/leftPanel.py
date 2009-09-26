import core
from japos.stockrooms.models import StockRoom

class Stock:
    
    def __init__(self):
        pass
    
    def get_stock(self):
        self.value = {}
        
        #data = StockRoom.objects.values_list('pk','pos__name', 'product__name','barcode', 'stock', 'product__stock', 'product__purchase_price', 'price', 'discount', 'tax','product__description')
        data = StockRoom.objects.values_list('pk','product__name', 'stock', 'price')
        
        for item in data:
            self.values = {item[0]:(str(item[1]), str(item[2]), str(item[3]))}
            
        self.items = self.values.items()
        return self.items
    
    def get_info_product(self, name):
        self.info_product = StockRoom.objects.get(product__name = name)
        
        return self.info_product
        
    