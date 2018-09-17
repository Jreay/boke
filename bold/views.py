from django.shortcuts import render
from . import models

# Create your views here.
def indexView(request):
    articles = models.Article.objects.all()
    print(articles)
    return render(request,'index.html',{'articles':articles})

def getContent(request,id):
    pass
    article = models.Article.objects.get(pk=id)
    return render(request,'article_content.html',{'article':article})

def addBoke(request,id):
    print(id)
    if id=='0':
        print('新增')
        return render(request,'article_edit_add.html',{'article':''})
    else:
        print('修改')
        article = models.Article.objects.get(pk=id)
        print(article)
        return render(request,'article_edit_add.html',{'article':article})

def submitBoke(request):
    print('啦啦啦啦')
    title = request.POST.get('title','默认标题')
    content = request.POST.get('content','默认内容')
    article_id = request.POST.get('article_id','0')

    if str(article_id) == '0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request,'index.html',{'articles':articles})
    else:
        articles = models.Article.objects.get(pk=article_id)
        articles.title = title
        articles.content = content
        articles.save()
        return render(request,'article_content.html',{'article':articles})