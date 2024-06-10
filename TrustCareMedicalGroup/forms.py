from django import forms
from .models import Doctor,Patient


class AddDoctor(forms.ModelForm):
    GENDER_CHOICES = [
        ('', '[Select]'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'specialization', 'phone', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            # 'date_of_birth': forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'})),
            # 'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specialization'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

class LoginDoctor(forms.ModelForm):
    class Meta:
        model = Doctor

        fields = ('email','password')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }


class AddPatient(forms.ModelForm):
    GENDER_CHOICES = [
        ('', '[Select]'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'doctor_id', 'gender', 'date_of_birth', 'phone', 'email', 'password', 'address', 'city', 'state', 'country', 'zip_code']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'doctor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor ID'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            # 'date_of_birth': forms.DateField(attrs={'class':'datepicker','is_hidden'='false'}),
            # 'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'address' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), 
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip code'}),
        }

class LoginPatient(forms.ModelForm):
    class Meta:
        model = Patient

        fields = ['email', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }