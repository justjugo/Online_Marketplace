from django.urls import path

from .views import message,inbox,details

app_name= 'conversation'

urlpatterns=[
    path('inbox/',inbox,name='inbox'),
    path('<int:pk>/',details,name='details'),
    path('inbox/',inbox,name='inbox'),
    path('new/<int:item_pk>/',message,name='new')
]