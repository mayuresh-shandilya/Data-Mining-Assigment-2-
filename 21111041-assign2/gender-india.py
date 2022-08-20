#!/usr/bin/env python
# coding: utf-8

# In[132]:


import csv
import pandas as pd
from scipy import stats


# In[133]:


dflang=pd.read_excel("DDW-C18-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
age=dflang.iloc[5:,4].tolist()
fem_sec=dflang.iloc[5:,7].tolist()
fem_third=dflang.iloc[5:,10].tolist()
male_sec=dflang.iloc[5:,6].tolist()
male_third=dflang.iloc[5:,9].tolist()


# In[134]:


state_lang={}
for i in range(len(area)):
    if(area[i]=="Total" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(male_third[i])
        lst.append(fem_third[i])
        state_lang[name[i]]=lst


# In[135]:


popl=pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")
level=popl["Level"].tolist()
lname=popl["Name"].tolist()
tot_male=popl["TOT_M"].tolist()
tot_fem=popl["TOT_F"].tolist()
typ=popl["TRU"].tolist()


# In[136]:


state_pop={}
for i in range(len(level)):
    if((level[i]=="STATE" or level[i]=="India" ) and typ[i]=="Total"):
        lst=[]
        lst.append(tot_male[i]) 
        lst.append(tot_fem[i]) 
        state_pop[lname[i]]=lst


# In[137]:


fin_lang=[]
for i in state_pop:
    for j in state_lang:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(state_lang[j][0])
            lst.append((state_lang[j][1]/state_pop[i][0])*100)
            lst.append((state_lang[j][2]/state_pop[i][1])*100)
            fin_lang.append(lst)


# In[138]:


sec_state_lang={}
for i in range(len(area)):
    if(area[i]=="Total" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(male_sec[i]-male_third[i])
        lst.append(fem_sec[i]-fem_third[i])
        sec_state_lang[name[i]]=lst


# In[139]:


sec_fin_lang=[]
for i in state_pop:
    for j in sec_state_lang:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(sec_state_lang[j][0])
            lst.append((sec_state_lang[j][1]/state_pop[i][0])*100)
            lst.append((sec_state_lang[j][2]/state_pop[i][1])*100)
            sec_fin_lang.append(lst)


# In[140]:


fst_state_lang={}
for i in range(len(area)):
    if(area[i]=="Total" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(male_sec[i])
        lst.append(fem_sec[i])
        fst_state_lang[name[i]]=lst


# In[141]:


fst_fin_lang=[]
for i in state_pop:
    for j in fst_state_lang:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(fst_state_lang[j][0])
            lst.append(((state_pop[i][0]-fst_state_lang[j][1])/state_pop[i][0])*100)
            lst.append(((state_pop[i][1]-fst_state_lang[j][2])/state_pop[i][1])*100)
            fst_fin_lang.append(lst)


# In[142]:


p_value=[]
for i in fst_state_lang:
    lst=[]
    if(i=="INDIA"):
        lst.append((state_pop["India"][0]-fst_state_lang[i][1])/(state_pop["India"][1]-fst_state_lang[i][2]))
        pp=state_pop["India"][0]/state_pop["India"][1] 
    else:
        lst.append((state_pop[i][0]-fst_state_lang[i][1])/(state_pop[i][1]-fst_state_lang[i][2]))
        pp=state_pop[i][0]/state_pop[i][1] 
    lst.append(sec_state_lang[i][1]/sec_state_lang[i][2])  
    lst.append(state_lang[i][1]/state_lang[i][2])
    var,pval=stats.ttest_1samp(lst,pp)
    p_value.append(pval)


# In[143]:


for i in range(len(fst_fin_lang)):
    fst_fin_lang[i].append(p_value[i])  
    sec_fin_lang[i].append(p_value[i])
    fin_lang[i].append(p_value[i])


# In[147]:


with open('gender-india-a.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code", "male-percentage", "female-percentage" ,"p-value"])
    writer.writerows(fst_fin_lang)


# In[148]:


with open('gender-india-b.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code", "male-percentage", "female-percentage" ,"p-value"])
    writer.writerows(sec_fin_lang)


# In[149]:


with open('gender-india-c.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code", "male-percentage", "female-percentage" ,"p-value"])
    writer.writerows(fin_lang)


# In[ ]:




