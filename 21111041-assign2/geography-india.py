#!/usr/bin/env python
# coding: utf-8

# In[36]:


import csv
import pandas as pd
from scipy import stats


# In[37]:


dflang=pd.read_excel("DDW-C18-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
age=dflang.iloc[5:,4].tolist()
sec_lang=dflang.iloc[5:,5].tolist()
third_lang=dflang.iloc[5:,8].tolist()


# In[38]:


urban_lang={}
for i in range(len(area)):
    if(area[i]=="Urban" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(third_lang[i])
        urban_lang[name[i]]=lst
        
rural_lang={}
for i in range(len(area)):
    if(area[i]=="Rural" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(third_lang[i])
        rural_lang[name[i]]=lst


# In[39]:


popl=pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")
level=popl["Level"].tolist()
lname=popl["Name"].tolist()
tot_pop=popl["TOT_P"].tolist()
typ=popl["TRU"].tolist()


# In[40]:


urban_pop={}
for i in range(len(level)):
    if((level[i]=="STATE" or level[i]=="India" ) and typ[i]=="Urban"):
        urban_pop[lname[i]]=tot_pop[i]

rural_pop={}
for i in range(len(level)):
    if((level[i]=="STATE" or level[i]=="India" ) and typ[i]=="Rural"):
        rural_pop[lname[i]]=tot_pop[i]


# In[41]:


fin_lang=[]
for i in urban_pop:
    for j in urban_lang:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(urban_lang[j][0])
            lst.append((urban_lang[j][1]/urban_pop[i])*100)
            lst.append((rural_lang[j][1]/rural_pop[i])*100)
            fin_lang.append(lst)


# In[42]:


sec_urban_lang={}
for i in range(len(area)):
    if(area[i]=="Urban" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(sec_lang[i]-third_lang[i])
        sec_urban_lang[name[i]]=lst
        
sec_rural_lang={}
for i in range(len(area)):
    if(area[i]=="Rural" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(sec_lang[i]-third_lang[i])
        sec_rural_lang[name[i]]=lst


# In[43]:


sec_fin_lang=[]
for i in urban_pop:
    for j in sec_urban_lang:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(sec_urban_lang[j][0])
            lst.append((sec_urban_lang[j][1]/urban_pop[i])*100)
            lst.append((sec_rural_lang[j][1]/rural_pop[i])*100)
            sec_fin_lang.append(lst)


# In[44]:


fst_urban_lang={}
for i in range(len(area)):
    if(area[i]=="Urban" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(sec_lang[i])
        fst_urban_lang[name[i]]=lst
        
fst_rural_lang={}
for i in range(len(area)):
    if(area[i]=="Rural" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(sec_lang[i])
        fst_rural_lang[name[i]]=lst


# In[45]:


fst_fin_lang=[]
for i in urban_pop:
    for j in fst_urban_lang:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(sec_urban_lang[j][0])
            lst.append(((urban_pop[i]-fst_urban_lang[j][1])/urban_pop[i])*100)
            lst.append(((rural_pop[i]-fst_rural_lang[j][1])/rural_pop[i])*100)
            fst_fin_lang.append(lst)


# In[46]:


p_value=[]
for i in fst_urban_lang:
    lst=[]
    if(i=="INDIA"):
        lst.append((urban_pop["India"]-fst_urban_lang[i][1])/(rural_pop["India"]-fst_rural_lang[i][1]))
        pp=urban_pop["India"]/rural_pop["India"]
    else:
        lst.append((urban_pop[i]-fst_urban_lang[i][1])/(rural_pop[i]-fst_rural_lang[i][1]))
        pp=urban_pop[i]/rural_pop[i]
    lst.append(sec_urban_lang[i][1]/sec_rural_lang[i][1])  
    lst.append(urban_lang[i][1]/rural_lang[i][1])
    var,pval=stats.ttest_1samp(lst,pp)
    p_value.append(pval)


# In[47]:


for i in range(len(fst_fin_lang)):
    fst_fin_lang[i].append(p_value[i])  
    sec_fin_lang[i].append(p_value[i])
    fin_lang[i].append(p_value[i])


# In[48]:


with open('geography-india-a.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code", "urban-percentage", "rural-percentage" ,"p-value"])
    writer.writerows(fst_fin_lang)


# In[49]:


with open('geography-india-b.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code", "urban-percentage", "rural-percentage" ,"p-value"])
    writer.writerows(sec_fin_lang)


# In[50]:


with open('geography-india-c.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code", "urban-percentage", "rural-percentage" ,"p-value"])
    writer.writerows(fin_lang)


# In[ ]:




