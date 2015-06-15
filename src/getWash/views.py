from django.shortcuts import render
from django.db import connection
from .forms import SignUpForm
from .models import Customer

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

def signIn(request):
	title = "signIn"
	context = {
		'title' : title,
	}
	return render(request, "registration/signIn.html", context)

def shopping(request):
	title = "Wash Now!"
	context = {
		'title': title,
	}
	return render(request, "shopping.html", context)

def unitPrice(request):
	if request.user.is_authenticated():
		title = "Price List"
		context = {
			'title': title,
		}
		return render(request, "home.html", context)
	else:
		signUp(request)

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

