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
    share_id=models.IntegerField(default=-1)
    good_count=models.IntegerField(default=0)
    share_count=models.IntegerField(default=0)
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "<Message:id="+str(self.id)+","+\
            self.title+"("+str(self.pub_date)+")>"
    def get_share(self):
        return Message.objects.get(id=self.share_id)
    class Meta:
        ordering=('pub_date',)

class User(models.Model):
    user=models.CharField(max_length=100)
    mail=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return "user.id="+str(self.id)+","+\
            self.user+"(password):"+str(self.password)

class Good(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,\
        related_name="good_user")
    message=models.ForeignKey(Message,on_delete=models.CASCADE)
    
    def __str__(self):
        return 'good for"'+str(self.message)+'"(by'+\
            str(self.user)+')'