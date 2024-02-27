from django.db import models
from item.models import Item
from django.contrib.auth.models import User
# Create your models here.

class Conversation(models.Model):
    item=models.ForeignKey(Item,related_name='conversation',on_delete=models.CASCADE)
    members= models.ManyToManyField(User,related_name='conversation')
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-modified_at',)
     
    def __str__(self):
        return str(self.item.name)

    
    
class ConversationMessage(models.Model):
    conversation=models.ForeignKey(Conversation,related_name="conversation", on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="created_by",on_delete=models.CASCADE)
    class Meta:
        ordering=('created_at',)
    
    def __str__(self):
        return str(self.body)

    

    
