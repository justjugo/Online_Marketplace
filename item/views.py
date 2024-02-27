from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import Item, Category
from .forms import NewItemForm,EditItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def items(request):
    query = request.GET.get('query','')
    items=Item.objects.all()

    if query:
        items=Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context={
        'items':items,
        'query':query
    }

    return render(request,"item/brows.html",context)



def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_item=Item.objects.filter(category=item.category,is_sold=False)[:3]
    context={
        'item':item,
        'related_item':related_item

    }
    
    return render(request,'item/details.html',context)

def category(request,fk):
    items=get_list_or_404(Item,category_id=fk)
    category=get_object_or_404(Category,id=fk)
    print(category.name)
    context={
        'category':category,
        'items':items
    }

    return render(request,'item/category.html',context)

@login_required
def newitem(request):
    if (request.method=='POST'):
        form=NewItemForm(request.POST,request.FILES)
        if(form.is_valid):
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()

            return redirect('item:detail',pk=item.id)

    else:
        form=NewItemForm()

    context={
        'form':form

    }
    
    return render(request,'item/newitem.html',context)


@login_required
def edititem(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if (request.method=='POST'):
        form=EditItemForm(request.POST,request.FILES,instance=item)
        if(form.is_valid):
            form.save()

            return redirect('item:detail',pk=item.id)

    else:
        form=EditItemForm(instance=item)

    context={
        'form':form

    }
    
    return render(request,'item/newitem.html',context)

@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

    
