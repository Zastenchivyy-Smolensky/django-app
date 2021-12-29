from django.db import models

class Apps(models.Model):
    file = models.FileField(upload_to="file/%Y/%m/%d")
    title= models.CharField(max_length=100)
    giturl=models.URLField(max_length=10000)
    link=models.URLField(max_length=10000)
    tech=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    a1=models.CharField(max_length=1000)

    def __str__(self):
        return "<app:id="+str(self.id)+','+\
            self.title+str(self.tech)+">"