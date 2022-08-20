#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv 
import pandas as pd


# In[11]:


df=pd.read_excel("DDW-C17-2300.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
mp_lang=df1.lang.to_list()
mp_ppl=df1.ppl.to_list()
mp_seclang=df2.lang.to_list()
mp_secppl=df2.ppl.to_list()
mp_thrlang=df3.lang.to_list()
mp_thrppl=df3.ppl.to_list()
acen_lang={}
bcen_lang={}
for i in range(len(mp_lang)):
    acen_lang[mp_lang[i]]=mp_ppl[i]
for i in range(len(mp_lang)):
    bcen_lang[mp_lang[i]]=mp_ppl[i]
for i in range(len(mp_seclang)):
    if mp_seclang[i] in bcen_lang:
        bcen_lang[mp_seclang[i]]+=mp_secppl[i]
    else:
        bcen_lang[mp_seclang[i]]=mp_secppl[i]
for i in range(len(mp_thrlang)):
    if mp_thrlang[i] in bcen_lang:
        bcen_lang[mp_thrlang[i]]+=mp_thrppl[i]
    else:
        bcen_lang[mp_thrlang[i]]=mp_thrppl[i] 
        
df=pd.read_excel("DDW-C17-0900.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
up_lang=df1.lang.to_list()
up_ppl=df1.ppl.to_list()
up_seclang=df2.lang.to_list()
up_secppl=df2.ppl.to_list()
up_thrlang=df3.lang.to_list()
up_thrppl=df3.ppl.to_list()
for i in range(len(up_lang)):
    if up_lang[i] in acen_lang:
        acen_lang[up_lang[i]]+=up_ppl[i]
    else:
        acen_lang[up_lang[i]]=up_ppl[i]
for i in range(len(up_lang)):
    if up_lang[i] in bcen_lang:
        bcen_lang[up_lang[i]]+=up_ppl[i]
    else:
        bcen_lang[up_lang[i]]=up_ppl[i]
for i in range(len(up_seclang)):
    if up_seclang[i] in bcen_lang:
        bcen_lang[up_seclang[i]]+=up_secppl[i]
    else:
        bcen_lang[up_seclang[i]]=up_secppl[i]
for i in range(len(up_thrlang)):
    if up_thrlang[i] in bcen_lang:
        bcen_lang[up_thrlang[i]]+=up_thrppl[i]
    else:
        bcen_lang[up_thrlang[i]]=up_thrppl[i] 
        
df=pd.read_excel("DDW-C17-2200.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
cg_lang=df1.lang.to_list()
cg_ppl=df1.ppl.to_list()
cg_seclang=df2.lang.to_list()
cg_secppl=df2.ppl.to_list()
cg_thrlang=df3.lang.to_list()
cg_thrppl=df3.ppl.to_list()
for i in range(len(cg_lang)):
    if cg_lang[i] in acen_lang:
        acen_lang[cg_lang[i]]+=cg_ppl[i]
    else:
        acen_lang[cg_lang[i]]=cg_ppl[i]
for i in range(len(cg_lang)):
    if cg_lang[i] in bcen_lang:
        bcen_lang[cg_lang[i]]+=cg_ppl[i]
    else:
        bcen_lang[cg_lang[i]]=cg_ppl[i]
for i in range(len(cg_seclang)):
    if cg_seclang[i] in bcen_lang:
        bcen_lang[cg_seclang[i]]+=cg_secppl[i]
    else:
        bcen_lang[cg_seclang[i]]=cg_secppl[i]
for i in range(len(cg_thrlang)):
    if cg_thrlang[i] in bcen_lang:
        bcen_lang[cg_thrlang[i]]+=cg_thrppl[i]
    else:
        bcen_lang[cg_thrlang[i]]=cg_thrppl[i]
        
acentral=dict(sorted(acen_lang.items(), key=lambda x:x[1], reverse=True))

afin_lst=[]
altt=[]
altt.append("Central")
for x in list(acentral)[0:3]:
    altt.append(x)
afin_lst.append(altt)

bcentral=dict(sorted(bcen_lang.items(), key=lambda x:x[1], reverse=True))

bfin_lst=[]
bltt=[]
bltt.append("Central")
for x in list(bcentral)[0:3]:
    bltt.append(x)
bfin_lst.append(bltt)


# In[12]:


df=pd.read_excel("DDW-C17-1000.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
aeast_lang={}
beast_lang={}
bh_lang=df1.lang.to_list()
bh_ppl=df1.ppl.to_list()
bh_seclang=df2.lang.to_list()
bh_secppl=df2.ppl.to_list()
bh_thrlang=df3.lang.to_list()
bh_thrppl=df3.ppl.to_list()
for i in range(len(bh_lang)):
    if bh_lang[i] in aeast_lang:
        aeast_lang[bh_lang[i]]+=bh_ppl[i]
    else:
        aeast_lang[bh_lang[i]]=bh_ppl[i]
for i in range(len(bh_lang)):
    if bh_lang[i] in beast_lang:
        beast_lang[bh_lang[i]]+=bh_ppl[i]
    else:
        beast_lang[bh_lang[i]]=bh_ppl[i]
for i in range(len(bh_seclang)):
    if bh_seclang[i] in beast_lang:
        beast_lang[bh_seclang[i]]+=bh_secppl[i]
    else:
        beast_lang[bh_seclang[i]]=bh_secppl[i]
for i in range(len(bh_thrlang)):
    if bh_thrlang[i] in beast_lang:
        beast_lang[bh_thrlang[i]]+=bh_thrppl[i]
    else:
        beast_lang[bh_thrlang[i]]=bh_thrppl[i]

df=pd.read_excel("DDW-C17-1900.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
wb_lang=df1.lang.to_list()
wb_ppl=df1.ppl.to_list()
wb_seclang=df2.lang.to_list()
wb_secppl=df2.ppl.to_list()
wb_thrlang=df3.lang.to_list()
wb_thrppl=df3.ppl.to_list()
for i in range(len(wb_lang)):
    if wb_lang[i] in aeast_lang:
        aeast_lang[wb_lang[i]]+=wb_ppl[i]
    else:
        aeast_lang[wb_lang[i]]=wb_ppl[i]
for i in range(len(wb_lang)):
    if wb_lang[i] in beast_lang:
        beast_lang[wb_lang[i]]+=wb_ppl[i]
    else:
        beast_lang[wb_lang[i]]=wb_ppl[i]
for i in range(len(wb_seclang)):
    if wb_seclang[i] in beast_lang:
        beast_lang[wb_seclang[i]]+=wb_secppl[i]
    else:
        beast_lang[wb_seclang[i]]=wb_secppl[i]
for i in range(len(wb_thrlang)):
    if wb_thrlang[i] in beast_lang:
        beast_lang[wb_thrlang[i]]+=wb_thrppl[i]
    else:
        beast_lang[wb_thrlang[i]]=wb_thrppl[i]
        
df=pd.read_excel("DDW-C17-2100.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
or_lang=df1.lang.to_list()
or_ppl=df1.ppl.to_list()
or_seclang=df2.lang.to_list()
or_secppl=df2.ppl.to_list()
or_thrlang=df3.lang.to_list()
or_thrppl=df3.ppl.to_list()
for i in range(len(or_lang)):
    if or_lang[i] in aeast_lang:
        aeast_lang[or_lang[i]]+=or_ppl[i]
    else:
        aeast_lang[or_lang[i]]=or_ppl[i]
for i in range(len(or_lang)):
    if or_lang[i] in beast_lang:
        beast_lang[or_lang[i]]+=or_ppl[i]
    else:
        beast_lang[or_lang[i]]=or_ppl[i]
for i in range(len(or_seclang)):
    if or_seclang[i] in beast_lang:
        beast_lang[or_seclang[i]]+=or_secppl[i]
    else:
        beast_lang[or_seclang[i]]=or_secppl[i]
for i in range(len(or_thrlang)):
    if or_thrlang[i] in beast_lang:
        beast_lang[or_thrlang[i]]+=or_thrppl[i]
    else:
        beast_lang[or_thrlang[i]]=or_thrppl[i]
        
df=pd.read_excel("DDW-C17-2000.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
jh_lang=df1.lang.to_list()
jh_ppl=df1.ppl.to_list()
jh_seclang=df2.lang.to_list()
jh_secppl=df2.ppl.to_list()
jh_thrlang=df3.lang.to_list()
jh_thrppl=df3.ppl.to_list()
for i in range(len(jh_lang)):
    if jh_lang[i] in aeast_lang:
        aeast_lang[jh_lang[i]]+=jh_ppl[i]
    else:
        aeast_lang[jh_lang[i]]=jh_ppl[i]
for i in range(len(jh_lang)):
    if jh_lang[i] in beast_lang:
        beast_lang[jh_lang[i]]+=jh_ppl[i]
    else:
        beast_lang[jh_lang[i]]=jh_ppl[i]
for i in range(len(jh_seclang)):
    if jh_seclang[i] in beast_lang:
        beast_lang[jh_seclang[i]]+=jh_secppl[i]
    else:
        beast_lang[jh_seclang[i]]=jh_secppl[i]
for i in range(len(jh_thrlang)):
    if jh_thrlang[i] in beast_lang:
        beast_lang[jh_thrlang[i]]+=jh_thrppl[i]
    else:
        beast_lang[jh_thrlang[i]]=jh_thrppl[i]
        
aeast=dict(sorted(aeast_lang.items(), key=lambda x:x[1], reverse=True))

altt=[]
altt.append("East")
for x in list(aeast)[0:3]:
    altt.append(x)
afin_lst.append(altt)

beast=dict(sorted(beast_lang.items(), key=lambda x:x[1], reverse=True))

bltt=[]
bltt.append("East")
for x in list(beast)[0:3]:
    bltt.append(x)
bfin_lst.append(bltt)


# In[13]:


df=pd.read_excel("DDW-C17-0100.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
anorth_lang={}
bnorth_lang={}
jk_lang=df1.lang.to_list()
jk_ppl=df1.ppl.to_list()
jk_seclang=df2.lang.to_list()
jk_secppl=df2.ppl.to_list()
jk_thrlang=df3.lang.to_list()
jk_thrppl=df3.ppl.to_list()
for i in range(len(jk_lang)):
    if jk_lang[i] in anorth_lang:
        anorth_lang[jk_lang[i]]+=jk_ppl[i]
    else:
        anorth_lang[jk_lang[i]]=jk_ppl[i]
for i in range(len(jk_lang)):
    if jk_lang[i] in bnorth_lang:
        bnorth_lang[jk_lang[i]]+=jk_ppl[i]
    else:
        bnorth_lang[jk_lang[i]]=jk_ppl[i]
for i in range(len(jk_seclang)):
    if jk_seclang[i] in bnorth_lang:
        bnorth_lang[jk_seclang[i]]+=jk_secppl[i]
    else:
        bnorth_lang[jk_seclang[i]]=jk_secppl[i]
for i in range(len(jk_thrlang)):
    if jk_thrlang[i] in bnorth_lang:
        bnorth_lang[jk_thrlang[i]]+=jk_thrppl[i]
    else:
        bnorth_lang[jk_thrlang[i]]=jk_thrppl[i]
        
df=pd.read_excel("DDW-C17-0300.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
pn_lang=df1.lang.to_list()
pn_ppl=df1.ppl.to_list()
pn_seclang=df2.lang.to_list()
pn_secppl=df2.ppl.to_list()
pn_thrlang=df3.lang.to_list()
pn_thrppl=df3.ppl.to_list()
for i in range(len(pn_lang)):
    if pn_lang[i] in anorth_lang:
        anorth_lang[pn_lang[i]]+=pn_ppl[i]
    else:
        anorth_lang[pn_lang[i]]=pn_ppl[i]
for i in range(len(pn_lang)):
    if pn_lang[i] in bnorth_lang:
        bnorth_lang[pn_lang[i]]+=pn_ppl[i]
    else:
        bnorth_lang[pn_lang[i]]=pn_ppl[i]
for i in range(len(pn_seclang)):
    if pn_seclang[i] in bnorth_lang:
        bnorth_lang[pn_seclang[i]]+=pn_secppl[i]
    else:
        bnorth_lang[pn_seclang[i]]=pn_secppl[i]
for i in range(len(pn_thrlang)):
    if pn_thrlang[i] in bnorth_lang:
        bnorth_lang[pn_thrlang[i]]+=pn_thrppl[i]
    else:
        bnorth_lang[pn_thrlang[i]]=pn_thrppl[i]
        
df=pd.read_excel("DDW-C17-0200.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
hp_lang=df1.lang.to_list()
hp_ppl=df1.ppl.to_list()
hp_seclang=df2.lang.to_list()
hp_secppl=df2.ppl.to_list()
hp_thrlang=df3.lang.to_list()
hp_thrppl=df3.ppl.to_list()
for i in range(len(hp_lang)):
    if hp_lang[i] in anorth_lang:
        anorth_lang[hp_lang[i]]+=hp_ppl[i]
    else:
        anorth_lang[hp_lang[i]]=hp_ppl[i]
for i in range(len(hp_lang)):
    if hp_lang[i] in bnorth_lang:
        bnorth_lang[hp_lang[i]]+=hp_ppl[i]
    else:
        bnorth_lang[hp_lang[i]]=hp_ppl[i]
for i in range(len(hp_seclang)):
    if hp_seclang[i] in bnorth_lang:
        bnorth_lang[hp_seclang[i]]+=hp_secppl[i]
    else:
        bnorth_lang[hp_seclang[i]]=hp_secppl[i]
for i in range(len(hp_thrlang)):
    if hp_thrlang[i] in bnorth_lang:
        bnorth_lang[hp_thrlang[i]]+=hp_thrppl[i]
    else:
        bnorth_lang[hp_thrlang[i]]=hp_thrppl[i]
        
df=pd.read_excel("DDW-C17-0600.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
hr_lang=df1.lang.to_list()
hr_ppl=df1.ppl.to_list()
hr_seclang=df2.lang.to_list()
hr_secppl=df2.ppl.to_list()
hr_thrlang=df3.lang.to_list()
hr_thrppl=df3.ppl.to_list()
for i in range(len(hr_lang)):
    if hr_lang[i] in anorth_lang:
        anorth_lang[hr_lang[i]]+=hr_ppl[i]
    else:
        anorth_lang[hr_lang[i]]=hr_ppl[i]
for i in range(len(hr_lang)):
    if hr_lang[i] in bnorth_lang:
        bnorth_lang[hr_lang[i]]+=hr_ppl[i]
    else:
        bnorth_lang[hr_lang[i]]=hr_ppl[i]
for i in range(len(hr_seclang)):
    if hr_seclang[i] in bnorth_lang:
        bnorth_lang[hr_seclang[i]]+=hr_secppl[i]
    else:
        bnorth_lang[hr_seclang[i]]=hr_secppl[i]
for i in range(len(hr_thrlang)):
    if hr_thrlang[i] in bnorth_lang:
        bnorth_lang[hr_thrlang[i]]+=hr_thrppl[i]
    else:
        bnorth_lang[hr_thrlang[i]]=hr_thrppl[i]
        
df=pd.read_excel("DDW-C17-0500.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
uk_lang=df1.lang.to_list()
uk_ppl=df1.ppl.to_list()
uk_seclang=df2.lang.to_list()
uk_secppl=df2.ppl.to_list()
uk_thrlang=df3.lang.to_list()
uk_thrppl=df3.ppl.to_list()
for i in range(len(uk_lang)):
    if uk_lang[i] in anorth_lang:
        anorth_lang[uk_lang[i]]+=uk_ppl[i]
    else:
        anorth_lang[uk_lang[i]]=uk_ppl[i]
for i in range(len(uk_lang)):
    if uk_lang[i] in bnorth_lang:
        bnorth_lang[uk_lang[i]]+=uk_ppl[i]
    else:
        bnorth_lang[uk_lang[i]]=uk_ppl[i]
for i in range(len(uk_seclang)):
    if uk_seclang[i] in bnorth_lang:
        bnorth_lang[uk_seclang[i]]+=uk_secppl[i]
    else:
        bnorth_lang[uk_seclang[i]]=uk_secppl[i]
for i in range(len(uk_thrlang)):
    if uk_thrlang[i] in bnorth_lang:
        bnorth_lang[uk_thrlang[i]]+=uk_thrppl[i]
    else:
        bnorth_lang[uk_thrlang[i]]=uk_thrppl[i]
        
df=pd.read_excel("DDW-C17-0700.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
dl_lang=df1.lang.to_list()
dl_ppl=df1.ppl.to_list()
dl_seclang=df2.lang.to_list()
dl_secppl=df2.ppl.to_list()
dl_thrlang=df3.lang.to_list()
dl_thrppl=df3.ppl.to_list()
for i in range(len(dl_lang)):
    if dl_lang[i] in anorth_lang:
        anorth_lang[dl_lang[i]]+=dl_ppl[i]
    else:
        anorth_lang[dl_lang[i]]=dl_ppl[i]
for i in range(len(dl_lang)):
    if dl_lang[i] in bnorth_lang:
        bnorth_lang[dl_lang[i]]+=dl_ppl[i]
    else:
        bnorth_lang[dl_lang[i]]=dl_ppl[i]
for i in range(len(dl_seclang)):
    if dl_seclang[i] in bnorth_lang:
        bnorth_lang[dl_seclang[i]]+=dl_secppl[i]
    else:
        bnorth_lang[dl_seclang[i]]=dl_secppl[i]
for i in range(len(dl_thrlang)):
    if dl_thrlang[i] in bnorth_lang:
        bnorth_lang[dl_thrlang[i]]+=dl_thrppl[i]
    else:
        bnorth_lang[dl_thrlang[i]]=dl_thrppl[i]
        
df=pd.read_excel("DDW-C17-0400.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
ch_lang=df1.lang.to_list()
ch_ppl=df1.ppl.to_list()
ch_seclang=df2.lang.to_list()
ch_secppl=df2.ppl.to_list()
ch_thrlang=df3.lang.to_list()
ch_thrppl=df3.ppl.to_list()
for i in range(len(ch_lang)):
    if ch_lang[i] in anorth_lang:
        anorth_lang[ch_lang[i]]+=ch_ppl[i]
    else:
        anorth_lang[ch_lang[i]]=ch_ppl[i]
for i in range(len(ch_lang)):
    if ch_lang[i] in bnorth_lang:
        bnorth_lang[ch_lang[i]]+=ch_ppl[i]
    else:
        bnorth_lang[ch_lang[i]]=ch_ppl[i]
for i in range(len(ch_seclang)):
    if ch_seclang[i] in bnorth_lang:
        bnorth_lang[ch_seclang[i]]+=ch_secppl[i]
    else:
        bnorth_lang[ch_seclang[i]]=ch_secppl[i]
for i in range(len(ch_thrlang)):
    if ch_thrlang[i] in bnorth_lang:
        bnorth_lang[ch_thrlang[i]]+=ch_thrppl[i]
    else:
        bnorth_lang[ch_thrlang[i]]=ch_thrppl[i]
        
anorth=dict(sorted(anorth_lang.items(), key=lambda x:x[1], reverse=True))

altt=[]
altt.append("North")
for x in list(anorth)[0:3]:
    altt.append(x)
afin_lst.append(altt)

bnorth=dict(sorted(bnorth_lang.items(), key=lambda x:x[1], reverse=True))

bltt=[]
bltt.append("North")
for x in list(bnorth)[0:3]:
    bltt.append(x)
bfin_lst.append(bltt)


# In[14]:


df=pd.read_excel("DDW-C17-3500.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
ane_lang={}
bne_lang={}
an_lang=df1.lang.to_list()
an_ppl=df1.ppl.to_list()
an_seclang=df2.lang.to_list()
an_secppl=df2.ppl.to_list()
an_thrlang=df3.lang.to_list()
an_thrppl=df3.ppl.to_list()
for i in range(len(an_lang)):
    if an_lang[i] in ane_lang:
        ane_lang[an_lang[i]]+=an_ppl[i]
    else:
        ane_lang[an_lang[i]]=an_ppl[i]
for i in range(len(an_lang)):
    if an_lang[i] in bne_lang:
        bne_lang[an_lang[i]]+=an_ppl[i]
    else:
        bne_lang[an_lang[i]]=an_ppl[i]
for i in range(len(an_seclang)):
    if an_seclang[i] in bne_lang:
        bne_lang[an_seclang[i]]+=an_secppl[i]
    else:
        bne_lang[an_seclang[i]]=an_secppl[i]
for i in range(len(an_thrlang)):
    if an_thrlang[i] in bne_lang:
        bne_lang[an_thrlang[i]]+=an_thrppl[i]
    else:
        bne_lang[an_thrlang[i]]=an_thrppl[i]
        
df=pd.read_excel("DDW-C17-1800.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
as_lang=df1.lang.to_list()
as_ppl=df1.ppl.to_list()
as_seclang=df2.lang.to_list()
as_secppl=df2.ppl.to_list()
as_thrlang=df3.lang.to_list()
as_thrppl=df3.ppl.to_list()
for i in range(len(as_lang)):
    if as_lang[i] in ane_lang:
        ane_lang[as_lang[i]]+=as_ppl[i]
    else:
        ane_lang[as_lang[i]]=as_ppl[i]
for i in range(len(as_lang)):
    if as_lang[i] in bne_lang:
        bne_lang[as_lang[i]]+=as_ppl[i]
    else:
        bne_lang[as_lang[i]]=as_ppl[i]
for i in range(len(as_seclang)):
    if as_seclang[i] in bne_lang:
        bne_lang[as_seclang[i]]+=as_secppl[i]
    else:
        bne_lang[as_seclang[i]]=as_secppl[i]
for i in range(len(as_thrlang)):
    if as_thrlang[i] in bne_lang:
        bne_lang[as_thrlang[i]]+=as_thrppl[i]
    else:
        bne_lang[as_thrlang[i]]=as_thrppl[i]
        
df=pd.read_excel("DDW-C17-1100.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
sk_lang=df1.lang.to_list()
sk_ppl=df1.ppl.to_list()
sk_seclang=df2.lang.to_list()
sk_secppl=df2.ppl.to_list()
sk_thrlang=df3.lang.to_list()
sk_thrppl=df3.ppl.to_list()
for i in range(len(sk_lang)):
    if sk_lang[i] in ane_lang:
        ane_lang[sk_lang[i]]+=sk_ppl[i]
    else:
        ane_lang[sk_lang[i]]=sk_ppl[i]
for i in range(len(sk_lang)):
    if sk_lang[i] in bne_lang:
        bne_lang[sk_lang[i]]+=sk_ppl[i]
    else:
        bne_lang[sk_lang[i]]=sk_ppl[i]
for i in range(len(sk_seclang)):
    if sk_seclang[i] in bne_lang:
        bne_lang[sk_seclang[i]]+=sk_secppl[i]
    else:
        bne_lang[sk_seclang[i]]=sk_secppl[i]
for i in range(len(sk_thrlang)):
    if sk_thrlang[i] in bne_lang:
        bne_lang[sk_thrlang[i]]+=sk_thrppl[i]
    else:
        bne_lang[sk_thrlang[i]]=sk_thrppl[i]
        
df=pd.read_excel("DDW-C17-1700.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
mg_lang=df1.lang.to_list()
mg_ppl=df1.ppl.to_list()
mg_seclang=df2.lang.to_list()
mg_secppl=df2.ppl.to_list()
mg_thrlang=df3.lang.to_list()
mg_thrppl=df3.ppl.to_list()
for i in range(len(mg_lang)):
    if mg_lang[i] in ane_lang:
        ane_lang[mg_lang[i]]+=mg_ppl[i]
    else:
        ane_lang[mg_lang[i]]=mg_ppl[i]
for i in range(len(mg_lang)):
    if mg_lang[i] in bne_lang:
        bne_lang[mg_lang[i]]+=mg_ppl[i]
    else:
        bne_lang[mg_lang[i]]=mg_ppl[i]
for i in range(len(mg_seclang)):
    if mg_seclang[i] in bne_lang:
        bne_lang[mg_seclang[i]]+=mg_secppl[i]
    else:
        bne_lang[mg_seclang[i]]=mg_secppl[i]
for i in range(len(mg_thrlang)):
    if mg_thrlang[i] in bne_lang:
        bne_lang[mg_thrlang[i]]+=mg_thrppl[i]
    else:
        bne_lang[mg_thrlang[i]]=mg_thrppl[i]
        
df=pd.read_excel("DDW-C17-1600.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
tr_lang=df1.lang.to_list()
tr_ppl=df1.ppl.to_list()
tr_seclang=df2.lang.to_list()
tr_secppl=df2.ppl.to_list()
tr_thrlang=df3.lang.to_list()
tr_thrppl=df3.ppl.to_list()
for i in range(len(tr_lang)):
    if tr_lang[i] in ane_lang:
        ane_lang[tr_lang[i]]+=tr_ppl[i]
    else:
        ane_lang[tr_lang[i]]=tr_ppl[i]
for i in range(len(tr_lang)):
    if tr_lang[i] in bne_lang:
        bne_lang[tr_lang[i]]+=tr_ppl[i]
    else:
        bne_lang[tr_lang[i]]=tr_ppl[i]
for i in range(len(tr_seclang)):
    if tr_seclang[i] in bne_lang:
        bne_lang[tr_seclang[i]]+=tr_secppl[i]
    else:
        bne_lang[tr_seclang[i]]=tr_secppl[i]
for i in range(len(tr_thrlang)):
    if tr_thrlang[i] in bne_lang:
        bne_lang[tr_thrlang[i]]+=tr_thrppl[i]
    else:
        bne_lang[tr_thrlang[i]]=tr_thrppl[i]
        
df=pd.read_excel("DDW-C17-1200.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
ar_lang=df1.lang.to_list()
ar_ppl=df1.ppl.to_list()
ar_seclang=df2.lang.to_list()
ar_secppl=df2.ppl.to_list()
ar_thrlang=df3.lang.to_list()
ar_thrppl=df3.ppl.to_list()
for i in range(len(ar_lang)):
    if ar_lang[i] in ane_lang:
        ane_lang[ar_lang[i]]+=ar_ppl[i]
    else:
        ane_lang[ar_lang[i]]=ar_ppl[i]
for i in range(len(ar_lang)):
    if ar_lang[i] in bne_lang:
        bne_lang[ar_lang[i]]+=ar_ppl[i]
    else:
        bne_lang[ar_lang[i]]=ar_ppl[i]
for i in range(len(ar_seclang)):
    if ar_seclang[i] in bne_lang:
        bne_lang[ar_seclang[i]]+=ar_secppl[i]
    else:
        bne_lang[ar_seclang[i]]=ar_secppl[i]
for i in range(len(ar_thrlang)):
    if ar_thrlang[i] in bne_lang:
        bne_lang[ar_thrlang[i]]+=ar_thrppl[i]
    else:
        bne_lang[ar_thrlang[i]]=ar_thrppl[i]
        
df=pd.read_excel("DDW-C17-1400.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
mn_lang=df1.lang.to_list()
mn_ppl=df1.ppl.to_list()
mn_seclang=df2.lang.to_list()
mn_secppl=df2.ppl.to_list()
mn_thrlang=df3.lang.to_list()
mn_thrppl=df3.ppl.to_list()
for i in range(len(mn_lang)):
    if mn_lang[i] in ane_lang:
        ane_lang[mn_lang[i]]+=mn_ppl[i]
    else:
        ane_lang[mn_lang[i]]=mn_ppl[i]
for i in range(len(mn_lang)):
    if mn_lang[i] in bne_lang:
        bne_lang[mn_lang[i]]+=mn_ppl[i]
    else:
        bne_lang[mn_lang[i]]=mn_ppl[i]
for i in range(len(mn_seclang)):
    if mn_seclang[i] in bne_lang:
        bne_lang[mn_seclang[i]]+=mn_secppl[i]
    else:
        bne_lang[mn_seclang[i]]=mn_secppl[i]
for i in range(len(mn_thrlang)):
    if mn_thrlang[i] in bne_lang:
        bne_lang[mn_thrlang[i]]+=mn_thrppl[i]
    else:
        bne_lang[mn_thrlang[i]]=mn_thrppl[i]
        
df=pd.read_excel("DDW-C17-1300.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
ng_lang=df1.lang.to_list()
ng_ppl=df1.ppl.to_list()
ng_seclang=df2.lang.to_list()
ng_secppl=df2.ppl.to_list()
ng_thrlang=df3.lang.to_list()
ng_thrppl=df3.ppl.to_list()
for i in range(len(ng_lang)):
    if ng_lang[i] in ane_lang:
        ane_lang[ng_lang[i]]+=ng_ppl[i]
    else:
        ane_lang[ng_lang[i]]=ng_ppl[i]
for i in range(len(ng_lang)):
    if ng_lang[i] in bne_lang:
        bne_lang[ng_lang[i]]+=ng_ppl[i]
    else:
        bne_lang[ng_lang[i]]=ng_ppl[i]
for i in range(len(ng_seclang)):
    if ng_seclang[i] in bne_lang:
        bne_lang[ng_seclang[i]]+=ng_secppl[i]
    else:
        bne_lang[ng_seclang[i]]=ng_secppl[i]
for i in range(len(ng_thrlang)):
    if ng_thrlang[i] in bne_lang:
        bne_lang[ng_thrlang[i]]+=ng_thrppl[i]
    else:
        bne_lang[ng_thrlang[i]]=ng_thrppl[i]
        
df=pd.read_excel("DDW-C17-1500.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
mz_lang=df1.lang.to_list()
mz_ppl=df1.ppl.to_list()
mz_seclang=df2.lang.to_list()
mz_secppl=df2.ppl.to_list()
mz_thrlang=df3.lang.to_list()
mz_thrppl=df3.ppl.to_list()
for i in range(len(mz_lang)):
    if mz_lang[i] in ane_lang:
        ane_lang[mz_lang[i]]+=mz_ppl[i]
    else:
        ane_lang[mz_lang[i]]=mz_ppl[i]
for i in range(len(mz_lang)):
    if mz_lang[i] in bne_lang:
        bne_lang[mz_lang[i]]+=mz_ppl[i]
    else:
        bne_lang[mz_lang[i]]=mz_ppl[i]
for i in range(len(mz_seclang)):
    if mz_seclang[i] in bne_lang:
        bne_lang[mz_seclang[i]]+=mz_secppl[i]
    else:
        bne_lang[mz_seclang[i]]=mz_secppl[i]
for i in range(len(mz_thrlang)):
    if mz_thrlang[i] in bne_lang:
        bne_lang[mz_thrlang[i]]+=mz_thrppl[i]
    else:
        bne_lang[mz_thrlang[i]]=mz_thrppl[i]

anorth_east=dict(sorted(ane_lang.items(), key=lambda x:x[1], reverse=True))

altt=[]
altt.append("North-East")
for x in list(anorth_east)[0:3]:
    altt.append(x)
afin_lst.append(altt)

bnorth_east=dict(sorted(bne_lang.items(), key=lambda x:x[1], reverse=True))

bltt=[]
bltt.append("North-East")
for x in list(bnorth_east)[0:3]:
    bltt.append(x)
bfin_lst.append(bltt)


# In[15]:


df=pd.read_excel("DDW-C17-2900.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
asouth_lang={}
bsouth_lang={}
kt_lang=df1.lang.to_list()
kt_ppl=df1.ppl.to_list()
kt_seclang=df2.lang.to_list()
kt_secppl=df2.ppl.to_list()
kt_thrlang=df3.lang.to_list()
kt_thrppl=df3.ppl.to_list()
for i in range(len(kt_lang)):
    if kt_lang[i] in asouth_lang:
        asouth_lang[kt_lang[i]]+=kt_ppl[i]
    else:
        asouth_lang[kt_lang[i]]=kt_ppl[i]
for i in range(len(kt_lang)):
    if kt_lang[i] in bsouth_lang:
        bsouth_lang[kt_lang[i]]+=kt_ppl[i]
    else:
        bsouth_lang[kt_lang[i]]=kt_ppl[i]
for i in range(len(kt_seclang)):
    if kt_seclang[i] in bsouth_lang:
        bsouth_lang[kt_seclang[i]]+=kt_secppl[i]
    else:
        bsouth_lang[kt_seclang[i]]=kt_secppl[i]
for i in range(len(kt_thrlang)):
    if kt_thrlang[i] in bsouth_lang:
        bsouth_lang[kt_thrlang[i]]+=kt_thrppl[i]
    else:
        bsouth_lang[kt_thrlang[i]]=kt_thrppl[i]
        
df=pd.read_excel("DDW-C17-2800.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
tg_lang=df1.lang.to_list()
tg_ppl=df1.ppl.to_list()
tg_seclang=df2.lang.to_list()
tg_secppl=df2.ppl.to_list()
tg_thrlang=df3.lang.to_list()
tg_thrppl=df3.ppl.to_list()
for i in range(len(tg_lang)):
    if tg_lang[i] in asouth_lang:
        asouth_lang[tg_lang[i]]+=tg_ppl[i]
    else:
        asouth_lang[tg_lang[i]]=tg_ppl[i]
for i in range(len(tg_lang)):
    if tg_lang[i] in bsouth_lang:
        bsouth_lang[tg_lang[i]]+=tg_ppl[i]
    else:
        bsouth_lang[tg_lang[i]]=tg_ppl[i]
for i in range(len(tg_seclang)):
    if tg_seclang[i] in bsouth_lang:
        bsouth_lang[tg_seclang[i]]+=tg_secppl[i]
    else:
        bsouth_lang[tg_seclang[i]]=tg_secppl[i]
for i in range(len(tg_thrlang)):
    if tg_thrlang[i] in bsouth_lang:
        bsouth_lang[tg_thrlang[i]]+=tg_thrppl[i]
    else:
        bsouth_lang[tg_thrlang[i]]=tg_thrppl[i]
        
df=pd.read_excel("DDW-C17-3300.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
tn_lang=df1.lang.to_list()
tn_ppl=df1.ppl.to_list()
tn_seclang=df2.lang.to_list()
tn_secppl=df2.ppl.to_list()
tn_thrlang=df3.lang.to_list()
tn_thrppl=df3.ppl.to_list()
for i in range(len(tn_lang)):
    if tn_lang[i] in asouth_lang:
        asouth_lang[tn_lang[i]]+=tn_ppl[i]
    else:
        asouth_lang[tn_lang[i]]=tn_ppl[i]
for i in range(len(tn_lang)):
    if tn_lang[i] in bsouth_lang:
        bsouth_lang[tn_lang[i]]+=tn_ppl[i]
    else:
        bsouth_lang[tn_lang[i]]=tn_ppl[i]
for i in range(len(tn_seclang)):
    if tn_seclang[i] in bsouth_lang:
        bsouth_lang[tn_seclang[i]]+=tn_secppl[i]
    else:
        bsouth_lang[tn_seclang[i]]=tn_secppl[i]
for i in range(len(tn_thrlang)):
    if tn_thrlang[i] in bsouth_lang:
        bsouth_lang[tn_thrlang[i]]+=tn_thrppl[i]
    else:
        bsouth_lang[tn_thrlang[i]]=tn_thrppl[i]
        
df=pd.read_excel("DDW-C17-3200.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
kl_lang=df1.lang.to_list()
kl_ppl=df1.ppl.to_list()
kl_seclang=df2.lang.to_list()
kl_secppl=df2.ppl.to_list()
kl_thrlang=df3.lang.to_list()
kl_thrppl=df3.ppl.to_list()
for i in range(len(kl_lang)):
    if kl_lang[i] in asouth_lang:
        asouth_lang[kl_lang[i]]+=kl_ppl[i]
    else:
        asouth_lang[kl_lang[i]]=kl_ppl[i]
for i in range(len(kl_lang)):
    if kl_lang[i] in bsouth_lang:
        bsouth_lang[kl_lang[i]]+=kl_ppl[i]
    else:
        bsouth_lang[kl_lang[i]]=kl_ppl[i]
for i in range(len(kl_seclang)):
    if kl_seclang[i] in bsouth_lang:
        bsouth_lang[kl_seclang[i]]+=kl_secppl[i]
    else:
        bsouth_lang[kl_seclang[i]]=kl_secppl[i]
for i in range(len(kl_thrlang)):
    if kl_thrlang[i] in bsouth_lang:
        bsouth_lang[kl_thrlang[i]]+=kl_thrppl[i]
    else:
        bsouth_lang[kl_thrlang[i]]=kl_thrppl[i]
        
df=pd.read_excel("DDW-C17-3100.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
ld_lang=df1.lang.to_list()
ld_ppl=df1.ppl.to_list()
ld_seclang=df2.lang.to_list()
ld_secppl=df2.ppl.to_list()
ld_thrlang=df3.lang.to_list()
ld_thrppl=df3.ppl.to_list()
for i in range(len(ld_lang)):
    if ld_lang[i] in asouth_lang:
        asouth_lang[ld_lang[i]]+=ld_ppl[i]
    else:
        asouth_lang[ld_lang[i]]=ld_ppl[i]
for i in range(len(ld_lang)):
    if ld_lang[i] in bsouth_lang:
        bsouth_lang[ld_lang[i]]+=ld_ppl[i]
    else:
        bsouth_lang[ld_lang[i]]=ld_ppl[i]
for i in range(len(ld_seclang)):
    if ld_seclang[i] in bsouth_lang:
        bsouth_lang[ld_seclang[i]]+=ld_secppl[i]
    else:
        bsouth_lang[ld_seclang[i]]=ld_secppl[i]
for i in range(len(ld_thrlang)):
    if ld_thrlang[i] in bsouth_lang:
        bsouth_lang[ld_thrlang[i]]+=ld_thrppl[i]
    else:
        bsouth_lang[ld_thrlang[i]]=ld_thrppl[i]
        
df=pd.read_excel("DDW-C17-3400.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
pd_lang=df1.lang.to_list()
pd_ppl=df1.ppl.to_list()
pd_seclang=df2.lang.to_list()
pd_secppl=df2.ppl.to_list()
pd_thrlang=df3.lang.to_list()
pd_thrppl=df3.ppl.to_list()
for i in range(len(pd_lang)):
    if pd_lang[i] in asouth_lang:
        asouth_lang[pd_lang[i]]+=pd_ppl[i]
    else:
        asouth_lang[pd_lang[i]]=pd_ppl[i]
for i in range(len(pd_lang)):
    if pd_lang[i] in bsouth_lang:
        bsouth_lang[pd_lang[i]]+=pd_ppl[i]
    else:
        bsouth_lang[pd_lang[i]]=pd_ppl[i]
for i in range(len(pd_seclang)):
    if pd_seclang[i] in bsouth_lang:
        bsouth_lang[pd_seclang[i]]+=pd_secppl[i]
    else:
        bsouth_lang[pd_seclang[i]]=pd_secppl[i]
for i in range(len(pd_thrlang)):
    if pd_thrlang[i] in bsouth_lang:
        bsouth_lang[pd_thrlang[i]]+=pd_thrppl[i]
    else:
        bsouth_langpd[_thrlang[i]]=pd_thrppl[i]
        
asouth=dict(sorted(asouth_lang.items(), key=lambda x:x[1], reverse=True))

altt=[]
altt.append("South")
for x in list(asouth)[0:3]:
    altt.append(x)
afin_lst.append(altt)

bsouth=dict(sorted(bsouth_lang.items(), key=lambda x:x[1], reverse=True))

bltt=[]
bltt.append("South")
for x in list(bsouth)[0:3]:
    bltt.append(x)
bfin_lst.append(bltt)


# In[16]:


df=pd.read_excel("DDW-C17-0800.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
awest_lang={}
bwest_lang={}
rj_lang=df1.lang.to_list()
rj_ppl=df1.ppl.to_list()
rj_seclang=df2.lang.to_list()
rj_secppl=df2.ppl.to_list()
rj_thrlang=df3.lang.to_list()
rj_thrppl=df3.ppl.to_list()
for i in range(len(rj_lang)):
    if rj_lang[i] in awest_lang:
        awest_lang[rj_lang[i]]+=rj_ppl[i]
    else:
        awest_lang[rj_lang[i]]=rj_ppl[i]
for i in range(len(rj_lang)):
    if rj_lang[i] in bwest_lang:
        bwest_lang[rj_lang[i]]+=rj_ppl[i]
    else:
        bwest_lang[rj_lang[i]]=rj_ppl[i]
for i in range(len(rj_seclang)):
    if rj_seclang[i] in bwest_lang:
        bwest_lang[rj_seclang[i]]+=rj_secppl[i]
    else:
        bwest_lang[rj_seclang[i]]=rj_secppl[i]
for i in range(len(rj_thrlang)):
    if rj_thrlang[i] in bwest_lang:
        bwest_lang[rj_thrlang[i]]+=rj_thrppl[i]
    else:
        bwest_lang[rj_thrlang[i]]=rj_thrppl[i]
        
df=pd.read_excel("DDW-C17-2400.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
gj_lang=df1.lang.to_list()
gj_ppl=df1.ppl.to_list()
gj_seclang=df2.lang.to_list()
gj_secppl=df2.ppl.to_list()
gj_thrlang=df3.lang.to_list()
gj_thrppl=df3.ppl.to_list()
for i in range(len(gj_lang)):
    if gj_lang[i] in awest_lang:
        awest_lang[gj_lang[i]]+=gj_ppl[i]
    else:
        awest_lang[gj_lang[i]]=gj_ppl[i]
for i in range(len(gj_lang)):
    if gj_lang[i] in bwest_lang:
        bwest_lang[gj_lang[i]]+=gj_ppl[i]
    else:
        bwest_lang[gj_lang[i]]=gj_ppl[i]
for i in range(len(gj_seclang)):
    if gj_seclang[i] in bwest_lang:
        bwest_lang[gj_seclang[i]]+=gj_secppl[i]
    else:
        bwest_lang[gj_seclang[i]]=gj_secppl[i]
for i in range(len(gj_thrlang)):
    if gj_thrlang[i] in bwest_lang:
        bwest_lang[gj_thrlang[i]]+=gj_thrppl[i]
    else:
        bwest_lang[gj_thrlang[i]]=gj_thrppl[i]
        
df=pd.read_excel("DDW-C17-2700.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
mh_lang=df1.lang.to_list()
mh_ppl=df1.ppl.to_list()
mh_seclang=df2.lang.to_list()
mh_secppl=df2.ppl.to_list()
mh_thrlang=df3.lang.to_list()
mh_thrppl=df3.ppl.to_list()
for i in range(len(mh_lang)):
    if mh_lang[i] in awest_lang:
        awest_lang[mh_lang[i]]+=mh_ppl[i]
    else:
        awest_lang[mh_lang[i]]=mh_ppl[i]
for i in range(len(mh_lang)):
    if mh_lang[i] in bwest_lang:
        bwest_lang[mh_lang[i]]+=mh_ppl[i]
    else:
        bwest_lang[mh_lang[i]]=mh_ppl[i]
for i in range(len(mh_seclang)):
    if mh_seclang[i] in bwest_lang:
        bwest_lang[mh_seclang[i]]+=mh_secppl[i]
    else:
        bwest_lang[mh_seclang[i]]=mh_secppl[i]
for i in range(len(mh_thrlang)):
    if mh_thrlang[i] in bwest_lang:
        bwest_lang[mh_thrlang[i]]+=mh_thrppl[i]
    else:
        bwest_lang[mh_thrlang[i]]=mh_thrppl[i]
        
df=pd.read_excel("DDW-C17-3000.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
goa_lang=df1.lang.to_list()
goa_ppl=df1.ppl.to_list()
goa_seclang=df2.lang.to_list()
goa_secppl=df2.ppl.to_list()
goa_thrlang=df3.lang.to_list()
goa_thrppl=df3.ppl.to_list()
for i in range(len(goa_lang)):
    if goa_lang[i] in awest_lang:
        awest_lang[goa_lang[i]]+=goa_ppl[i]
    else:
        awest_lang[goa_lang[i]]=goa_ppl[i]
for i in range(len(goa_lang)):
    if goa_lang[i] in bwest_lang:
        bwest_lang[goa_lang[i]]+=goa_ppl[i]
    else:
        bwest_lang[goa_lang[i]]=goa_ppl[i]
for i in range(len(goa_seclang)):
    if goa_seclang[i] in bwest_lang:
        bwest_lang[goa_seclang[i]]+=goa_secppl[i]
    else:
        bwest_lang[goa_seclang[i]]=goa_secppl[i]
for i in range(len(goa_thrlang)):
    if goa_thrlang[i] in bwest_lang:
        bwest_lang[goa_thrlang[i]]+=goa_thrppl[i]
    else:
        bwest_lang[goa_thrlang[i]]=goa_thrppl[i]
        
df=pd.read_excel("DDW-C17-2600.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
dn_lang=df1.lang.to_list()
dn_ppl=df1.ppl.to_list()
dn_seclang=df2.lang.to_list()
dn_secppl=df2.ppl.to_list()
dn_thrlang=df3.lang.to_list()
dn_thrppl=df3.ppl.to_list()
for i in range(len(dn_lang)):
    if dn_lang[i] in awest_lang:
        awest_lang[dn_lang[i]]+=dn_ppl[i]
    else:
        awest_lang[dn_lang[i]]=dn_ppl[i]
for i in range(len(dn_lang)):
    if dn_lang[i] in bwest_lang:
        bwest_lang[dn_lang[i]]+=dn_ppl[i]
    else:
        bwest_lang[dn_lang[i]]=dn_ppl[i]
for i in range(len(dn_seclang)):
    if dn_seclang[i] in bwest_lang:
        bwest_lang[dn_seclang[i]]+=dn_secppl[i]
    else:
        bwest_lang[dn_seclang[i]]=dn_secppl[i]
for i in range(len(dn_thrlang)):
    if dn_thrlang[i] in bwest_lang:
        bwest_lang[dn_thrlang[i]]+=dn_thrppl[i]
    else:
        bwest_lang[dn_thrlang[i]]=dn_thrppl[i]
        
df=pd.read_excel("DDW-C17-2500.XLSX")
df1=pd.DataFrame(df,columns=["Unnamed: 3","Unnamed: 4"])
df1=df1[5:]
df1=df1.rename(columns={"Unnamed: 3":"lang","Unnamed: 4":"ppl"})
df1=df1.dropna()
df2=pd.DataFrame(df,columns=["Unnamed: 8","Unnamed: 9"])
df2=df2[5:]
df2=df2.rename(columns={"Unnamed: 8":"lang","Unnamed: 9":"ppl"})
df2=df2.dropna()
df3=pd.DataFrame(df,columns=["Unnamed: 13","Unnamed: 14"])
df3=df3[5:]
df3=df3.rename(columns={"Unnamed: 13":"lang","Unnamed: 14":"ppl"})
df3=df3.dropna()
dd_lang=df1.lang.to_list()
dd_ppl=df1.ppl.to_list()
dd_seclang=df2.lang.to_list()
dd_secppl=df2.ppl.to_list()
dd_thrlang=df3.lang.to_list()
dd_thrppl=df3.ppl.to_list()
for i in range(len(dd_lang)):
    if dd_lang[i] in awest_lang:
        awest_lang[dd_lang[i]]+=dd_ppl[i]
    else:
        awest_lang[dd_lang[i]]=dd_ppl[i]
for i in range(len(dd_lang)):
    if dd_lang[i] in bwest_lang:
        bwest_lang[dd_lang[i]]+=dd_ppl[i]
    else:
        bwest_lang[dd_lang[i]]=dd_ppl[i]
for i in range(len(dd_seclang)):
    if dd_seclang[i] in bwest_lang:
        bwest_lang[dd_seclang[i]]+=dd_secppl[i]
    else:
        bwest_lang[dd_seclang[i]]=dd_secppl[i]
for i in range(len(dd_thrlang)):
    if dd_thrlang[i] in bwest_lang:
        bwest_lang[dd_thrlang[i]]+=dd_thrppl[i]
    else:
        bwest_lang[dd_thrlang[i]]=dd_thrppl[i]
        
awest=dict(sorted(awest_lang.items(), key=lambda x:x[1], reverse=True))

altt=[]
altt.append("West")
for x in list(awest)[0:3]:
    altt.append(x)
afin_lst.append(altt)

bwest=dict(sorted(bwest_lang.items(), key=lambda x:x[1], reverse=True))

bltt=[]
bltt.append("West")
for x in list(bwest)[0:3]:
    bltt.append(x)
bfin_lst.append(bltt)


# In[17]:


with open('region-india-a.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["region", "language-1", "language-2","language-3"])
    writer.writerows(afin_lst)


# In[18]:


with open('region-india-b.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["region", "language-1", "language-2","language-3"])
    writer.writerows(bfin_lst)


# In[ ]:




