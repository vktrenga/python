from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Registor_User
#from django.http import HttpResponse
from datetime import datetime,date
from .forms import Registor_frm

#import datetime as dt
# Create your views here.
def hello1(request):
	text = """<h1>welcome to my app !</h1>"""
	return HttpResponse(text)

def hello(request):
	totay_date=date.today();
	return render(request,"hello.html",{"today":totay_date})

def CreateUser(request):
	ru=Registor_User(username="Mani",mail="rengaraj.nishta@gmail.com",password="123")
	ru.save()
	return HttpResponse(request)

def RetriveUser(request):
	res=Registor_User.objects.all()
	ret=""
	for elt in res:
		ret+=elt.username+"<br>"
	return HttpResponse(ret)

def customer1(request):
	return HttpResponse("Hai tEST");

def UpdateUser(request):
	up=Registor_User.objects.get(id=1)
	up.username="G.Rengaraj"
	up.save();
	return HttpResponse("Updated successfully")

def DeleteUser(request):
	de=Registor_User.objects.get(id=1)
	#up.username="G.Rengaraj"
	de.delete();
	return HttpResponse("Deleted successfully")

def Registor_frm_fun(self):
	if self.method=="POST":
		form=Registor_frm(self.POST)
		if form.is_valid():
			username = form.cleaned_data['first_name']
			last_name =form.cleaned_data['last_name']
			#email=self.cleaned_data.get("username")
			ru=Registor_User(username=username,mail=last_name,password=last_name)
			ru.save()
		return render(self, 'registor_frm.html', {'form': form})
	else:
		form=Registor_frm()
		return render(self, 'registor_frm.html', {'form': form})