from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
#from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

#class LoginForm(forms.ModelForm):
    #domain = forms.CharField(error_messages={'required': 'domain required'})
 #   email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
  #  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

   # class Meta:
    #    model = User
     #   fields = ['email', 'password']


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'name': 'password'}))

    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password1', 'password2')


class UpdateUserModelFields(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email')

class UpdateUserProfileModelFields(forms.ModelForm):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    phonenumber = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    profile_picture = forms.ImageField(required=True)
    # gender = forms.CharField(required=True, widget=forms.RadioChoiceInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('address', 'phonenumber', 'gender', 'profile_picture')

