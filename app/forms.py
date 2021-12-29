from django import forms
from.models import Apps
class AppForm(forms.Form):
    title=forms.CharField(label="title",\
        widget=forms.TextInput(attrs={"class":"forms-control"}))

    
class AppsForm(forms.ModelForm):
    class Meta:
        model=Apps
        fields=["file","title","giturl","link","tech","content","a1"]