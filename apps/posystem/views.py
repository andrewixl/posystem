from django.shortcuts import render, redirect
from .models import Product
from ..login_app.models import User
from django.contrib import messages
import random

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	products = Product.objects.all().order_by('-created_at')[:10]
	context = {
	"product":products
	}
	return render(request, 'posystem/index.html', context)

def request(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	return render(request, 'posystem/request.html')

def addrequest(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	results = Product.objects.registerProduct(request.POST)
	request.session['status'] = results['status']
	if results['status'] == True:
		user = Product.objects.createProduct(request.POST)
		messages.success(request, 'Product Requested!')
	else:
		genErrors(request, results['errors'])
		return redirect("/request")
	return redirect('/')

def export(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	return render(request, 'posystem/export.html')

def vote(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	products = Product.objects.exclude(voters = request.session['user_id']).all()
	products2 = Product.objects.filter(voters = request.session['user_id']).all()
	context = {
	"product":products,
	"product2":products2,
	}
	return render(request, 'posystem/vote.html', context)

def status(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	products = Product.objects.all()
	context = {
	"product":products,
	}
	return render(request, 'posystem/status.html', context)

def editstatus(request, product_id):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	products = Product.objects.all()
	context = {
	"product":products,
	"theid" : int(product_id),
	}
	return render(request, 'posystem/status.html', context)

def voteProduct(request, product_id):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	try:
		product = Product.objects.get(id = product_id)
		product.votes += 1
		if product.votes >= 5:
			product.status = "Ready to Order"
		product.save()
		this_user = User.objects.get(id=request.session['user_id'])
		this_product = Product.objects.get(id=product_id)
		this_product.voters.add(this_user)
		return redirect('/vote')
	except:
		return redirect('/vote')

def changestatus(request, product_id):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	try:
		product = Product.objects.get(id = product_id)
		print "ok"
		print request.POST
		print "done"
		product.status = request.POST.get("status")
		product.save()
		return redirect('/status')
	except:
		return redirect('/status2')

def addVendor(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	return render(request, 'posystem/addvendor.html')

def createVendor(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect("/login")
	results = Vendor.objects.registerVendor(request.POST)
	request.session['status'] = results['status']
	if results['status'] == True:
		user = Vendor.objects.createVendor(request.POST)
		messages.success(request, 'Vendor Created!')
	else:
		genErrors(request, results['errors'])
		return redirect("/addvendor")
	return redirect('/')
