from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser) :
	types = (
		('SA', 'System Admin'),
		('C' , 'Customer'),
		('R' , 'Restaurant')
		)

	user_type = models.CharField(max_length=2,
								choices = types,
								default='A')

class SystemAdmin(models.Model) :
	Utype = models.OneToOneField('MyUser')
	
class Customer(models.Model) :
	Utype = models.OneToOneField('MyUser')
	name = models.CharField(max_length = 50)
	phone_number = models.CharField(max_length = 10)

class Cuisine(models.Model) :
	cus_type = models.CharField(max_length = 50)

class Restaurant(models.Model) :
	Utype = models.OneToOneField('MyUser')
	name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 10)
	cuisine = models.ManyToManyField(Cuisine, max_length = 30, verbose_name = "list of cuisines")
	location =  models.TextField(max_length = 200)

class Item(models.Model) :
	name = models.CharField(max_length = 100)
	item_types = (
		('NV', 'non-veg'),
		('V', 'veg'),
		('B', 'bev'),
		('D', 'des')
		)
	item_type = models.CharField(max_length = 2, choices = item_types, default='V')
	restaurant = models.ForeignKey(Restaurant, verbose_name='restaurant')
	price = models.IntegerField()

class Order(models.Model) :
	order_ID = models.AutoField(primary_key=True)
	status = models.CharField(max_length = 200)
	price = models.IntegerField()
	customer = models.ForeignKey(Customer, verbose_name='customer')
	restaurant = models.ForeignKey(Restaurant, verbose_name='restaurant')
	address = models.CharField(max_length = 100, default = 'IITKGP')

class OrderItems(models.Model) :
	item = models.ForeignKey(Item)
	order = models.ForeignKey(Order)
	quantity = models.IntegerField(default = 0)

