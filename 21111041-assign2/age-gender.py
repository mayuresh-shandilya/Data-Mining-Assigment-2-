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
msec_lang=dflang.iloc[5:,6].tolist()
fsec_lang=dflang.iloc[5:,7].tolist()
mthird_lang=dflang.iloc[5:,9].tolist()
fthird_lang=dflang.iloc[5:,10].tolist()


# In[3]:


tstate_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(mthird_lang[i])
        lst.append(fthird_lang[i])
        tstate_lang.append(lst)


# In[4]:


dfpop=pd.read_excel("DDW-0000C-14.xls")
pcode=dfpop.iloc[6:,1].tolist()
page=dfpop.iloc[6:,4].tolist()
mpop=dfpop.iloc[6:,6].tolist()
fpop=dfpop.iloc[6:,7].tolist()


# In[5]:


state_pop=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(0)
        lst.append(0)
        state_pop.append(lst)


# In[6]:


for i in range(len(pcode)):
    for j in state_pop:
        if(pcode[i]==j[0] and page[i]==j[1]):
            j[2]=mpop[i]
            j[3]=fpop[i]
        elif(pcode[i]==j[0] and page[i]!=j[1]):
            if((page[i]=="30-34" or page[i]=="35-39" or page[i]=="40-44" or page[i]=="45-49") and j[1]=="30-49"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]
            if((page[i]=="50-54" or page[i]=="55-59" or page[i]=="60-64" or page[i]=="65-69") and j[1]=="50-69"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]
            if((page[i]=="70-74" or page[i]=="75-79" or page[i]=="80+") and j[1]=="70+"):
                j[2]+=mpop[i]
                j[3]+=fpop[i] 


# In[7]:


tfin_lang={}
for i in tstate_lang:
    tfin_lang[i[0]]=[0,0,0,0]


# In[8]:


for i in tstate_lang:
    for j in state_pop:
        if(i[0]==j[0] and i[1]==j[1] and tfin_lang[i[0]][1]<(i[2]/j[2])):
            tfin_lang[i[0]][0]=i[1]
            k=(i[2]/j[2])
            tfin_lang[i[0]][1]=k 
        if(i[0]==j[0] and i[1]==j[1] and tfin_lang[i[0]][3]<(i[3]/j[3]) ):
            tfin_lang[i[0]][2]=i[1]
            k=(i[3]/j[3])
            tfin_lang[i[0]][3]=k 


# In[9]:


with open('age-gender-a.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "age-group-males", "ratio-males", "age-group-females", "ratio-females"])
    for i in tfin_lang:
        writer.writerow([i,tfin_lang[i][0],tfin_lang[i][1],tfin_lang[i][2],tfin_lang[i][3]])  


# In[10]:


sstate_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(msec_lang[i]-mthird_lang[i])
        lst.append(fsec_lang[i]-fthird_lang[i])
        sstate_lang.append(lst)


# In[11]:


sstate_pop=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(0)
        lst.append(0)
        sstate_pop.append(lst)


# In[12]:


for i in range(len(pcode)):
    for j in sstate_pop:
        if(pcode[i]==j[0] and page[i]==j[1]):
            j[2]=mpop[i]
            j[3]=fpop[i]
        elif(pcode[i]==j[0] and page[i]!=j[1]):
            if((page[i]=="30-34" or page[i]=="35-39" or page[i]=="40-44" or page[i]=="45-49") and j[1]=="30-49"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]
            if((page[i]=="50-54" or page[i]=="55-59" or page[i]=="60-64" or page[i]=="65-69") and j[1]=="50-69"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]
            if((page[i]=="70-74" or page[i]=="75-79" or page[i]=="80+") and j[1]=="70+"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]


# In[13]:


sfin_lang={}
for i in sstate_lang:
    sfin_lang[i[0]]=[0,0,0,0]


# In[14]:


for i in sstate_lang:
    for j in sstate_pop:
        if(i[0]==j[0] and i[1]==j[1] and sfin_lang[i[0]][1]<(i[2]/j[2])):
            sfin_lang[i[0]][0]=i[1]
            k=(i[2]/j[2])
            sfin_lang[i[0]][1]=k 
        if(i[0]==j[0] and i[1]==j[1] and sfin_lang[i[0]][3]<(i[3]/j[3]) ):
            sfin_lang[i[0]][2]=i[1]
            k=(i[3]/j[3])
            sfin_lang[i[0]][3]=k            


# In[15]:


with open('age-gender-b.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "age-group-males", "ratio-males", "age-group-females", "ratio-females"])
    for i in sfin_lang:
        writer.writerow([i,sfin_lang[i][0],sfin_lang[i][1],sfin_lang[i][2],sfin_lang[i][3]])  


# In[16]:


fstate_pop=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(0)
        lst.append(0)
        fstate_pop.append(lst)


# In[17]:


for i in range(len(pcode)):
    for j in fstate_pop:
        if(pcode[i]==j[0] and page[i]==j[1]):
            j[2]=mpop[i]
            j[3]=fpop[i]
        elif(pcode[i]==j[0] and page[i]!=j[1]):
            if((page[i]=="30-34" or page[i]=="35-39" or page[i]=="40-44" or page[i]=="45-49") and j[1]=="30-49"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]
            if((page[i]=="50-54" or page[i]=="55-59" or page[i]=="60-64" or page[i]=="65-69") and j[1]=="50-69"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]
            if((page[i]=="70-74" or page[i]=="75-79" or page[i]=="80+") and j[1]=="70+"):
                j[2]+=mpop[i]
                j[3]+=fpop[i]


# In[18]:


mlen=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        mlen.append(msec_lang[i])
mlang=[]
for i in range(len(mlen)):
    mlang.append(fstate_pop[i][2]-mlen[i])
        
flen=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        flen.append(fsec_lang[i])
        
flang=[]
for i in range(len(flen)):
    flang.append(fstate_pop[i][3]-flen[i])


# In[19]:


fstate_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and age[i]!="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(age[i])
        lst.append(0)
        lst.append(0)
        fstate_lang.append(lst)


# In[20]:


for i in range(len(fstate_lang)):
    fstate_lang[i][2]=mlang[i]
    fstate_lang[i][3]=flang[i] 


# In[21]:


ffin_lang={}
for i in fstate_lang:
    ffin_lang[i[0]]=[0,0,0,0]


# In[22]:


for i in fstate_lang:
    for j in fstate_pop:
        if(i[0]==j[0] and i[1]==j[1] and ffin_lang[i[0]][1]<(i[2]/j[2])):
            ffin_lang[i[0]][0]=i[1]
            k=(i[2]/j[2])
            ffin_lang[i[0]][1]=k 
        if(i[0]==j[0] and i[1]==j[1] and ffin_lang[i[0]][3]<(i[3]/j[3]) ):
            ffin_lang[i[0]][2]=i[1]
            k=(i[3]/j[3])
            ffin_lang[i[0]][3]=k 


# In[23]:


with open('age-gender-c.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "age-group-males", "ratio-males", "age-group-females", "ratio-females"])
    for i in ffin_lang:
        writer.writerow([i,ffin_lang[i][0],ffin_lang[i][1],ffin_lang[i][2],ffin_lang[i][3]]) 


# In[ ]:




