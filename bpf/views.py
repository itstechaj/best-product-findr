from django.db import models
from django.db.models.query import EmptyQuerySet
from django.http.response import HttpResponse
from django.contrib import messages
from homemodels.models import prodcatglist
# importent note 
# to import model from apps in this project we use following two lines of codes 
# from django.apps import apps 
# model=apps.get_model('App name','Modelname') 
from django.shortcuts import render
# from django.apps import apps


def home(request):
    # catgmodel=apps.get_model('homemodels','prodcatglist')
    #here we store all data in our model in allcatgs
    allcatg=prodcatglist.objects.all()
    #we store all data with ecommerce category in ecomcatg 
    ecomcatg=allcatg.filter(catg="E-commerce")
    #we store all data with fintech category in fintechcatg
    fintechcatg=allcatg.filter(catg="FinTech")
    # print(catgmodel)
    #add category if available in homepagedict (we are displaying key on homepage so write key carefully)
    homepagedict={"E-commerce Products":ecomcatg,"FinTech Apps":fintechcatg}
    #here we are sending dictionary of dictionary so that we can apply two for loop and print all the categories with #their respective items
    return render(request,'home.html',{"homepagedict":homepagedict})

def aboutus(request):
    return render(request,'aboutus.html')
def review(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        mob=request.POST['phone']
        msg=request.POST['message']
        if len(name)<2 or len(email)<5 or len(str(mob))!=10 or len(msg)<1:
            messages.error(request,"\U0001F61E Please Fill the Form Correctly !")
        else:
            rating="NULL"
            try:
                rating=request.POST['emojioption']
            except:
                messages.error(request,"\U0001F915 Please Select The Emoji option !")
            if rating!="NULL":
                from homemodels.models import reviewform
                #temp working
                allforms=reviewform.objects.filter(name=name)
                print(allforms)
                if (allforms.exists()):
                    messages.error(request,f"\U0001F641 Sorry {name} but you already submitted the form. If you want to submit again then try with a diffrent name.")
                else:
                #temp working
                    import datetime
                    obj=reviewform(name=name,email=email,phone=mob,message=msg,rating=rating,submit_time=datetime.datetime.now())
                    obj.save()
                    messages.success(request,f"\U0001F60A Dear {name},Thank you for Your time ,your form Submitted Successfuly,we will look into it Asap.")
    return render(request,'review.html')


# def submitmsg(request):
#     if request.method == 'GET':
#         if(len(request.GET.get)==0):
#             return HttpResponse("Please fill the form correctly")
#         else:
#             name=request.GET.get('name',"User")
#             email=request.GET.get('email',"default@default")
#             mob=request.GET.get('phone','0000000000')
#             msg=request.GET.get('message',"default message")
#             rating=request.GET.get('emojioption','happy')
#             print(name,email,mob,msg,rating)
#             from homemodels.models import reviewform
#             import datetime
#             obj=reviewform(name=name,email=email,phone=mob,message=msg,rating=rating,submit_time=datetime.datetime.now())
#             obj.save()
#             print(obj)
#             return HttpResponse("Form successfuly submitted")
#     else:
#         return HttpResponse("Please submit form correctly")