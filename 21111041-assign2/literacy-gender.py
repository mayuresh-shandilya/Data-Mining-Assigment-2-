#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd


# In[2]:


dflang=pd.read_excel("DDW-C19-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
edu=dflang.iloc[5:,4].tolist()
msec_lang=dflang.iloc[5:,6].tolist()
mthird_lang=dflang.iloc[5:,9].tolist()
fsec_lang=dflang.iloc[5:,7].tolist()
fthird_lang=dflang.iloc[5:,10].tolist()


# In[3]:


dfpop=pd.read_excel("DDW-0000C-08.xlsx")
pcode=dfpop.iloc[6:,1].tolist()
pcat=dfpop.iloc[6:,4].tolist()
page=dfpop.iloc[6:,5].tolist()
malepop=dfpop.iloc[6:,7].tolist()
fempop=dfpop.iloc[6:,8].tolist()
millit=dfpop.iloc[6:,10].tolist()
mbelowpri=dfpop.iloc[6:,19].tolist()
mprim=dfpop.iloc[6:,22].tolist()
mmid=dfpop.iloc[6:,25].tolist()
mmat=dfpop.iloc[6:,28].tolist()
mhigh=dfpop.iloc[6:,31].tolist()
mnon=dfpop.iloc[6:,34].tolist()
mtech=dfpop.iloc[6:,37].tolist()
mgrad=dfpop.iloc[6:,40].tolist()
mmatirc=[]
mmatric = [a + b + c + d for a, b ,c ,d in zip(mmat,mhigh,mnon,mtech)]
fillit=dfpop.iloc[6:,11].tolist()
fbelowpri=dfpop.iloc[6:,20].tolist()
fprim=dfpop.iloc[6:,23].tolist()
fmid=dfpop.iloc[6:,26].tolist()
fmat=dfpop.iloc[6:,29].tolist()
fhigh=dfpop.iloc[6:,32].tolist()
fnon=dfpop.iloc[6:,35].tolist()
ftech=dfpop.iloc[6:,38].tolist()
fgrad=dfpop.iloc[6:,41].tolist()
fmatirc=[]
fmatric = [a + b + c + d for a, b ,c ,d in zip(fmat,fhigh,fnon,ftech)]


# In[4]:


state_pop=[]
for i in range(len(pcode)):
    if(pcat[i]=="Total" and page[i]=="All ages"):
        lst=[]
        state_pop.append([pcode[i],"Illiterate",millit[i],fillit[i]])
        state_pop.append([pcode[i],"Literate but below primary",mbelowpri[i],fbelowpri[i]])
        state_pop.append([pcode[i],"Primary but below middle",mprim[i],fprim[i]])
        state_pop.append([pcode[i],"Middle but below matric/secondary",mmid[i],fmid[i]])
        state_pop.append([pcode[i],"Matric/Secondary but below graduate",mmatric[i],fmatric[i]])
        state_pop.append([pcode[i],"Graduate and above",mgrad[i],fgrad[i]])


# In[5]:


state_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and edu[i]!="Total" and edu[i]!="Literate"):
        lst=[]
        lst.append(code[i])
        lst.append(edu[i])
        lst.append(mthird_lang[i])
        lst.append(fthird_lang[i])
        state_lang.append(lst)


# In[6]:


fin_lang={}
k=int((len(state_lang))/6)
for i in range(k):
    fin_lang[state_lang[i*6][0]]=[0,0,0,0]


# In[7]:


for i in state_lang:
    for j in state_pop:
        if(i[0]==j[0] and i[1]==j[1] and fin_lang[i[0]][1]<(i[2]/j[2]) ):
            fin_lang[i[0]][0]=i[1]
            l=(i[2]/j[2])
            fin_lang[i[0]][1]=l
        if(i[0]==j[0] and i[1]==j[1] and fin_lang[i[0]][3]<(i[3]/j[3]) ):
            fin_lang[i[0]][2]=i[1]
            l=(i[3]/j[3])
            fin_lang[i[0]][3]=l


# In[8]:


with open('literacy-gender-a.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "literacy-group-males", "ratio-males", "literacy-group-females", "ratio-females"])
    for i in fin_lang:
        writer.writerow([i,fin_lang[i][0],fin_lang[i][1],fin_lang[i][2],fin_lang[i][3]]) 


# In[9]:


sec_state_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and edu[i]!="Total" and edu[i]!="Literate"):
        lst=[]
        lst.append(code[i])
        lst.append(edu[i])
        lst.append(msec_lang[i]-mthird_lang[i])
        lst.append(fsec_lang[i]-fthird_lang[i])
        sec_state_lang.append(lst)


# In[10]:


sec_fin_lang={}
k=int((len(sec_state_lang))/6)
for i in range(k):
    sec_fin_lang[sec_state_lang[i*6][0]]=[0,0,0,0]


# In[11]:


for i in sec_state_lang:
    for j in state_pop:
        if(i[0]==j[0] and i[1]==j[1] and sec_fin_lang[i[0]][1]<(i[2]/j[2]) ):
            sec_fin_lang[i[0]][0]=i[1]
            l=(i[2]/j[2])
            sec_fin_lang[i[0]][1]=l
        if(i[0]==j[0] and i[1]==j[1] and sec_fin_lang[i[0]][3]<(i[3]/j[3]) ):
            sec_fin_lang[i[0]][2]=i[1]
            l=(i[3]/j[3])
            sec_fin_lang[i[0]][3]=l


# In[12]:


with open('literacy-gender-b.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "literacy-group-males", "ratio-males", "literacy-group-females", "ratio-females"])
    for i in sec_fin_lang:
        writer.writerow([i,sec_fin_lang[i][0],sec_fin_lang[i][1],sec_fin_lang[i][2],sec_fin_lang[i][3]]) 


# In[13]:


fst_state_lang=[]
for i in range(len(area)):
    if(area[i]=="Total" and edu[i]!="Total" and edu[i]!="Literate"):
        lst=[]
        lst.append(code[i])
        lst.append(edu[i])
        lst.append(msec_lang[i])
        lst.append(fsec_lang[i])
        fst_state_lang.append(lst)


# In[14]:


fst_fin_lang={}
k=int((len(fst_state_lang))/6)
for i in range(k):
    fst_fin_lang[fst_state_lang[i*6][0]]=[0,0,0,0]


# In[15]:


for i in fst_state_lang:
    for j in state_pop:
        if(i[0]==j[0] and i[1]==j[1] and fst_fin_lang[i[0]][1]<((j[2]-i[2])/j[2]) ):
            fst_fin_lang[i[0]][0]=i[1]
            l=((j[2]-i[2])/j[2])
            fst_fin_lang[i[0]][1]=l
        if(i[0]==j[0] and i[1]==j[1] and fst_fin_lang[i[0]][3]<((j[3]-i[3])/j[3])):
            fst_fin_lang[i[0]][2]=i[1]
            l=((j[3]-i[3])/j[3])
            fst_fin_lang[i[0]][3]=l


# In[16]:


with open('literacy-gender-c.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state/ut", "literacy-group-males", "ratio-males", "literacy-group-females", "ratio-females"])
    for i in fst_fin_lang:
        writer.writerow([i,fst_fin_lang[i][0],fst_fin_lang[i][1],fst_fin_lang[i][2],fst_fin_lang[i][3]]) 


# In[ ]:




