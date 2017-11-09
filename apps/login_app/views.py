from django.shortcuts import render, redirect, HttpResponse
from models import User, Club
from django.contrib import messages
import random

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
	try:
		print "good"
		request.session['user_id']
		redirect("/")
	except KeyError:
		print "bad"
		redirect("/login")
	clubs = Club.objects.all()
	context = {
	"club":clubs,
	}
	return render(request, 'login_app/index.html', context)

def register(request):
	# try:
	# 	request.session['user_id']
	# 	redirect("/")
	# except KeyError:
	# 	redirect("/login")
	results = User.objects.registerVal(request.POST)
 	request.session['status'] = results['status']
	if results['status'] == True:
		user = User.objects.createUser(request.POST)
		messages.success(request, 'User Registered! Please Log In.')
	genErrors(request, results['errors'])
	return redirect('/login')
def login(request):
	# try:
	# 	request.session['user_id']
	# 	redirect("/")
	# except KeyError:
	# 	redirect("/login")
	results = User.objects.loginVal(request.POST)
	request.session['status'] = results['status']
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/login')

	request.session['first_name'] = results['user'][0].first_name
	request.session['last_name'] = results['user'][0].last_name
	request.session['email'] = results['user'][0].email
	request.session['username'] = results['user'][0].username
	request.session['club_name'] = results['user'][0].club.club_name
	request.session['club_id'] = results['user'][0].club.id
	request.session['user_id'] = results['user'][0].id
	print request.session['user_id']
	return redirect('/')

def logout(request):
	request.session.flush()
	return redirect('/login')

def createclub(request):
	return render(request, 'login_app/createclub.html')

def addclub(request):
	results = Club.objects.registerClub(request.POST)
 	request.session['status'] = results['status']
	if results['status'] == True:
		user = Club.objects.createClub(request.POST)
		messages.success(request, 'Club Created!')
	genErrors(request, results['errors'])
	return redirect("/login")
