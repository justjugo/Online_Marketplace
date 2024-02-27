from django.shortcuts import render,redirect
from item.models import Item,Category
from .forms import SignupForm
# Create your views here.

def index(request):

    context={
    'items':Item.objects.filter(is_sold=False)[:6],
    'categories':Category.objects.all()
    }
   
    return render(request,"core/index.html",context)


def contact(request):
    return render(request,"core/contact.html",{})

def signup(request):
    if (request.method=='POST'):
        form=SignupForm(request.POST)
        if(form.is_valid):
            form.save()
            print("done")
    
    form=SignupForm()
    context={'form':form}

    return render(request,'core/signup.html',context)