from django.contrib import admin
from .models import Apps,Message,User,Good

admin.site.register(Apps)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Good)