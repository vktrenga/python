from django.conf.urls import url,patterns, include
from django.contrib import admin
import views
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
 	url(r'^$', views.index),
 	#url(r'^$', index),
 	url(r'^menu_list/$', views.menu_list, name='menu_list'),
]