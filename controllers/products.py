import core

class Product:
    
    def __init__(self):
        pass
    
    def get_stock():
        data = StockRoom.objects.values_list('pos__name', 'product__name','barcode', 'stock', 'product__stock', 'product__purchase_price', 'price', 'discount', 'tax', 'product__description')