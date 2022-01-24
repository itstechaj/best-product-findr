from django.db import models
from django.db.models.fields import CharField

# Create your models here.
#Here you create all the Subcategory models (it means that Total no of models = Total no. of subcategory you have )
#ex :- you create one class for mobile one for laptop one for stock trading app one for crypto and so onn...

#You should Add model with same name that is used as subcategory name on home page (With All spaces between word replaced to _(underscore) and total charecters converted into lowercase) 
#Ex :- for Top Stock Trading and Investments Apps (so class name is "top_stock_trading_and_investments_apps")

#common class
class commonclass(models.Model):
    name=models.CharField(verbose_name="Name of Product",max_length=100) #stores the product name
    rating=models.DecimalField(verbose_name="User Rating",max_digits=2,decimal_places=1) #it stores the User rating of Product out of 5 (in decimal ex :- 4.5,4.6,4.7....)
    pros=models.TextField(verbose_name="Enter Pros (using'/'to seperate)",max_length=500) #it stores the pros list Enter '/' to Write next pro.
    cons=models.TextField(verbose_name="Enter Cons (using'/'to seperate)",max_length=500) #it stores the cons list Enter '/' to Write next con.
    upr=models.TextField(verbose_name="Users +ve review(using'/'to seperate)") #it stores the Users Positive Review list Enter '/' to Write next Users Positive Review.
    unr=models.TextField(verbose_name="Users -ve review(using'/'to seperate)") #it stores the Users Negative Review list Enter '/' to Write next Users Negative Review.
    youtubelink=models.URLField(verbose_name="Youtube Reveiw/Comparision link", max_length=200) #it stores the Youtube Reveiw/Comparision link for the product
    
    # This code Below makes its parent class as common class and we can just give this common class as argument for next class to inherit this common class
    class Meta: 
        abstract = True

class price(models.Model):
    amazonp=models.CharField(verbose_name="Price on Amazon",max_length=40)
    amazonlink=models.URLField(verbose_name="Amazon Link")
    flipkartp=models.CharField(verbose_name="Price on Flipkart",max_length=40)
    flipkartlink=models.URLField(verbose_name="Flipkart link")
    officialp=models.CharField(verbose_name="Price on Official store",max_length=40)
    officiallink=models.URLField(verbose_name="Official link")
    minp=models.PositiveIntegerField(verbose_name="Minimum Price")
    minplink=models.URLField(verbose_name="Minimum Price Link")
    minpseller=models.CharField(verbose_name="Minimum Price Seller",max_length=50)
    # This code Below makes its parent class as common class and we can just give this common class as argument for next class to inherit this common class
    class Meta: 
        abstract = True
    
