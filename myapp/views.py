from django.shortcuts import render,redirect
from .models import Message_bord
from mysite.parser import *

def myapp_index(request):
  msg = request.GET.get('words')

  #文字列が入力されていなければ、現在のDB情報の取得のみ
  if msg is None:
    data_list = Message_bord.objects.all()
    
    contexts = {
      'result_list': data_list,
    }

    return render(request,'myapp/index.html',contexts)

  else: 
    
    #入力された文字列をパーサーにかける。
    #返り値がFalseであれば、現在のDB情報の取得のみ
    if not parser_text(msg):
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
