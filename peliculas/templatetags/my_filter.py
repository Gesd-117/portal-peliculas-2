from datetime import datetime
from django import template

register = template.Library()

@register.filter(name='str_to_date')
def str_to_date(value, format="%Y-%m-%d"):
    return  datetime.strptime(value, format)