#Class for Top Stock Trading and Investments Apps
class best_stock_trading_apps(commonclass): #giving coomonclass as argument means it inherit feilds from the commonclass
    rank=models.PositiveSmallIntegerField(verbose_name="App Rank") #stores the Rank at which it displays
    aoc=models.PositiveSmallIntegerField(verbose_name="Account opening charge") #stores Account opening charge
    amc=models.PositiveSmallIntegerField(verbose_name="Account maintenance charge") #stores Account maintenance charge
    edc=models.CharField(verbose_name="Equity Delivery Charges",max_length=50) #stores the Equity Delivery charges
    idc=models.CharField(verbose_name="Intraday Charges",max_length=50) #stores the Intraday charges
    fc=models.CharField(verbose_name="Future Charges",max_length=50) #stores the Future charges
    oc=models.CharField(verbose_name="Option Charges",max_length=50) #stores the option charges
    dpc=models.CharField(verbose_name="DP charge",max_length=50) #stores the Depositiry charges
    est=models.PositiveSmallIntegerField(verbose_name="Establishment Year") #stores the Establishment Year
    calc=models.URLField(verbose_name="Brokerage Calculator Link", max_length=200) #it stores the Link of Brokerage Calculator of the App
    applink=models.URLField(verbose_name="App/Website link", max_length=200) #it stores the Link of App/Website (further use as referral link)
    appimg=models.ImageField(verbose_name="Product image",upload_to="fintech/top_stock_trading_and_investments_apps/img/",default="defaultimg/") #stores the image of the product 
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class crypto_trading_apps(commonclass): #giving coomonclass as argument means it inherit feilds from the commonclass
    rank=models.PositiveSmallIntegerField(verbose_name="App Rank") #stores the Rank at which it displays
    aoc=models.PositiveSmallIntegerField(verbose_name="Account opening charge") #stores Account opening charge
    cryptoavialable=models.PositiveSmallIntegerField(verbose_name="No. of Cryptos avialable") #stores no. of crypto avialable
    makerfees=models.CharField(verbose_name="Maker fees (in percent)",max_length=50) #stores the Maker fees
    takerfees=models.CharField(verbose_name="Taker fees (in percent)",max_length=50) #stores the taker fees
    withdrawlfees=models.CharField(verbose_name="Withdrawl fees (in BTC)",max_length=50) #stores the withdrawl fees in BTC
    minwdllimit=models.CharField(verbose_name="Minimum withdrawl limit (in BTC)",max_length=50) #stores the Mini withdrawl limit (in BTC)
    est=models.PositiveSmallIntegerField(verbose_name="Establishment Year") #stores the Establishment Year
    applink=models.URLField(verbose_name="App/Website link", max_length=200) #it stores the Link of App/Website (further use as referral link)
    appimg=models.ImageField(verbose_name="Product image",upload_to="fintech/crypto_trading_apps/img/",default="defaultimg/") #stores the image of the product 
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class online_course(commonclass):
    coursecatg=models.CharField("Category name of course",max_length=200)#ensure to give coursecatgname same as subcatgname in veiws.py
    rank=models.PositiveSmallIntegerField(verbose_name="App Rank") #stores the Rank at which it displays
    designedfor=models.CharField("Designed/Suitable for",max_length=100) # here we fill like : Beginners, Medium level...etc
    courselength=models.CharField("Course length",max_length=100) # Course length in week and hours both
    coursefees=models.CharField("Course Fees",max_length=100) # Course fees Here we only fill Free
    coursecertificate=models.CharField("Course include certificate ?",max_length=200) # Course include certificate (here we answer yes and no (also add if any exam is needed for certificate )
    studentscompleted=models.CharField("No. of Students Completed",max_length=150) # students completed Number
    courseplatform=models.CharField("Course platform",max_length=100) #platform at which course is available
    courseteacher=models.CharField("Course teacher name & details",max_length=300) #Corse teacher name and details
    prerequisite=models.CharField("Prerequisite of course",max_length=250) # students completed Number
    courselink=models.URLField("Course Link")
    prodimg=models.ImageField(verbose_name="Course image",upload_to=f"fintech/{coursecatg}/img/",default="defaultimg/")
    def __str__(self):
        return " ".join([str(self.rank),self.name])
    
