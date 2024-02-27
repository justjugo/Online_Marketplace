from django.urls import path
from .views import myitems


app_name='dashboard'

urlpatterns =[
    
    path("",myitems,name='index')
]