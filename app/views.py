from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    QLWO=WebPage.objects.all()
    d={'webpage':QLWO}

    return render(request,'display_webpage.html',d)

def display_acessrecord(request):
    QLAO=AcessRecord.objects.all()
    d={'ar':QLAO}

    return render(request,'display_acessrecord.html',d)

def insert_topic(request):
    tn=input('enter topic name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn=input('enter topic name')
    n=input('enter name')
    u=input('enter url')
    TO=Topic.objects.get(topic_name=tn)
    NTO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NTO.save()
    QLWO=WebPage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def insert_acessrecord(request):
    pk=int(input('enter pk value:'))
    a=input('enter author')
    d=input('enter date')
    AO=WebPage.objects.get(pk=pk)
    ARO=AcessRecord.objects.get_or_create(name=AO,date=d,author=a)[0]
    ARO.save()
    QLAO=AcessRecord.objects.all()
    d={'ar':QLAO}
    return render(request,'display_acessrecord.html',d)



