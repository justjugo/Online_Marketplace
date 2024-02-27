from django import forms
from .models import Item


classname='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
class EditItemForm(forms.ModelForm):

    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold')
        widgets={
            

            'name':forms.TextInput(attrs={
                 'class':classname
             }),

            'description':forms.Textarea(attrs={
                 'class':classname,
                 'rows':4,
             }),

            'price':forms.TextInput(attrs={
                 'class':classname
             }),

            'image':forms.FileInput(attrs={
                 'class':classname
             }),

            
        }


class NewItemForm(forms.ModelForm):

    class Meta:
        model=Item
        fields=('category','name','description','price','image')
        widgets={
            'category':forms.Select(attrs={
                'class':classname
            }),

            'name':forms.TextInput(attrs={
                 'class':classname
             }),

            'description':forms.Textarea(attrs={
                 'class':classname,
                 'rows':4,
             }),

            'price':forms.TextInput(attrs={
                 'class':classname
             }),

            'image':forms.FileInput(attrs={
                 'class':classname
             }),

            
        }

    
        
