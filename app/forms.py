from django import forms

class AppForm(forms.Form):
    title=forms.CharField(label="title",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
class AppsForm(forms.Form):
    file=forms.FileField(label="file",\
        widget=forms.FileInput(attrs={"class":"form-control"}))
    title=forms.CharField(label="title",\
        widget=forms.TextInput(attrs={"class":"form-control"}))
    giturl=forms.URLField(label="giturl",\
        widget=forms.URLInput(attrs={"class":"forms-control"}))
    link=forms.URLField(label="link",\
        widget=forms.URLInput(attrs={"class":"forms-control"}))
    tech=forms.CharField(label="tech",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
    content=forms.CharField(label="content",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))
    a1=forms.CharField(label="a1",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))