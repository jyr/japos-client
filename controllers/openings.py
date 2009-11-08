
import core

from japos.openings.models import Opening
from japos.pos.models import Pos
from japos.crews.models import Employee
from helpers.message import Message


class Opening_controller:
    
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
            data = Employee.objects.filter(user__groups=4).exclude(user__groups=3).values_list('pk','user__username')
        if category == 3:
            data = Employee.objects.filter(user__groups=3).values_list('pk','user__username')
            
        for item in data:
            self.choices.append( str(item[1]))
            self.Values.append((item[0],item[1]))

        return self.choices, self.Values

    def error(self):
		Message("Select a option")

    def __get_pk_pos(self, pos):
		data = Pos.objects.get(name = pos)
		return data

    def __get_pk_cashier(self, cashier):
	    data = Employee.objects.get(user__username=cashier)
	    return data

    def __get_pk_auditor(self, auditor):
	    data = Employee.objects.get(user__username=auditor)
	    return data
	
    def create_opening(self, pos, cashier, auditor, initialfund):
	    pos_pk = self.__get_pk_pos(pos)
	    cashier_pk = self.__get_pk_cashier(cashier)
	    auditor_pk = self.__get_pk_auditor(auditor)
	    opening = Opening()
	    opening.pos = pos_pk
	    opening.cashier = cashier_pk
	    opening.auditor = auditor_pk
	    opening.initial_fund = initialfund
	    opening.save()
	    #print auditor_pk, initialfund
	    #print dir(opening)

if __name__ == '__main__':
    Opening