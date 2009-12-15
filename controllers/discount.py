#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
from japos.discounts.models import Discount

class Discount_controller:
	
	def __init__(self):
		self.get_discount()
	
	def get_discount(self):
		self.choices = []
		data = Discount.objects.filter(is_enabled=1).values_list('pk', 'percentage')
		
		for item in data:
			self.choices.append( str(item[1]))