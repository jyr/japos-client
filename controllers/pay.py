#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core


from japos.crews.models import Employee
from japos.coins.models import Money


class Pay_controller:
	
	def __init__(self):
		pass

	def get_data_pay(self):
	    
	    self.choices_salesman = []
	    self.choices_coins = []
	
	    data = Employee.objects.filter(user__groups=5).exclude(user__groups=3).values_list('pk', 'user__username')
	    for item in data:
		    self.choices_salesman.append(str(item[1]))
	
	    data = Money.objects.filter(is_enabled = 1).values_list('initials')
	    i = 0
	    for item in data:
		    self.choices_coins.append(str(item[0]))