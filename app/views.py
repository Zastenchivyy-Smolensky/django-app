from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .models import Apps
from .forms import AppForm,AppsForm
def top(request):
    params={
        "title":"制作アプリ"
    }
    return render(request,"app/top.html",params)

def about(request):
    params={
        "title":"制作物アプリ詳細ページ",
        "p":"このアプリは学生が作ったアプリやサイトを公開するページとなっています"
    }
    return render(request,"app/about.html",params)

def signup(request):
    params={
        "title":"ユーザー登録ページ",
    }
    return render(request,"app.signup",params)

def login(request):
    params={
        "title":"ログインページ",
    }
    return render(request,"app/login",params)

def index(request):
    
    params={
        "title":"一覧ページ",
        "form":AppForm(),
        "data":[],
    }
    if(request.method=="POST"):
        tmp=request.POST["title"]
        item=Apps.objects.get(title=tmp)
        params["data"]=[item]
        params["form"]=AppForm(request.POST)
    else:
        params["data"]=Apps.objects.all()
    return render(request,"app/index.html",params)

def add(request):
    params={
        "title":"投稿画面",
        "form":AppsForm
    }
    if(request.method=="POST"):
        file=request.POST["file"]
        title=request.POST["title"]
        giturl=request.POST["giturl"]
        link=request.POST["link"]
        tech=request.POST["tech"]
        content=request.POST["content"]
        a1=request.POST["a1"]
        
        apps=Apps(file=file,title=title,giturl=giturl,link=link,tech=tech,\
            content=content,a1=a1)
        apps.save()
        messages.success(request,title+"を追加しました")
        return redirect(to="/app/index")
    
    
    return render(request,"app/add.html",params)