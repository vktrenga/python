from django import template
register = template.Library()

@register.assignment_tag
def menu_list(request):
	return {"val":"hai"}