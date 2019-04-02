from django import forms
from django.contrib.auth.models import User
from userlogin.models import MyUser, Customer, Restaurant, Cuisine
from django.contrib.auth.forms import UserCreationForm

class CustomerReg(UserCreationForm) :
	phone_number = forms.CharField(required=True)
	name = forms.CharField(required=True, max_length=25)
	Utype = forms.CharField(required=False)

	class Meta :
		model = MyUser
		fields = ('username', 'password1', 'password2', 'phone_number', 'name')

	def save(self, commit = True) :
		usr = super(CustomerReg, self).save(commit=False)
		usr.user_type = 'C'
		cus = Customer()
		cus.phone_number = self.cleaned_data['phone_number']
		cus.name = self.cleaned_data['name']
		if commit :
			usr.save()
			cus.Utype = usr
			cus.save()

		return usr


class RestReg(UserCreationForm) :
	phone_number = forms.CharField(required=True)
	name = forms.CharField(required=True, max_length=25)
	location = forms.CharField(required=True, max_length=200)
	Utype = forms.CharField(required=False)
	cuisine = forms.CharField(max_length = 30)


	class Meta :
		model = MyUser
		fields = ('username', 'password1', 'password2', 'phone_number', 'name', 'cuisine', 'location')

	def save(self, commit = True) :
		usr = super(RestReg, self).save(commit=False)
		usr.user_type = 'R'
		res = Restaurant()
		csn = Cuisine()
		csn.cus_type = self.cleaned_data['cuisine']
		res.phone_number = self.cleaned_data['phone_number']
		res.name = self.cleaned_data['name']
		res.location = self.cleaned_data['location']
		if commit :
			usr.save()
			res.Utype = usr
			csn.save()
			res.save()
			res.cuisine.add(csn)
			# res.save()

		return usr


