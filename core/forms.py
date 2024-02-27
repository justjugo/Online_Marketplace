from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SigninForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs=
                                                    {
                                                        
                                                        'name':"username",
                                                        'class':"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                                                        'placeholder':"Your name",
                                                        'required':""
                                                    }))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs=
                                                    {
                                                        
                                                        'name':"password2",
                                                        'class':"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
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
                                                        'class':"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                                                        'placeholder':"Your name",
                                                        'required':""
                                                    }))
    
    email=forms.CharField(widget=forms.EmailInput(attrs=
                                                    {
                                                        
                                                        'name':"email",
                                                        'class':"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                                                        'placeholder':"Exemple@gmail.com",
                                                        'required':""
                                                    }))
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs=
                                                    {
                                                        
                                                        'name':"password1",
                                                        'class':"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                                                        'placeholder':"••••••••",
                                                        'required':""
                                                    }))
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs=
                                                    {
                                                        
                                                        'name':"password2",
                                                        'class':"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                                                        'placeholder':"••••••••",
                                                        'required':""
                                                    }))