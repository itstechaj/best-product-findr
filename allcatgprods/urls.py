#i created this
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from homemodels.models import prodcatglist

urlpatterns =[
    path('<subcatgname>/',views.navigator),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)