from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)

    class Meta:
        ordering=('name',)
        verbose_name_plural="Categories"
    
    def __str__(self):
        return self.name
    
class Item (models.Model):
     category= models.ForeignKey(Category,related_name='items', on_delete=models.CASCADE)
     name= models.CharField(max_length=100)
     description = models.TextField(null=True, blank=True)
     price= models.FloatField()
     image=models.ImageField(upload_to='item_image',blank=True,null=True)
     is_sold= models.BooleanField(default=False)
     created_by= models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
     created_at=models.DateTimeField(auto_now_add=True)
     class Meta:
        ordering=('-created_at',)
        verbose_name_plural="Items"
     def __str__(self):
        return self.name
    
    


     
    