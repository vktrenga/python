from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from datetime import datetime,date
from myapp.customer.customer_model import Customer_table
from myapp.customer.customer_forms import customer_frm
from django.contrib import messages
from django.http import Http404

def customer_add(request):
	if request.method=="POST":
		form=customer_frm(request.POST)
		#return HttpResponseNotFound(form.is_valid())
		#print form.is_valid(), form.errors, type(form.errors)
		if form.is_valid():
			username = form.cleaned_data['customer']
			customer_contact_no = form.cleaned_data['mobile_no']
			ru=Customer_table(customer=username,mobile_no=customer_contact_no,email_no="test",address="test")
			if ru.save():
				messages.success(request, 'Profile details updated.')
				return render(request, 'customer/customer_add.html', {'form': form,'msg':"failure"})
			else:
				messages.success(request, 'Profile details updated.')
				return render(request, 'customer/customer_add.html', {'form': form,'msg':"Success"})
		else:
			messages.error(request, "Error")
			raise Http404
			#return render(request, 'customer/customer_add.html', {'form': form,'msg':"Value Error"})
	else:
		text = """<h1>customer_add!</h1>"""
		form=customer_frm()
		return render(request, 'customer/customer_add.html', {'form': form,'msg':"Test"})
		#return render(self,"customer/customer_add.html")

def customer_delete(request):
	text = """<h1>customer_delete!</h1>"""
	return HttpResponse(text)

def customer_view(request):
	text = """<h1>customer_view!</h1>"""
	#return HttpResponse(text)
	return render(request, 'customer/customer_view.html', {'values': "form"})


def customer_update(request):
	text = """<h1>customer_update!</h1>"""
	return HttpResponse(text)