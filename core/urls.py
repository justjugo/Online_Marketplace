from django.urls import path
from django.contrib.auth import views 
from .views import index, contact,signup
from .forms import SigninForm
app_name='core'

urlpatterns= [
 path('',index,name='index'),
 path('contact/', contact, name='contact'),
 path('signup/',signup,name='signup'),
 path('login/',views.LoginView.as_view(template_name='core/login.html',authentication_form= SigninForm),name='login')

]