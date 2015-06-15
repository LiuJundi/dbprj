from django.shortcuts import render
from django.db import connection
from .forms import SignUpForm
from .models import Customer
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
import json
from django.http import JsonResponse
from datetime import *

def home(request):
	title = "Welcome!"
	context = {
		'title': title,
	}
	return render(request, "home.html", context)

def signUp(request):
	title = "SignUp!"
	form = SignUpForm(request.POST or None)
	flag = False
	context = {
		'title': title,
	}
	if form.is_valid():
		pass1 = form.cleaned_data['password']
		pass2 = form.cleaned_data['password2']
		cursor= connection.cursor()
		cursor.execute('SELECT count(*) \
		                FROM getWash_customer \
		                WHERE cellphone = %s',
		                [ form.cleaned_data['cellphone'] ] )
		user_count = cursor.fetchone()
		if user_count[0] > 0: #the cellphone has been registered
			context['error'] = 'The cellphone has been registered.'
		elif pass1 == pass2: #sign up success
			flag = True
			cursor.execute('INSERT INTO getWash_customer(cellphone, firstName, lastName, password)\
			                VALUES (%s, %s, %s, %s)',
			                [ form.cleaned_data['cellphone'],
			                  form.cleaned_data['firstName'],
			                  form.cleaned_data['lastName'],
			                  form.cleaned_data['password'], ]
			              )
	if flag:
		context['content'] = 'Sign Up Successfully!'
	else:
		context['form'] = form

	return render(request, "registration/signUp.html", context)

@requires_csrf_token
def shopping(request):
	title = "Wash Now!"
	cursor= connection.cursor()
	cursor.execute("SELECT clothType, unitPrice\
	             FROM getWash_cloth")
	clothType = cursor.fetchall()
	cursor.execute("SELECT *\
	                FROM getWash_address")
	addrs = cursor.fetchall()
	context = {
		'title': title,
		'clothType': clothType,
		'addrs': addrs,
	}
	return render(request, "shopping.html", context)

def unitPrice(request):
	title = "Wash Now!"
	context = {
		'title': title,
	}
	return render(request, "home.html", context)

def coverArea(request):
	title = "Wash Now!"
	context = {
		'title': title,
	}
	return render(request, "home.html", context)

def about(request):
	title = "Wash Now!"
	context = {
		'title': title,
	}
	return render(request, "home.html", context)

@requires_csrf_token
def makeOrder(request):
	print "HERE"
	tempData = request.POST
	for jsonData in tempData:
		break;
	data = json.loads(jsonData)
	print data
	cursor= connection.cursor()
	now = datetime.now()
	idstr = now.strftime("%Y%m%d%H%M%S")
	print idstr
	cursor.execute("INSERT INTO getWash_order(orderId, memo, customer_id, state, sumPrice, addr_id, createdAt, bookTime)\
	                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
	                [ 	idstr,
	                	str(data['memo']),
	                	1,
	                	0,
	                	str(data['sumPrice']),
	                	data['addrId'],
	                	datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
	                	datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	                ] )

	itemList = data['itemlist']
	print itemList
	for item in itemList:
		clothType = item['type']
		quantity = item['quantity']
		if quantity > 0:
			cursor.execute("INSERT INTO getWash_clothdetail(order_id, quantity, clothType_id)\
			                VALUES(%s, %s, %s)",
			                [	idstr,
			                	quantity,
			                	clothType,
			                ])

	return HttpResponse("Success.", content_type="text/plain")



def orders(request):
	title = "getWash"
	cursor= connection.cursor()
	cursor.execute("SELECT *\
	                FROM getWash_order\
	                WHERE state=%s",
	                [0,] )
	orders = cursor.fetchall()
	print orders
	context = {
		'orders': orders,
		'type': 0, # 0 means all orders
	}
	return render(request, "manage.html", context)

def newOrders(request):
	title = "getWash"
	cursor= connection.cursor()
	cursor.execute("SELECT *\
	                FROM getWash_order\
	                WHERE state=%s \
	                ORDER BY createdAt DESC\
	                LIMIT 10",
	                [0,] )
	orders = cursor.fetchall()
	print orders
	context = {
		'orders': orders,
		'type': 1, # 0 means all orders
	}
	return render(request, "manage.html", context)

def getOrders(request):
	cursor= connection.cursor()
	state = request.GET['state']
	offset = request.GET['offset']
	if ( int(state) < 0 ): #all orders
		cursor.execute("SELECT orderId, sumPrice, addr_id, customer_id \
		                FROM getWash_order\
		                ORDER BY createdAt DESC\
		                LIMIT 10 OFFSET %s",
		                [ offset,] )
		result = { "orders": [ list(order) for order in cursor.fetchall() ] }
	else:
		cursor.execute("SELECT orderId, sumPrice, addr_id, customer_id \
		                FROM getWash_order\
		                WHERE state=%s\
		                ORDER BY createdAt DESC\
		                LIMIT 10 OFFSET %s",
		                [state, offset, ])
		result = {"orders": [list(order) for order in cursor.fetchall() ] }

	return JsonResponse(json.dumps(result), safe=False )




