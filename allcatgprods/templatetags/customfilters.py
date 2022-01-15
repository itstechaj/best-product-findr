from django import template
from django.db.models import Max,Min
from django.template.defaultfilters import stringfilter
register=template.Library()

# we use this filter to print the pro and cons and user review (As they contains "/" to seperate one thins from another)
#for using this in your template write {% load customfilters %}
@register.filter(name='spliter')
@stringfilter #for use this filter only on strings
def spliter(value):
    return value.split("/")

@register.filter(name='replacewithdash')
@stringfilter #for use this filter only on strings
def replacewithdash(value):
    return value.replace(" ","-")
    
@register.filter(name='checkspclcatg')
@stringfilter #for use this filter only on strings
def checkspclcatg(value):
    if(value=="general"):
        return ""
    else:
        return value.capitalize()

