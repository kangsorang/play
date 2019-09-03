import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), ".."))
from somepackage import *
import json

def checkSpec(model = "", platform = ""):
    print("model : " + model)
    print("platform : " + platform)
'''
checkSpec()
checkSpec("SM5D", "3.2")
'''
print("Start")
mm = "SM5D"
with open('./model.json') as f:
  data = json.load(f)
  print(repr(data))
  print(data[mm])
  for item in data[mm] :
      print(">> " + item)

