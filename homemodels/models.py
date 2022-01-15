from django.db import models
from django import forms
# Create your models here.
#we created model for Products category list that we are going to show on homepage
class prodcatglist(models.Model): 
    catg=models.CharField(max_length=50) #ex- Ecommerce
    subcatg=models.CharField(max_length=50) #ex - Mobiles
    rank=models.SmallIntegerField() #ex - which rank to show
    subcatgimg=models.ImageField(upload_to="homepage/img/",default="defaultimg/")
    def __str__(self):
        return "/".join([self.catg,self.subcatg,str(self.rank)])

class reviewform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.PositiveBigIntegerField()
    message=models.TextField()
    rating=models.CharField(max_length=10)
    submit_time=models.DateTimeField()
    def __str__(self):
        return " @ ".join([self.name,str(self.submit_time)])
    
    # submit_time=models.TimeField()