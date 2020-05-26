from django import template
from app01 import forms
register = template.Library()


@register.inclusion_tag('app01/form.html')
def inclusionform(form_name):
    form = getattr(forms,form_name)


    return locals()


