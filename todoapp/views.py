from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django_ratelimit.decorators import ratelimit
from django.http import HttpResponseForbidden


# Create your views here.
@ratelimit(key='ip', rate='5/m', block=True)
def index(request):
    return render(request,'index.html')

@ratelimit(key='ip', rate='5/m', block=True)
def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.status = request.GET['status']
    obj.endDate = datetime.strptime(request.GET['endDate'], '%d-%m-%Y')
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def sortdata(request):
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-priority')
    }
    return render(request,'list.html',context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def sortdataDate(request):
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-endDate')
    }
    return render(request,'list.html',context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def filterDataIncomplete(request):
    mydictionary ={
        "alltodos" : Todo.objects.filter(status=0)
    }
    return render(request, 'list.html', context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def filterDataComplete(request):
    mydictionary ={
        "alltodos" : Todo.objects.filter(status=1)
    }
    return render(request, 'list.html', context=mydictionary)


@ratelimit(key='ip', rate='5/m', block=True)
def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(title__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

@ratelimit(key='ip', rate='5/m', block=True)
def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "endDate":obj.endDate,
        "status":obj.status,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydictionary)


@ratelimit(key='ip', rate='5/m', block=True)
def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.status = request.GET['status']
    obj.endDate = datetime.strptime(request.GET['endDate'], '%d-%m-%Y')
    # import datetime
    updated_at = datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)


def rate_limit_exceeded(request, exception):
    return HttpResponseForbidden("Rate limit exceeded. Please try again after some time.")