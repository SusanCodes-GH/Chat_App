from django import forms
from django.forms import ModelForm
from .models import Chatmsg

class Chatmsgform(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":1, "placeholder":"Type here..."}))
    class Meta:
        model = Chatmsg
        fields = ["body",]