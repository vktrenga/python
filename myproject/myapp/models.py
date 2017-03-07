from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registor_User(models.Model):
	username=models.CharField(max_length=100)
	mail=models.CharField(max_length=50)
	password=models.CharField(max_length=40)
	user_contact=models.CharField(max_length=20)
	contact_no=models.CharField(max_length=20,default="t")
	class Meta:
		db_table="codesupporter_user"

