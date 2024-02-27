from django import forms
from .models import ConversationMessage

classname='w-full py-2 pl-4 pr-10 text-sm bg-gray-100 border border-transparent appearance-none rounded-tg placeholder-gray-400 focus:bg-white focus:outline-none focus:border-blue-500 focus:text-gray-900 focus:shadow-outline-blue'
style="border-radius: 25px"
placeholder="Senda message"
autocomplete="off"

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage  # Specify your model here
        fields = ('body',)  # Specify the fields you want in the form
        widgets = {
        'body': forms.TextInput(attrs={
            'class': classname ,
            'style':style,
            'placeholder':placeholder,
            'autocomplete':autocomplete

        })
    }
    
  
    