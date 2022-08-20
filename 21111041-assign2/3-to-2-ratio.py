#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import pandas as pd


# In[3]:


dflang=pd.read_excel("DDW-C18-0000.xlsx")
code=dflang.iloc[5:,0].tolist()
name=dflang.iloc[5:,2].tolist()
area=dflang.iloc[5:,3].tolist()
age=dflang.iloc[5:,4].tolist()
sec_lang=dflang.iloc[5:,5].tolist()
third_lang=dflang.iloc[5:,8].tolist()


# In[4]:


state_lang={}
for i in range(len(area)):
    if(area[i]=="Total" and age[i]=="Total"):
        lst=[]
        lst.append(code[i])
        lst.append(sec_lang[i])
        lst.append(third_lang[i])
        state_lang[name[i]]=lst


# In[6]:


fin_lst=[]
for i in state_lang:
    if(i!="INDIA"):
        lst=[]
        lst.append(state_lang[i][2]/(state_lang[i][1]-state_lang[i][2]))
        lst.append(state_lang[i][0])
        fin_lst.append(lst)
fin_lst.sort(reverse=True)


# In[7]:


with open('3-to-2-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["State-code"])
    writer.writerow([fin_lst[0][1]])    
    writer.writerow([fin_lst[1][1]])    
    writer.writerow([fin_lst[2][1]])
    writer.writerow([fin_lst[-1][1]])    
    writer.writerow([fin_lst[-2][1]])    
    writer.writerow([fin_lst[-3][1]])    


# In[ ]:





# In[ ]:




