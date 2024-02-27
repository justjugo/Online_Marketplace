from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SigninForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs=
                                                    {
                                                        
                                                        'name':"username",
                                                        'class':"w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                                                        'placeholder':"Your name",
                                                        'required':""
                                                    }))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs=
                                                    {
                                                        
                                                        'name':"password2",
                                                        'class':"w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                                                        'placeholder':"••••••••",
                                                        'required':""
                                                    }))

   


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username=forms.CharField(widget=forms.TextInput(attrs=
                                                    {
                                                        
                                                        'name':"username",
                                                        'class':"w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                                                        'placeholder':"Your name",
                                                        'required':""
                                                    }))
    
    email=forms.CharField(widget=forms.EmailInput(attrs=
                                                    {
                                                        
                                                        'name':"email",
                                                        'class':"w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                                                        'placeholder':"Exemple@gmail.com",
                                                        'required':""
                                                    }))
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs=
                                                    {
                                                        
                                                        'name':"password1",
                                                        'class':"w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                                                        'placeholder':"••••••••",
                                                        'required':""
                                                    }))
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs=
                                                    {
                                                        
                                                        'name':"password2",
                                                        'class':"w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                                                        'placeholder':"••••••••",
                                                        'required':""
                                                    }))