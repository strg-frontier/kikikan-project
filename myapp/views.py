from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from .models import Message_bord
from mysite.parser import *


@login_required
def myapp_index(request):
  user_id = request.user.id
  user = User.objects.get(id=user_id)
  user_name = user.get_username()
  print(user_name)
  msg = request.GET.get('words')

  #文字列が入力されていなければ、現在のDB情報の取得のみ
  if msg is None:
    data_list = Message_bord.objects.all()
    
    contexts = {
      'result_list': data_list,
      'user_name': user_name,
    }

    return render(request,'myapp/index.html',contexts)

  else: 
    
    #入力された文字列をパーサーにかける。
    #返り値がFalseであれば、現在のDB情報の取得のみ
    if parser_text(msg):
      message_data = Message_bord()
      message_data.new_message = msg

      message_data.save()

      data_list = Message_bord.objects.all()
      contexts = {
        'result_list': data_list,
        'user_name': user_name,
      }
      return render(request,'myapp/index.html',contexts)

    else:
      data_list = Message_bord.objects.all()

      contexts = {
        'result_list': data_list,
        'user_name': user_name,
      }
      return render(request,'myapp/index.html',contexts)

