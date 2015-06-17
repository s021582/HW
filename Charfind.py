#使用python2版本，用cmd移到python的Script資料夾  , 然後打指令:pip install nltk
#-*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import *
import sys, os.path
from cStringIO import StringIO
from nltk.util import ngrams
from collections import OrderedDict
import re


text=""
keyresult = []
result = []
time=0
key=""
key_time = ""
buff=""
sbuff=""

correct=[]

def load_file():
    global text,buff

    text = fopen()
    
    buff.set("已讀取檔案, 請輸入想搜尋的字")
    


def click(t):

    global result,time,keyresult,key,key_time      
    buff.set("")
    sbuff.set("")

    ftext = StringIO(text)
    
    
    if(t!=''):
     result = ngram(ftext,t,1)

     if len(result)==0:
        spell(t)
        
     elif len(result)>0:   

      ftext = StringIO(text) 
      keyresult = ngram(ftext,t,2)
      time = result.items()[0][1][0]
      print(result)#test
      print(keyresult)#test

      key = keyresult.items()[0][0][1]
      key_time = str(keyresult.items()[0][1][0])
      
      buff.set("查詢的單字為"+e.get()+"   文章中出現次數: "+str(time)+"\n 後面出現次數最多單字"+key+"  出現次數: "+key_time)
     
      

def fopen():
 filename = askopenfilename() 
 file = open(filename)#開檔
 return file.read()

def ngram(f, word,n):
  i=0
  r=0
  data = {}
  
  for line in f:
     if line == '':
         break
     else:
         i +=1
     lis = re.findall("[a-z]+",line.lower())
     ingrams = ngrams(lis,int(n))
  
     for  grams in ingrams:
       if (grams[0]==word.lower()):
        if grams in data:
          data[grams][0] +=1
          data[grams].append(i)
        else:
         data[grams]=[1, i]

    
  revise = OrderedDict(sorted(data.items(), key=lambda t: t[1],reverse=True))
 
  return revise

def spell(t):
    global correct
    ftext = StringIO(text)
    correct = check(ftext,t)
    ct = "沒有您輸入的字, 是否改為收尋"
    
    for i in range(len(correct)):
      ct += "\n"+correct[i]
    sbuff.set(ct)
    

def check(f, word):
  
  correct = []
  for line in f:
     if line == '':
         break

     lis = re.findall("[a-z]+",line.lower())
     ingrams = ngrams(lis,int(1))
  
     for  grams in ingrams:
       if (grams[0].find(word.lower())>=0):
           if(grams[0] in correct)==False:
            print(grams[0].find(word.lower()))#test
            correct.append(grams[0])
          
  return correct



     
#創視窗 
root = Tk()

m0 = Menu(root);
root.configure(menu = m0);

m1 = Menu(m0, tearoff = 0)
m0.add_cascade(label = 'File', under = 0, menu = m1 )

m1.add_command(label = 'Open', under = 0, command = load_file)
m1.add_separator
m1.add_command(label = 'Exit', under = 0, command = sys.exit)


button = Button(root, text='Find', command=lambda:click(e.get()))
button.grid(row=0,column=0)


e = Entry(root, textvariable = buffer)
e.grid(row=0,column=1)


buff = StringVar()
buff.set("請先從左上角選擇檔案")
label = Label(root, textvariable = buff)
label.grid(row=1,column=1)


sbuff = StringVar()
sbuff.set("")
slabel = Label(root, textvariable = sbuff)
slabel.grid(row=1,column=0)


root.mainloop()
