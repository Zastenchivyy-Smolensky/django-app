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

class Message(models.Model):
    apps=models.ForeignKey(Apps,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "<Message:id="+str(self.id)+","+\
            self.title+"("+str(self.pub_date)+")>"
    class Meta:
        ordering=('pub_date',)
