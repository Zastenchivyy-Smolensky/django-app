from django.db import models
from django.contrib.auth.models import User

class Apps(models.Model):
    file = models.FileField(upload_to="file/%Y/%m/%d")
    title= models.CharField(max_length=100)
    giturl=models.TextField(max_length=10000)
    link=models.TextField(max_length=10000)
    tech=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    a1=models.TextField(max_length=1000)
    
    def __str__(self):
        return "<app:id="+str(self.id)+','+\
            self.title+">"