class laptop(commonclass,price):
    #Full specification table feild starts here 
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    weight=models.CharField(verbose_name="Items Weight",max_length=10)
    color=models.CharField(verbose_name="Colour",max_length=20)
    os=models.CharField(verbose_name="Operating system",max_length=20)
    bb=models.CharField(verbose_name="Battery Backup",max_length=20)
    proc=models.CharField(verbose_name="Processor",max_length=50)
    clockspeed=models.CharField(verbose_name="Processor Clock speed",max_length=200)
    gproc=models.CharField(verbose_name="Graphic processor",max_length=50)
    ram=models.CharField(verbose_name="Ram Capacity",max_length=15)
    refreshrate=models.CharField(verbose_name="Refresh rate",max_length=15)
    ssd=models.CharField(verbose_name="SSD Capacity",max_length=20)
    cache=models.CharField(verbose_name="Cache",max_length=10)
    graphiccard=models.CharField(verbose_name="Graphic card Memory",max_length=10)
    noc=models.CharField(verbose_name="Number of cores",max_length=2)
    dispsize=models.CharField(verbose_name="Display Size",max_length=50)
    dispres=models.CharField(verbose_name="Display Resolution",max_length=50)
    touchscr=models.CharField(verbose_name="Touch Screen",max_length=5)
    disptype=models.CharField(verbose_name="Display type",max_length=150)
    webcam=models.CharField(verbose_name="Web-Cam",max_length=50)
    mic=models.CharField(verbose_name="In-built Microphone",max_length=50)
    speakers=models.CharField(verbose_name="Speakers",max_length=80)
    usbport=models.CharField(verbose_name="USB ports",max_length=150)
    hdmiport=models.CharField(verbose_name="HDMI ports",max_length=150)
    backlit=models.CharField(verbose_name="Backlit Keyboard",max_length=25)
    fingerprint=models.CharField(verbose_name="Fingerprint Scanner",max_length=20)
    retina=models.CharField(verbose_name="Retina Scanner",max_length=20)
    warrenty=models.CharField(verbose_name="Warrenty",max_length=50)
    #Full specification table feild Ends here 
    #the below feild can change accordingly with product category
    spclcatg=models.CharField(verbose_name="Special Category",max_length=50)
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/laptop/img/",default="defaultimg/")
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class mobile(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    weight=models.CharField(verbose_name="Items Weight",max_length=10)
    color=models.CharField(verbose_name="Colour",max_length=20)
    os=models.CharField(verbose_name="Operating system",max_length=20)
    battery=models.CharField(verbose_name="Battery Backup",max_length=100) #here we give battery capacity in mah
    proc=models.CharField(verbose_name="Processor",max_length=50)
    clockspeed=models.CharField(verbose_name="Processor Clock speed",max_length=200)
    gproc=models.CharField(verbose_name="Graphic processor",max_length=50)
    ram=models.CharField(verbose_name="Ram Capacity",max_length=25)
    memory=models.CharField(verbose_name="Memory",max_length=25)
    simslot=models.CharField(verbose_name="Sim card Slot",max_length=100)
    memoryslot=models.CharField(verbose_name="Memory Slots",max_length=50)
    dispsize=models.CharField(verbose_name="Display Size",max_length=50)
    dispres=models.CharField(verbose_name="Display Resolution",max_length=50)
    fingerscan=models.CharField(verbose_name="Touch Screen",max_length=20)
    facescan=models.CharField("Face scan",max_length=20)
    speakers=models.CharField(verbose_name="Speakers",max_length=80)
    camera=models.CharField(verbose_name="Camera details",max_length=150) #give here both camera details (rear +front)
    videorec=models.CharField(verbose_name="Video Recording",max_length=100)
    spclcatg=models.CharField(verbose_name="Special Category",max_length=50) #here give a special category like gaming ,camera,general
    metallicbody=models.CharField("Metallic Body",max_length=30)
    warrenty=models.CharField(verbose_name="Warrenty",max_length=50)
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/mobile/img/",default="defaultimg/")
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class camera(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    battery=models.CharField(verbose_name="Battery details",max_length=100) #here we give battery composition details with volt
    dispsize=models.CharField(verbose_name="Display Size",max_length=50)#here we give display type + size
    dim=models.CharField(verbose_name="Product Dimension",max_length=200)#here we give dimension+weight
    pixel=models.CharField(verbose_name="Optical res(in pixel)",max_length=100)# here we give pixel of the camera ex:- 18MP , 20 MP
    mountinghardware=models.CharField(verbose_name="Mounting Hardware(In the box)",max_length=400) #here we give what inside the pakaging of the camera 
    shutterspeed=models.CharField(verbose_name="Minimum Shutter speed",max_length=100) #here we give minimum shutter speed
    focallength=models.CharField(verbose_name="Minimum Focal length",max_length=100) #here we give minimum focal length
    fps=models.CharField(verbose_name="Continuos shooting speed(in fps)",max_length=100) #here we give continuos shooting speed (in fps)
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/camera/img/",default="defaultimg/")
    warrenty=models.CharField(verbose_name="Warrenty",max_length=100)
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    spclcatg=models.CharField(verbose_name="Special Category",max_length=100) #here give a special category like gaming ,camera,general
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class smart_tv(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    dispsize=models.CharField(verbose_name="Display Size",max_length=50)#here we give display size in inch
    dispres=models.CharField(verbose_name="Display Resolution",max_length=50)#here we give display resolution eg:- 1920*1080px
    dispresstd=models.CharField(verbose_name="Display Resolution std",max_length=50)#here we give display resolution standard eg:- 4k, HD+ etc
    color=models.CharField(verbose_name="Product color",max_length=50)#here we give color
    smarttv=models.CharField(verbose_name="Is it smart Tv",max_length=50) #here we give yes or no
    #sound details
    noofspeakers=models.CharField(verbose_name="No. of Speakers",max_length=50) #here we give total no. of speakers it has
    speakername=models.CharField(verbose_name="Name of Speaker",max_length=150) #here we give name of speakers and it technology eg:-Dolby Atmos, DTS-HD
    #smarttv features
    noofcores=models.CharField(verbose_name="No. of Cores",max_length=50) #here we give number of cores eg:- quad or ,4,
    ram=models.CharField(verbose_name="Ram",max_length=50) #here we give Ram in GB
    internalstorage=models.CharField(verbose_name="Internal storage",max_length=100) #here we give internal memory storage in GB
    os=models.CharField(verbose_name="Operating system of T.v",max_length=100) #here we give operating system details
    supportedapps=models.CharField(verbose_name="Supported apps(list)",max_length=200) #here we give list of apps (comma seperated) eg:- youtube,netflix,amazon prime
    warrenty=models.CharField(verbose_name="Warrenty",max_length=150)
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/smart_tv/img/",default="defaultimg/")
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class earphone(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    drivers=models.CharField(verbose_name="Drivers size",max_length=50)#here we give drivers size in mm
    inbuitmic=models.CharField(verbose_name="In-built mic",max_length=50)#here we ans as Yes and No
    noisecancellation=models.CharField(verbose_name="Noise cancellation",max_length=50)#here we give Yes and No 
    color=models.CharField(verbose_name="Product color",max_length=50)#here we give color
    wirelength=models.CharField(verbose_name="Length of wire",max_length=50) #here we give length of wire as L,M
    earbudsize=models.CharField(verbose_name="Size of Earbud",max_length=50) #here we give size of earbud as M l s or any other format
    tangelfree=models.CharField(verbose_name="Is wires tangel free",max_length=50) #here we give yes or no
    warrenty=models.CharField(verbose_name="Warrenty",max_length=150)
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/earphone/img/",default="defaultimg/")
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class headphone(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    drivers=models.CharField(verbose_name="Drivers size",max_length=50)#here we give drivers size in mm
    inbuitmic=models.CharField(verbose_name="In-built mic",max_length=50)#here we ans as Yes and No
    noisecancellation=models.CharField(verbose_name="Noise cancellation",max_length=50)#here we give Yes and No 
    color=models.CharField(verbose_name="Product color",max_length=50)#here we give color
    wirelength=models.CharField(verbose_name="Length of wire",max_length=50) #here we give length of wire as L,M
    headphonetype=models.CharField(verbose_name="Headphone type",max_length=50) #here we give In ear,Over ear etc...
    warrenty=models.CharField(verbose_name="Warrenty",max_length=150)
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/headphone/img/",default="defaultimg/")
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class earpod(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    playbacktime=models.CharField(verbose_name="Play time after full charge",max_length=100)#here we give earpod play time after full charge
    inbuiltmic=models.CharField(verbose_name="In-built mic",max_length=50)#here we ans as Yes and No
    color=models.CharField(verbose_name="Product color",max_length=50)#here we give color
    dimension=models.CharField(verbose_name="Enter dimension (with weight)",max_length=200) #here we give dimension +weight of Earpod
    battery=models.CharField(verbose_name="Full battery details",max_length=150) #here we give Full battery details
    waterresistant=models.CharField(verbose_name="Waterproof details",max_length=150) #give here details about waterproof
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/earpod/img/",default="defaultimg/")
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    def __str__(self):
        return " ".join([str(self.rank),self.name])

class trimmer(commonclass,price):
    rank=models.PositiveSmallIntegerField(verbose_name="Rank of product")
    model=models.CharField(verbose_name="Model No.",max_length=30)
    batteryruntime=models.CharField(verbose_name="Run time in Full charge",max_length=100)#here we give earpod battery runtime
    chargingtime=models.CharField(verbose_name="Charging time(for full)",max_length=50)#here we give time to full charge
    color=models.CharField(verbose_name="Product color",max_length=50)#here we give color
    washablehead=models.CharField(verbose_name="Washable head",max_length=200) #here we give that its head is washable is not
    waterresistant=models.CharField(verbose_name="Waterproof details",max_length=150) #give here details about waterproof
    lengthadjustment=models.CharField(verbose_name="How many length adjustment",max_length=50)
    warrenty=models.CharField(verbose_name="Warrenty",max_length=150)
    prodimg=models.ImageField(verbose_name="Product image",upload_to="e_commerce/trimmer/img/",default="defaultimg/")
    reliancep=models.CharField(verbose_name="Price on Reliance Digital",max_length=40) #this feild can be changed according to category
    reliancelink=models.URLField(verbose_name="Reliance Link")
    def __str__(self):
        return " ".join([str(self.rank),self.name])