from django.urls import path

from .views import detail,category,newitem,delete,edititem,items

app_name='item'

urlpatterns =[
    path("<int:pk>/",detail,name='detail'),
    path("categorie/<int:fk>/",category,name='categorie'),
    path("browser/",items,name='browser'),
    path("newitem/",newitem,name='newitem'),
    path("<int:pk>/delete/",delete,name='delete'),
    path("<int:pk>/edit/",edititem,name='edititem'),
]
