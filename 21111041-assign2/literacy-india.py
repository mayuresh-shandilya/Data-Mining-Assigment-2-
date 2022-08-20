#!/usr/bin/env python
# coding: utf-8

# In[15]:


import csv
import pandas as pd


# In[26]:


dflang=pd.read_excel("DDW-C19-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
edu=dflang.iloc[5:,4].tolist()
sec_lang=dflang.iloc[5:,5].tolist()
third_lang=dflang.iloc[5:,8].tolist()


# In[27]:


dfpop=pd.read_excel("DDW-0000C-08.xlsx")
pcode=dfpop.iloc[6:,1].tolist()
pcat=dfpop.iloc[6:,4].tolist()
page=dfpop.iloc[6:,5].tolist()
illit=dfpop.iloc[6:,9].tolist()
belowpri=dfpop.iloc[6:,18].tolist()
prim=dfpop.iloc[6:,21].tolist()
mid=dfpop.iloc[6:,24].tolist()
mat=dfpop.iloc[6:,27].tolist()
high=dfpop.iloc[6:,30].tolist()
non=dfpop.iloc[6:,33].tolist()
tech=dfpop.iloc[6:,36].tolist()
grad=dfpop.iloc[6:,39].tolist()
matirc=[]
matric = [a + b + c + d for a, b ,c ,d in zip(mat,high,non,tech)]


# In[28]:


state_pop=[]
for i in range(len(pcode)):
    if(pcat[i]=="Total" and page[i]=="All ages"):
        lst=[]
        state_pop.append([pcode[i],"Illiterate",illit[i]])
        state_pop.append([pcode[i],"Literate but below primary",belowpri[i]])
        state_pop.append([pcode[i],"Primary but below middle",prim[i]])
        state_pop.append([pcode[i],"Middle but below matric/secondary",mid[i]])
        state_pop.append([pcode[i],"Matric/Secondary but below graduate",matric[i]])
        state_pop.append([pcode[i],"Graduate and above",grad[i]])


# In[19]:


state_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and edu[i]!="Total" and edu[i]!="Literate"):
        lst=[]
        lst.append(code[i])
        lst.append(edu[i])
        lst.append(third_lang[i])
        state_lang.append(lst)


# In[20]:


fin_lang={}
k=int((len(state_lang))/6)
for i in range(k):
    fin_lang[state_lang[i*6][0]]=[0,0]


# In[23]:


for i in state_lang:
    for j in state_pop:
        if(i[0]==j[0] and i[1]==j[1] and fin_lang[i[0]][1]<(i[2]/j[2])*100 ):
            lst=[]
            lst.append(i[1])
            l=(i[2]/j[2])*100
            lst.append(l)
            fin_lang[i[0]]=lst


# In[57]:


with open('literacy-india.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "literacy-group", "percentage"])
    for i in fin_lang:
        writer.writerow([i,fin_lang[i][0],fin_lang[i][1]]) 


# In[ ]:




