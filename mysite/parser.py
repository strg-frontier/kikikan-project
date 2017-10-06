import os
import re

def parser_text(msg):
  #入力されて文字列が15文字以上であれば、Flaseを返す
  if count_text(msg) and  reg_text(msg):
    return True
  else:
    return False

def count_text(msg):
  print("count start") 
  print(len(msg))
  if len(msg) < 15 and len(msg) >7:
    print("count OK")
    return True
  else:
    return False 


def reg_text(msg):
  print("reg start")
  m = re.match(r"Hello[0-9]+",msg)
  if m:
    print("reg OK")
    return True
  else:
    return False
