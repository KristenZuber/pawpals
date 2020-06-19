from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile, Apply

# Define fields for the registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Define fields for the update form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = False)

    class Meta:
        model = User
        fields = ['username', 'email']

# Define fields for the apply form
class UserApplyForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Apply
        labels = {
        'first_name':'First Name',
        'last_name':'Last Name',
        'email':'Email',
        'phone_number':'Phone Number',
        'answer1':'Who are you interested in adopting? (name)',
        'answer2':'How many pets do you have at home?',
        'answer3':'How much time do you have to devote to a pet? (hours/day)',
        }
        fields = [
        'first_name', 'last_name', 'email', 'phone_number', 'answer1', 'answer2', 'answer3'
        ]
