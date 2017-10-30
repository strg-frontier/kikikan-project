#from django.shortcuts import render
from .models import Weight

# Create your views here.
def index():
  pass

def get_weight(request):
  login_user_id = request.user.id
  weight_list = Weight.objects.filter(user_id=login_user_id)

  return weight_list
