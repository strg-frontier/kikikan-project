from django.shortcuts import render
from django.http import HttpResponse
from .models import Add_Word
from django.template import loader

# Create your views here.

def helloworld_index(request):
    data_list = Add_Word.objects.all()
    context = {
        'lists':data_list,
    }

    return render(request,'helloworld/index.html',context)
