from __future__ import unicode_literals

from django.db import models

class Customer_table(models.Model):
	customer=models.CharField(max_length=100)
	customer_id=models.CharField(max_length=50)
	mobile_no=models.CharField(max_length=40)
	email_no=models.CharField(max_length=20)
	address=models.CharField(max_length=20,default="t")
	class Meta:
		db_table="customer"
