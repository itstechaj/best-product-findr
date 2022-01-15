from django.contrib import admin

# Register your models here.
from .models import prodcatglist, reviewform
admin.site.register(prodcatglist)
admin.site.register(reviewform)