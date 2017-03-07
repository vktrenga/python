from django import template
register = template.Library()

@property
def menu_list():
	menu_list_val=[]
	menu_values = {'index': 'index.html','contact':'contact.html', 'aboutus': 'aboutus.html'}
	menu_list_val.append(menu_values)
	return menu_list_val