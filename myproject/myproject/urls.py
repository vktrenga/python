"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
import myapp 
#import myapp.customer
from myapp.views import hello,DeleteUser,CreateUser,RetriveUser,UpdateUser,Registor_frm_fun,customer1
from myapp.customer.customer import customer_add,customer_delete,customer_view
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^admin', include(admin.site.urls)),
    url(r'^$',  hello),
    #url(r'^hello/', hello),
    url(r'^customer1/', customer1),
    url(r'^customer_add/', customer_add),
    url(r'^customer_delete/', customer_delete),
    url(r'^customer_view/', customer_view),
    url(r'^CreateUser/', CreateUser),
    url(r'^RetriveUser/', RetriveUser),
    url(r'^UpdateUser/', UpdateUser),
    url(r'^DeleteUser/', DeleteUser),
    url(r'^Registor_frm_fun/', Registor_frm_fun),
]
