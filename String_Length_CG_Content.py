# -*- coding: utf-8 -*-
"""


@author: Shujaat
"""
#Funcation to Calculate Pertentage of Alaphats in a String
def pct(str,cou):
    substringG ="G"
    substringC ="C"
    count1 = str.count(substringC)
    count2 = str.count(substringG)
    count=count1+count2
    pct1=(count/cou)*100
    return pct1
pctList=list()      
#Merage differnt line Strings to one String from File              
string2=""
linelist2 = list()
string=""  
lineList = list()
#Get all strings to one strings
with open("rosalind_gc_28_07_2020.txt",'r') as f:
  for line in f:
    lineList.append(line)
for x in range (len(lineList)):
    string+=(lineList[x])
#Separate the strings    
for i in range(len(string)):
    string2+=string[i]
    if(i<(len(string)-1) and string[i+1]=='>'):
       linelist2.append(string2)
       string2=""
linelist2.append(string2)
#Calcuate Nextline in Strings

NextLineCounter=0
for i in range(len(string2)):   
    if(string2[i]=='\n'):
        NextLineCounter+=1 
#Calulate Length of ID
counter=0
for i in range(len(string2)):
    if(string2[i]!='A'and string2[i]!='C' and string2[i]!='G' and string2[i]!='T' and string2[i]!='\n'):        
        counter=counter+1
       
StrLeng=len(string2)-counter-NextLineCounter
#Calcuate pertentage of Alphabet and Return Back to Alpahat index
for i in range(len(linelist2)):
    pctList.append(pct(linelist2[i],StrLeng))
m=(max(pctList))
index=0
for i, j in enumerate(pctList):
    if j == m:
        print("Index is:",i)
        print("Maximum value:",pctList[i])
        index=i
#GetID from index
indexString=(linelist2[index])
indexS=""        
for x in range (counter):
    indexS+=indexString[x]
print(indexS)

       
