#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
import pandas as pd


# In[10]:


dflang=pd.read_excel("DDW-C18-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
age=dflang.iloc[5:,4].tolist()
sec_lang=dflang.iloc[5:,5].tolist()
third_lang=dflang.iloc[5:,8].tolist()


# In[11]:


state_lang={}
for i in range(len(area)):
    if(area[i]=="Total" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(sec_lang[i])
        lst.append(third_lang[i])
        state_lang[name[i]]=lst


# In[12]:


popl=pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")
level=popl["Level"].tolist()
lname=popl["Name"].tolist()
tot_pop=popl["TOT_P"].tolist()
typ=popl["TRU"].tolist()


# In[13]:


state_pop={}
for i in range(len(level)):
    if(level[i]=="STATE" and typ[i]=="Total"):
        state_pop[lname[i]]=tot_pop[i] 
pop_overall=tot_pop[0]


# In[14]:


fin_lang=[]
lst=[]
lst.append(code[0])
lst.append(((pop_overall-sec_lang[0])/pop_overall)*100)

lst.append(((sec_lang[0]-third_lang[0])/pop_overall)*100)

lst.append((third_lang[0]/pop_overall)*100)
fin_lang.append(lst)


# In[15]:


for i in state_pop:
    for j in state_lang:
        if(i==j):
            lst=[]
            lst.append(state_lang[i][0])
            lst.append(((state_pop[i]-state_lang[j][1])/state_pop[i])*100)
            
            lst.append(((state_lang[j][1]-state_lang[j][2])/state_pop[i])*100)
           
            lst.append((state_lang[j][2]/state_pop[i])*100)
            fin_lang.append(lst)


# In[17]:


with open('percent-india.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["state-code", "percent-one", "percent-two", "percent-three"])
    writer.writerows(fin_lang)


# In[ ]:





# In[ ]:




