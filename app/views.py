from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params={
        "title":"制作アプリ"
    }
    return render(request,"app/index.html",params)

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