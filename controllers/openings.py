
import core

from japos.pos.models import Pos
from japos.crews.models import Cashier, Auditor


class Opening:
    
    def __init__(self):
        pass
        
    def get_data_opening(self,category):
        """
            Obtiene los datos para abrir turno, cuando
            category = 1 = pos
            category = 2 = cashier
            category = 3 = auditor
        """
        self.choices = []
        self.Values = []
        
        if category == 1: 
            data = Pos.objects.values_list('id','name')
        if category == 2:
            data = Cashier.objects.values_list('id','user__username')
        if category == 3:
            data = Auditor.objects.values_list('id','user__username')
            
        for item in data:
            self.choices.append( str(item[1]))
            self.Values.append((item[0],item[1]))

        return self.choices, self.Values

if __name__ == '__main__':
    Opening