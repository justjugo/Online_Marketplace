from django.shortcuts import render,get_object_or_404,redirect
from .models import Conversation,ConversationMessage
from item.models import Item
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.



@login_required
def  message(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)

    if(item.created_by==request.user):
        return redirect('dashboard:index')

    conversation= Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        return redirect('conversation:details',conversation.get().pk)

    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)
 
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            return redirect('conversation:details',conversation.id)
        
        
           
        
    else:
        
        form=ConversationMessageForm()

    return  render(request,'conversation/new.html',{
        'form':form,
        'item':item
    })

@login_required
def inbox(request):
    
    query = request.GET.get('query','')

    if query:
        print("quesrry seted")
        conversations=Conversation.objects.filter(Q(members__in=[request.user.id]) & Q(item__name__icontains=query) | Q(item__description__icontains=query)  )
    else:
        conversations = Conversation.objects.filter(members__in=[request.user.id])


    return render(request,'conversation/inbox.html',{
        'conversations':conversations,
         'query':query
        

    })





@login_required
def details(request,pk):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    conversation = Conversation.objects.get(pk=pk)

    if request.method =='POST':
        form=ConversationMessageForm(request.POST)

        if form.is_valid:
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:details',pk)
        
    else:
         form=ConversationMessageForm()

           

    
    return render(request,'conversation/details.html',{
        
        'conversation':conversation,
        'conversations':conversations,
        'form':form

    })


