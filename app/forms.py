from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from.models import Apps,Message,User,Good

class AppForm(forms.Form):
    file=forms.FileField(label="file",\
        widget=forms.FileInput(attrs={"class":"forms-control"}))
    title=forms.CharField(label="title",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
    giturl=forms.URLField(label="gitrul",\
        widget=forms.URLInput(attrs={"class":"forms-control"}))
    link=forms.URLField(label="link",\
        widget=forms.URLInput(attrs={"class":"forms-control"}))
    tech=forms.CharField(label="tech",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
    content=forms.CharField(label="content",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
    a1=forms.CharField(label="a1",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
class FindForm(forms.Form):
    find=forms.CharField(label="find",\
        widget=TextInput(attrs={"class":"forms-control"}))
class AppsForm(forms.ModelForm):
    class Meta:
        model=Apps
        fields=["file","title","giturl","link","tech","content","a1"]

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=["title","content","apps"]
        
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control form-control-sm"}),
            "contnet":forms.Textarea(attrs={"class":"form-control form-control-sm","row":2}),
            "apps":forms.Select(attrs={"class":"form-control form-control-sm"}),
        }
class UserForm(forms.Form):
    user=forms.CharField(max_length=100,\
        widget=forms.TextInput(attrs={"class":"form-control","row":2}))
    mail=forms.EmailField(max_length=1000,\
        widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,\
        widget=forms.PasswordInput(attrs={"class":"form-control"})) 

class GoodForm(forms.ModelForm):
    class Meta:
        model=Good
        fields=["user","message"]