from nltk.util import ngrams
from collections import OrderedDict
import re
n = 0
i = 0
l = 0
data = {}
gram = []
frequence = []

file =  open("Apple.txt","r",encoding='UTF-8')
n = input("ngram  n=")

def ngram(n):
 global i   
 while  True:
     line = file.readline()
     if line == '':
         break
     else:
         i +=1
     lis = re.findall("[a-z]+",line.lower())
     ingrams = ngrams(lis,int(n))
     for  grams in ingrams:
        #print (grams)
        if grams in data:
          data[grams][0] +=1
          data[grams].append(i)
         
        else:
         data[grams]=[1, i]
        
 file.close()
 revise = OrderedDict(sorted(data.items(), key=lambda t: t[1],reverse=True))
 print("切割結果\n")
 print(revise)
 test = revise.items()
 for d in test:
     gram.append(d[0])
     frequence.append(d[1])
 print("\nTop 5 Sequence")
 for i in range(6):
  print(str(gram[i])+"  [次數,出現行數]為"+str(frequence[i]))
#print(revise[0])
ngram(n)
        
      
