
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Officer

class OfficerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Officer 
        fields = ('login_id', 'password')
class OfficerChangeForm(UserChangeForm):

    class Meta:
        model = Officer
        fields = UserChangeForm.Meta.fields