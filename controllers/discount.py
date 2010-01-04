#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
from japos.discounts.models import Discount

class Discount_controller:
	
	def __init__(self):
		pass
			
	def get_discount(self, t):
		self.choices = []
		data = Discount.objects.filter(is_enabled=1, type = t).values_list('pk', 'percentage')
		
		for item in data:
			self.choices.append( str(item[1]))