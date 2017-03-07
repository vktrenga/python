from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	text = """<h1>welcome to my app !</h1>"""
	return render(request,"index.html")
	#return HttpResponse(text)

def menu_list(request):
	menu_list=[]
	menu_values = {'index': 'index.html','contact':'contact.html', 'aboutus': 'aboutus.html'}
	menu_list.append(menu_values)
	return  HttpResponse(menu_list)