from django.forms import fields
from django.forms import widgets
from myapp.models import UserDetails
from django import forms
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm , AuthenticationForm, UsernameField,PasswordResetForm , PasswordChangeForm, SetPasswordForm
from django.forms.fields import CharField
PasswordResetForm , SetPasswordForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, Widget
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation


class UserRegistration(UserCreationForm):
    username = forms.CharField (label= 'Username' , widget = forms.TextInput( attrs={'class' : 'form-control'}))
    email = forms.CharField (required= True ,label='Email' , widget = forms.EmailInput( attrs = {'class' : 'form-control'}))
    password1 = forms.CharField(label='Password' , widget= forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Coanfirm password(agian)' , widget= forms.PasswordInput(attrs={'class' : 'form-control'}))


    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class' : 'form-control' , 'autofocus': True}))
    password = forms.CharField(label=_("Password"), strip = False , widget=forms.PasswordInput(attrs =
    {'autocomplete' : 'current-password' ,'class' : 'form-control'
    }))



class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old password') , strip=False , widget=forms.PasswordInput
    (attrs={'autocomplete_complete' : 'current_password' , 'autofocus' : True , 'class' : 'form-control'}))

    new_password1 = forms.CharField(label=_('New password'), strip=False , widget=forms.PasswordInput(attrs={
        'autocomplete' : 'new-password' , 'class':'form-control'}),
         help_text = password_validation.
        password_validators_help_text_html())

    new_password2 = forms.CharField(label=_('Confirm new password') , strip=False , widget=forms.PasswordInput(attrs={
        'autocomplete' : 'new-password' , 'class' : 'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Enter your registered email' , max_length=254 , widget=forms.EmailInput(attrs={
        'autocomplete' : 'email' , 'class' : 'form-control'}))




class SetMyPassword(SetPasswordForm):
    new_password1 = forms.CharField(label= 'New Pasword' , strip=False , widget=forms.PasswordInput(attrs=
    { 'autocomplete' : 'new-password' , 'class' : 'form-control'}),
    help_text=password_validation.
    password_validators_help_text_html())

    new_password2 = forms.CharField(label=('Confrim new password') , strip=False , widget = forms.PasswordInput(attrs={
        'autocomplte' : 'new-password' , 'class' : 'form-control'
     }))


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        labels = {'first_name' : 'First_Name ' , 'last_name' : 'Last_Name ' , 'mobile_number' : 'Mobile_Number' , 'area_and_street' : 'Area_&_Street' }
        fields = [ 'first_name' , 'last_name' , 'mobile_number' , 'email' , 'locality' , 'area_and_street' , 'city'
        , 'pincode' , 'landmark' , 'state']

        widgets = {'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        'mobile_number' : forms.NumberInput(attrs={'class' : 'form-control'}),
        'email' : forms.EmailInput(attrs={'class' : 'form-control'}),       
        'locality' : forms.TextInput(attrs={'class' : 'form-control'}),
        'area_and_street' : forms.Textarea(attrs={'class' : 'form-control'}),
        'city' : forms.TextInput(attrs={'class' : 'form-control'}),
        'pincode' : forms.NumberInput(attrs={'class' : 'form-control'}),
        'landmark' : forms.TextInput(attrs={'class' : 'form-control'}),
        'state' : forms.TextInput(attrs={'class' : 'form-control'})}
