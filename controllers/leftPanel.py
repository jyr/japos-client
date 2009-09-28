import core
from django.db.models import Q
from japos.stockrooms.models import StockRoom

class Stock:
    
    def __init__(self):
        pass
    
    def get_stock(self, search = None):
        self.values = []
        
        if search:
            data = StockRoom.objects.filter(
                    Q(product__name__contains = search) |
                    Q(product__barcode__contains = search)
                ).values_list('pk','product__name', 'stock', 'price')
        else:
            data = StockRoom.objects.values_list('pk','product__name', 'stock', 'price')
        
        for item in data:
            self.values.append((unicode(item[1]), unicode(item[2]), unicode(item[3])))

        return self.values
    
    def get_info_product(self, name):
        self.info_product = StockRoom.objects.get(product__name = name)
        
        return self.info_product
        
    