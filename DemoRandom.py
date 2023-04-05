# DemoRandom.py 
import random

print( random.random() )
print( random.random() )
print( random.uniform(1.0, 5.0) )
print("---randrange()---")
print( [random.randrange(20) for i in range(10)] )
print( [random.randrange(20) for i in range(10)] )
print("---sample()---")
print( random.sample(range(20), 10) )
print( random.sample(range(20), 10) )

lotto = list(range(1,46))
random.shuffle(lotto)
print( lotto[:5] )

from os.path import * 

print("---파일정보---")
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))
print("파일이 있음:{0}".format(exists("c:\\python310\\python.exe")))
print(getsize("c:\\python310\\python.exe"))

#운영체제의 정보 
import os 
print("운영체제이름:{0}".format(os.name))
#os.system("notepad.exe")

import glob 
print( "현재폴더:{0}".format(os.getcwd()) )
os.chdir("..")
os.chdir("c:\\work")
result = glob.glob("*.py")
for item in result:
    print(item)
    
