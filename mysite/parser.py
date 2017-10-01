

import os

def parser_text(msg):
  #入力されて文字列が15文字以上であれば、Flaseを返す
  if len(msg) < 15:
    return True
  else:
    return False