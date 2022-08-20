#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd


# In[2]:


dflang=pd.read_excel("DDW-C18-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
age=dflang.iloc[5:,4].tolist()
sec_lang=dflang.iloc[5:,5].tolist()
third_lang=dflang.iloc[5:,8].tolist()


# In[3]:


state_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(third_lang[i])
        state_lang.append(lst)


# In[4]:


dfpop=pd.read_excel("DDW-0000C-14.xls")
pcode=dfpop.iloc[6:,1].tolist()
page=dfpop.iloc[6:,4].tolist()
ppop=dfpop.iloc[6:,5].tolist()


# In[5]:


state_pop=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(0)
        state_pop.append(lst)
for i in range(len(pcode)):
    for j in state_pop:
        if(pcode[i]==j[0] and page[i]==j[1]):
            j[2]=ppop[i]
        elif(pcode[i]==j[0] and page[i]!=j[1]):
            if((page[i]=="30-34" or page[i]=="35-39" or page[i]=="40-44" or page[i]=="45-49") and j[1]=="30-49"):
                j[2]+=ppop[i]
            if((page[i]=="50-54" or page[i]=="55-59" or page[i]=="60-64" or page[i]=="65-69") and j[1]=="50-69"):
                j[2]+=ppop[i]
            if((page[i]=="70-74" or page[i]=="75-79" or page[i]=="80+") and j[1]=="70+"):
                j[2]+=ppop[i]           


# In[6]:


fin_lang={}
for i in state_lang:
    fin_lang[i[0]]=[0,0]


# In[8]:


for i in state_lang:
    for j in state_pop:
        if(i[0]==j[0] and i[1]==j[1] and fin_lang[i[0]][1]<(i[2]/j[2])*100 ):
            lst=[]
            lst.append(i[1])
            k=(i[2]/j[2])*100
            lst.append(k)
            fin_lang[i[0]]=lst 


# In[40]:


with open('age-india.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "age-group", "percentage"])
    for i in fin_lang:
        writer.writerow([i,fin_lang[i][0],fin_lang[i][1]])       


# In[ ]:




