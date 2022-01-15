from django.shortcuts import render
import requests
import importlib
from django.db.models import Max,Min
#including homemodels for getting all the prodcatg and subcatg to be used in Making header link
from homemodels.models import prodcatglist



# Create your views here.

# Replacing '-' with '_' if any and also making it lowercase for Product category name and product subcategory name to avoid confusion 
# product category name (ex:- E-commerce -> e_commerce) 
# product category name (ex:- Top-Stock-Trading-and-investments-Apps -> top_stock_trading_and_investments_apps) 
#In templates of this app please make folder by proper name as {prodcatgname/prodsubcatgname.html}
def navigator(request,catgname,subcatgname):
    catgname=catgname.replace("-","_").lower() #Replacing '-' with '_' if any and also making it lowercase to avoid confusion
    subcatgname=subcatgname.replace("-","_").lower() #Replacing '-' with '_' if any and also making it lowercase to avoid confusion
    if(catgname=="e_commerce"):
        return e_commerce(request,catgname,subcatgname)
    elif(catgname=="fintech"):
        return fintech(request,catgname,subcatgname)
    #--------------------------import proablem solution -----------------------------#
    # proablem i faced :- how to import a class from a module using a variable as the class Name
    # that means lets suppose i have a module named models.py (or file models.py) and in that module i have a class named Products (so for simply(hard-coded) importing the class i write from models import Products , But Now i make a variable string as varstr="Products" ,Now using this varstr i have to import my Product class from my module .

    # solution :- first i import importlib (by writing import importlib) ->then using importlib.import_module("module_path or adress") i load my module and store into a var name mymodule ->now i have my module imported so now i use a getattr func to import classes from that module using string as class name {getattr(module,"class name") ->it takes module ,class name (as string) } and store that class in another variable called myclass.

    #overall code
    # import importlib
    # mymodule=importlib.import_module("module path")
    # myclass=getattr(mymodule,"class name")

    #-------------------------------------------------------------------#
def fintech(request,catgname,subcatgname):
    if(subcatgname=="top_stock_trading_and_investments_apps"):
        # path=catgname+"/"+subcatgname #to accessthe template
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        prodset=myclass.objects.all() #prodset stores query set containing all objects of my class
        # working to extract prodcatg model from homemodels.models starts here  
        stocknamesdict={"Infosys Ltd":'INFY',"Reliance Industries Ltd":'RELIANCE',"TCS Ltd":'TCS',"HDFC Bank Ltd":'HDFCBANK'}
        apikey="2JUWDOXY0IHC2FNU" #this is api key
        stockdict={}
        for stock,key in stocknamesdict.items():
          url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={key}.BSE&apikey={apikey}"
          try:
            response = requests.get(url)
            price=(response.json()['Global Quote']['05. price'])
            change=(response.json()['Global Quote']['10. change percent'])
            price=price[:-2]
            change=change[:-3]
            color="success"
            if(change[:1]=='-'):
              color="danger"
            #   change="-"+change
            else:
              change="+"+change
            temp={"stockname":stock,"price":price,"change":change,"color":color}
            stockdict.update({f"{stock}":temp})
          except (ConnectionError,TimeoutError,RuntimeError) as e:
            print(e)
        # prodcatglist_class=getattr(importlib.import_module("homemodels.models"),"prodcatglist")
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"prodset":prodset,"prodcatglist_allobjects":prodcatglist_allobjects,"stockdict":stockdict} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)
    
    elif(subcatgname=="best_cryptocurrency_trading_apps_in_india"):
        subcatgname="crypto_trading_apps" #change to give the model name and template name easy
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #prodset stores query set containing all objects of my class
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        cryptonamesdict={"Bitcoin":90,"Etherium":80,"Polygon":33536,"Tether":518}
        cryptodict={}
        for crypto,key in cryptonamesdict.items():
          url=f"https://api.coinlore.net/api/ticker/?id={key}"
          try:
            response = requests.get(url)
            price=(response.json()[0]['price_usd'])
            change=(response.json()[0]['percent_change_24h'])
            color="success"
            if(change[:1]=='-'):
              color="danger"
            #   change="-"+change
            else:
              change="+"+change
            temp={"cryptoname":crypto,"price":price,"change":change,"color":color}
            cryptodict.update({f"{crypto}":temp})
          except (ConnectionError,TimeoutError,RuntimeError) as e:
            print(e)
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"cryptodict":cryptodict} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="best_stock_market_courses_for_beginners"):
        subcatgname="stock_market_course" #change to easy model name
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),"online_course") #we can do all the courses with same class (filtering by coursecatg)
        filterset=myclass.objects.filter(coursecatg=f"{subcatgname}") #it store queryset containing all crypto_trading_course
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models #it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="best_free_crypto_trading_&_nft_courses"):
        subcatgname="crypto_trading_course" #change to easy model name
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),"online_course") #we can do all the courses with same class (filtering by coursecatg)
        filterset=myclass.objects.filter(coursecatg=f"{subcatgname}") #it store queryset containing all crypto_trading_course
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models #it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)



def e_commerce(request,catgname,subcatgname):
    if(subcatgname=="laptop"):
        # return render(request,f"allcatgprods/e_commerce/laptop.html")
        optval=2 #doing this for making it global
        spclcatg="general" #setting default value of special category
        if 'options' in request.GET:
            optval=int(request.GET.get('options',2))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=40000
        maxp=60000
        if(optval<=3 and optval>=0):
            minp=20000*optval
            maxp=20000*(optval+1)
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==4): #80000 and above
            minp=20000*optval
            filterset=myclass.objects.filter(spclcatg="general")
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price'] #read this aggregate function on documentation very well explained https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
            filterset=filterset.filter(minp__range=(minp,maxp))
        elif(optval==5): #gaming laptops
            filterset=myclass.objects.filter(spclcatg="gaming")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            spclcatg="gaming"
        elif(optval==6): #touchscreeen foldable laptops
            filterset=myclass.objects.filter(spclcatg="touchscreen foldable")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            spclcatg="touchscreen foldable"
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp,"spclcatg":spclcatg} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="mobile"):
        # return render(request,f"allcatgprods/e_commerce/laptop.html")
        optval=3 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',2))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=13000
        maxp=16000
        spclcatg="general" #setting default value of special category
        if(optval==0): #below 7999 #
            minp=0
            maxp=7999
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==1): #8000 to 10999
            minp=8000
            maxp=10999
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==2): #11000 to 14999
            minp=11000
            maxp=14999
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==3): #15000 to 19999
            minp=15000
            maxp=19999
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==4): #20000 to 24999
            minp=20000
            maxp=24999
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==5): #25000 above
            minp=25000
            filterset=myclass.objects.filter(spclcatg="general")
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price'] #read this aggregate function on documentation very well explained https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
            filterset=filterset.filter(minp__range=(minp,maxp))
        elif(optval==6):#best camera phones
            filterset=myclass.objects.filter(spclcatg="camera")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            spclcatg="camera"
        elif(optval==7): #best gaming phones
            filterset=myclass.objects.filter(spclcatg="gaming")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            spclcatg="gaming"
        elif(optval==8): #best keypad phones.
            filterset=myclass.objects.filter(spclcatg="keypad")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            spclcatg="keypad"
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp,"spclcatg":spclcatg} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="camera"):
        optval=0 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',0))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=0
        maxp=0
        spclcatg="general" #setting default value of special category
        if(optval==0):#Best Camera for Bloggers
            filterset=myclass.objects.filter(spclcatg="blogging")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            spclcatg="blogging"
        elif(optval==1): #0 - 15000
            minp=0
            maxp=15000
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==2): #15000 - 30000
            minp=15000
            maxp=30000
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==3): #30000 - 50000
            minp=30000
            maxp=50000
            filterset=myclass.objects.filter(spclcatg="general",minp__range=(minp,maxp))
        elif(optval==4): #50000 and above
            minp=50000
            filterset=myclass.objects.filter(spclcatg="general")
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price'] #read this aggregate function on documentation very well explained https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
            filterset=filterset.filter(minp__range=(minp,maxp))
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp,"spclcatg":spclcatg} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="smart_t.v"):
        subcatgname="smart_tv"
        optval=0 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',0))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=0
        maxp=0
        screensize="32 inch"
        if(optval==0):#32 inch
            filterset=myclass.objects.filter(dispsize="32 inch")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
        elif(optval==1): #43 inch
            filterset=myclass.objects.filter(dispsize="43 inch")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            screensize="43 inch"
        elif(optval==2): #55 inch
            filterset=myclass.objects.filter(dispsize="55 inch")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            screensize="55 inch"
        elif(optval==3): #60 inch
            filterset=myclass.objects.filter(dispsize="60 inch")
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            screensize="60 inch"
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp,"screensize":screensize} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="earphone"):
        optval=0 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',0))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=0
        maxp=0
        if(optval==0):#Under 500
            min=0
            max=500
            filterset=myclass.objects.filter(minp__range=(0,500))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
        elif(optval==1): #500 to 1000
            filterset=myclass.objects.filter(minp__range=(500,1000))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
        elif(optval==2): #more thn 1000
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            filterset=myclass.objects.filter(minp__range=(1000,maxp))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)   

    elif(subcatgname=="headphone"):
        optval=0 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',0))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=0
        maxp=0
        if(optval==0):#Under 1000
            filterset=myclass.objects.filter(minp__range=(0,1000))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
        elif(optval==1): #1000 and above
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            filterset=myclass.objects.filter(minp__range=(1000,maxp))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="earpod"):
        optval=0 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',0))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=0
        maxp=0
        if(optval==0):#Under 1000
            filterset=myclass.objects.filter(minp__range=(0,1000))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
        elif(optval==1): #1000 and above
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            filterset=myclass.objects.filter(minp__range=(1000,maxp))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)

    elif(subcatgname=="trimmer"):
        optval=0 #doing this for making it global
        if 'options' in request.GET:
            optval=int(request.GET.get('options',0))
        myclass=getattr(importlib.import_module(f"allcatgprods.models"),f"{subcatgname}")
        filterset=myclass.objects.all() #initially filterset contains all the products of subcatgclass
        minp=0
        maxp=0
        if(optval==0):#Under 2000
            filterset=myclass.objects.filter(minp__range=(0,2000))
            minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
            maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
            # we will add more price options soon 
        # elif(optval==1): #2000 and above
        #     maxp=filterset.aggregate(maximum_price=Max('minp'))['maximum_price']
        #     filterset=myclass.objects.filter(minp__range=(1000,maxp))
        #     minp=filterset.aggregate(minimum_price=Min('minp'))['minimum_price']
        prodcatglist_allobjects=prodcatglist.objects.all() #this stores all the object of prodcatglist class of homemodels.models 3it is a common code in all category
        mydict={"filterset":filterset,"prodcatglist_allobjects":prodcatglist_allobjects,"minimumprice":minp,"maximumprice":maxp} #we will also add the prodcatglist_allobjects in mydict
        return render(request,f"allcatgprods/{catgname}/{subcatgname}.html",mydict)