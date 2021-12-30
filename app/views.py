from django.core import paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from.models import Apps,Message,User
from .forms import AppForm
from .forms import AppsForm,FindForm,MessageForm,UserForm,GoodForm
from django.views.generic import DetailView
from django.core.paginator import Paginator
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

def index(request,num=1):
    data=Apps.objects.all()
    page=Paginator(data,3)
    params={
        "title":"一覧ページ",
        "data":page.get_page(num),
    }
    
    return render(request,"app/index.html",params)

def add(request):
    
    if(request.method == "POST"):
        file=request.POST["file"]
        title=request.POST["title"]
        giturl=request.POST["giturl"]
        link=request.POST["link"]
        tech=request.POST["tech"]
        content=request.POST["content"]
        a1=request.POST["a1"]
        app=Apps(file=file,title=title,giturl=giturl,link=link,tech=tech,\
            content=content,a1=a1)
        app.save()
        obj=Apps()
        
        return redirect(to="/app/index")
    
    
    messages.success(request,"追加しました")
    params={
        "title":"投稿画面",
        "form":AppForm(),
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

def delete(request,num):
    apps=Apps.objects.get(id=num)
    if(request.method=="POST"):
        apps.delete()
        return redirect(to="/app/index")
    messages.success(request,"プロダクトを削除しました")
    params={
        "title":"削除画面",
        "id":num,
        "obj":apps
    }
    return render(request,"app/delete.html",params)
def find(request):
    if(request.method=="POST"):
        form=FindForm(request.POST)
        find=request.POST["find"]
        data=Apps.objects.filter(title=find)
    else:
        form=FindForm()
        data=Apps.objects.all()
    params={
        "title":"検索ページ",
        "form":form,
        "data":data,
    }
    return render(request,"app/find.html",params)
class AppsDetail(DetailView):
    model=Apps

def message(request,page=1):
    if(request.method=="POST"):
        obj=Message()
        form=MessageForm(request.POST,instance=obj)
        form.save()
    data=Message.objects.all().reverse()
    paginator=Paginator(data,5)
    params={
        "title":"コメント",
        "form":MessageForm(),
        "data":paginator.get_page(page)
    }
    return render(request,"app/message.html",params)

def signup(request):
    params={
        "title":"ユーザー登録",
        "form":UserForm(),
    }
    if (request.method=="POST"):
        user=request.POST["user"]
        mail=request.POST["mail"]
        password=request.POST["password"]
        user=User(user=user,mail=mail,password=password)
        user.save()
        return redirect(to="/app/index")
    
    return render(request,"app/signup.html",params)    
    