#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core

from django.contrib.auth.models import check_password
from japos.crews.models import Employee
from helpers.message import Message

class Auth_controller:
	
	def __init__(self):
	    self.get_auditor()

	def auth(self, username, password):
	    self.username = Employee.objects.get(user__username = username)
	    self.valid = check_password(password, self.username.user.password)

	    return self.valid

	def error(self):
	    Message("Invalid username or password. Please try again")

	def get_auditor(self):
	    self.choices = []
	    data = Employee.objects.filter(user__groups=3).values_list('pk','user__username')
	
	    for item in data:
			self.choices.append( str(item[1]))