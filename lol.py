import os

f = open('foo.txt','w')
f.write('Hello world!')
f.close()
os.system("notepad.exe foo.txt")