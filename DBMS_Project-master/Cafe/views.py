from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from forms import CustomerReg, RestReg
from django.http import HttpResponse, JsonResponse
from userlogin.models import Customer, Restaurant, MyUser, Item, Order, OrderItems
import json
from django.core import serializers
import operator


def login_user(request) :
	return render(request, 'login_User.html')

def login_restaurant(request) :
	return render(request, 'login_Restaurant.html')

def authenticate_user(request) :
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username = username, password = password)

	if user is not None :
		auth.login(request, user)
		if user.user_type == 'C' :
			return JsonResponse({'success' : '1', 'username' : username})

	# else :
	return JsonResponse({'success' : '0'})


def authenticate_res(request) :
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username = username, password = password)

	if user is not None :
		auth.login(request, user)
		if user.user_type == 'R' :
			return JsonResponse({'success' : '1', 'username' : username})

	return JsonResponse({'success' : '0'})



def additem(request):
	if request.method == 'POST' :
		itemtype = request.POST.get('itemType', 'NV')
		itemcost =  request.POST.get('number', 123)
		item = request.POST.get ('item', 'grill')
		username = request.user.username
		usr = MyUser.objects.get(username = username)
		res = Restaurant.objects.get(Utype = usr)
		orders = res.order_set.all

		newitem = Item(name = item, item_type = itemtype, price = itemcost, restaurant= res)
		newitem.save()

		return HttpResponse('/rest_home/')

def deleteitem(request):
	if request.method == 'POST' :
		item = request.POST.get ('itemND', 'grill')
		username = request.user.username
		usr = MyUser.objects.get(username = username)
		res = Restaurant.objects.get(Utype = usr)
		orders = res.order_set.all

		newitem = Item.objects.get(name = item)
		newitem.delete()

		return HttpResponse('/rest_home/')

 

def home(request) :
	username = request.user.username
	usr = MyUser.objects.get(username = username)
	customer = Customer.objects.get(Utype = usr)
	custorders = customer.order_set.all
	# print custorders.count()
	ok = 0
	for each in customer.order_set.all():
		if each.status!='completed':
			ok =1 
	print ok

	orders = Order.objects.all()
	temp1 = Restaurant.objects.all()
	dic = {}
	for each in temp1:
		temp = 1000
		for every in orders:
			# print every.restaurant.id, every.customer.id, each.id, customer.id
			if every.restaurant.id == each.id and every.customer.id == customer.id:
				temp= temp-1
		dic[each] = temp
		# print each,temp
	
	lol = sorted(dic.items(),key=operator.itemgetter(1))
	sdic = {}
	for a in lol:
		sdic[a[0]] = 1005-a[1]
	# print sdic

	return render_to_response('user_home.html',{'priority' : sdic, 'status':ok, 'Restaurants':Restaurant.objects.all(), 'orders' : custorders})

def customer_register(request) :
	if request.method == 'POST' :
		form = CustomerReg(request.POST)
		if form.is_valid() :
			form.save()
			return HttpResponse('/login_user/')
	else :
		return render_to_response('debug.html', {'form' : form})

def restaurant_register(request) :
	if request.method == 'POST' :
		form = RestReg(request.POST)
		if form.is_valid() :
			form.save()
			return HttpResponse('/login_restaurant/')

	else :
		args = {}
		args['form'] = RestReg()
		return render(request, 'login_Restaurant', args)


def rest_home(request) :
	username = None
	orders = None
	if request.user.is_authenticated():
		username = request.user.username
		usr = MyUser.objects.get(username = username)
		res = Restaurant.objects.get(Utype = usr)
		orders = res.order_set.all
		orderitems = OrderItems.objects.all
	return render(request,'rest_home.html', {'orders' : orders,'restaurant' : res, 'orderitems': orderitems})

def place_order(request) :
	res_id = request.session['res_id']
	items = request.session['items'] 
	username = request.user.username
	usr = MyUser.objects.get(username = username)
	customer = Customer.objects.get(Utype = usr)
	money = 0
	for each in items :
		money = money + (each["item"]["price"] * each["item"]["num"])
	request.session['price'] = money
	return render(request, 'place_order.html', {'customer': customer,'items' : items, 'totalMoney' : money})
		

def rest_display(request, rest_id = 1):
	res = Restaurant.objects.get(id = rest_id)
	items = res.item_set.all
	return render(request, 'rest_single.html', {'restaurant' : res, 'usr' : res.Utype, 'items' : items})

def query(request, check_id=1):
	a = Restaurant.objects.get(id = check_id)
	return JsonResponse({'id': a.id, 'name':a.name , 'phone_number':a.phone_number, 'location': a.location,'cuisine':a.cuisine})

def setstatus(request):
	if request.method == 'POST' :
		status = request.POST.get('status','placed')
		orderno = request.POST.get('orderNo', 0)
		order = Order.objects.get(order_ID = orderno)
		order.status = status
		order.save()
		username = request.user.username
		usr = MyUser.objects.get(username = username)
		res = Restaurant.objects.get(Utype = usr)
		orders = res.order_set.all
		orderitems = OrderItems.objects.all

		return HttpResponse('/rest_home/')

def cart(request) :
	if request.method == 'POST' :
		res_id = request.POST.get('res_id', 0)
		items = json.loads(request.POST.get('itArray'))
		request.session['res_id'] = res_id
		request.session['items'] = items
		return HttpResponse('success')

def checkout(request):
	# print 'Here'
	if request.method == 'POST' :
		res_id = request.session['res_id']
		items =	request.session['items']
		address = request.POST.get('address', 'IIT')
		# print address
		username = request.user.username
		usr = MyUser.objects.get(username = username)
		customer = Customer.objects.get(Utype = usr)
		rest = Restaurant.objects.get(id = res_id)
		status = 'Placed'
		ord = Order(status = status, price = request.session['price'], customer = customer, restaurant = rest, address = address)
		ord.save()
		order_id = ord.order_ID
		for each in items:
			itname = each["item"]["name"]
			item = Item.objects.get(name = itname)
			orditem = OrderItems(item = item, order = ord, quantity = each["item"]["num"])
			
			orditem.save()

		# print "Yoooo"
		return HttpResponse(order_id)

