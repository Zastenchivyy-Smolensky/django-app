from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from.models import Apps
from .forms import AppForm
from .forms import AppsForm
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
    
    if(request.method=="POST"):
        obj=AppsForm()
        appform=AppsForm(request.POST,instance=obj)
        appform.save()
        
        return redirect(to="/app/index")
    messages.success(request,+"追加しました")
    params={
        "title":"投稿画面",
        "form":AppsForm()
    }
    
    
    return render(request,"app/add.html",params)

def edit(request,num):
    obj=Apps.objects.get(id=num)
    if (request.method == "POST"):
        apps=AppsForm(request.POST,instance=obj)
        apps.save()
        return redirect(to="/app/index")
    messages.success(request,"プロダクトを編集しました")
    params={
        "title":"編集画面",
        "id":num,
        "form": AppsForm(instance=obj),
    }
    return render(request, "app/edit.html" ,params)
    