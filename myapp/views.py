from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from weight.views import *
#from friend.views import *


#トップ画面
@login_required
def index(request):
  user_id = request.user.id
  user = User.objects.get(id=user_id)
  user_name = user.get_username()
  print(user_name)
  msg = request.POST.get('words')
  

  #体重情報取得
  user_weight = get_weight(request)


  #フレンド情報取得
  #friend_list = get_friend_list(request)
  
  context = {
    'login_user':user_name,
    'user_weight':user_weight,
    #'friend_list':friend_list,
  }
  return render(request,'myapp/index.html',context)

