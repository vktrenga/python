from django import forms

class customer_frm(forms.Form):
	customer = forms.CharField(label='Customer  name', max_length=100)
	customer_id=forms.CharField(label='Customer Contact No',max_length=100)
	mobile_no = forms.CharField(label='Customer  name', max_length=100)
	email_no=forms.CharField(label='Customer Contact No',max_length=100)
	address = forms.CharField(label='Customer  name', max_length=100)
	