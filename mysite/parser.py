import os
import re

def parser_text(msg):
  #入力されて文字列が長さ・正規表現の条件に合致していればTrueを返す
  if count_text(msg) and  reg_text(msg):
    return True
  else:
    return False

#入力文字列の長さが8以上14以下であればTrueを返す
def count_text(msg):
  print("count start") 
  print(len(msg))
  if len(msg) > 7 and len(msg) < 15:
    print("count OK")
    return True
  else:
    return False 

#入力文字列がHello+数列であればTrueを返す
def reg_text(msg):
  print("reg start")
  m = re.match(r"Hello[0-9]+",msg)
  if m:
    print("reg OK")
    return True
  else:
    return False
