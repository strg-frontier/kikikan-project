from django.shortcuts import render,redirect
from .models import Message_bord

def myapp_index(request):
  msg = request.GET.get('words')
  if msg is None:
    data_list = Message_bord.objects.all()
    
    contexts = {
      'result_list': data_list,
    }

    return render(request,'myapp/index.html',contexts)
  else: 
    message_data = Message_bord()
    message_data.new_message = msg

    message_data.save()

    data_list = Message_bord.objects.all()
    contexts = {
      'result_list': data_list,
    }
    return render(request,'myapp/index.html',contexts)
# Create your views here.
