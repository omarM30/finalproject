#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


df=pd.read_csv("Salaries.csv",low_memory=False)
df


# In[6]:


df.info()


# In[7]:


df.columns=df.columns.str.strip()


# In[8]:


df["EmployeeName"]=df["EmployeeName"].str.lower()
df["JobTitle"]=df["JobTitle"].str.lower()
df


# In[9]:


df.info()


# In[10]:


df["BasePay"]=pd.to_numeric(df["BasePay"],errors="coerce")
df["OvertimePay"]=pd.to_numeric(df["OvertimePay"],errors="coerce")
df["OtherPay"]=pd.to_numeric(df["OtherPay"],errors="coerce")
df["Benefits"]=pd.to_numeric(df["Benefits"],errors="coerce")
df.info()


# In[12]:


df.isnull().sum()


# In[13]:


df["BasePay"]=df["BasePay"].fillna(0)
df["OvertimePay"]=df["OvertimePay"].fillna(0)
df["OtherPay"]=df["OtherPay"].fillna(0)
df["Benefits"]=df["Benefits"].fillna(0)
df["Status"]=df["Status"].fillna("unknown")
df.isnull().sum()


# 

# In[ ]:





# In[38]:


df["TotalPay"].mean()


# # The highest paid employee

# In[39]:


df['TotalPay'].max()


# In[40]:


df['TotalPay'].min()


# In[41]:


df.describe()


# In[46]:





# In[63]:


df.groupby('Year').mean()['TotalPay']


# In[31]:


MaxEm=df["TotalPayBenefits"]==df['TotalPayBenefits'].max()


# In[36]:


df[MaxEm][["EmployeeName","TotalPayBenefits"]]


# In[16]:


MinEm=df["TotalPayBenefits"]==df['TotalPayBenefits'].min()
df[MinEm][["EmployeeName","TotalPayBenefits"]]


# In[50]:


df['TotalPayBenefits'].count()


# In[38]:


df.duplicated()


# In[15]:


df.to_csv(r"E:\course\sf salaries.csv")


# In[19]:


df.describe()


# In[53]:


Maxjob=df["TotalPay"]==df['TotalPay'].max()
df[Maxjob][["JobTitle","TotalPay"]]


# In[52]:


Minjob=df["TotalPay"]==df['TotalPay'].min()
df[Minjob][["JobTitle","TotalPay"]]


# In[31]:


df.drop('Notes', axis=1, inplace=True)


# In[29]:


df


# In[32]:


df.drop('Agency', axis=1, inplace=True)


# In[36]:


df.count()


# In[57]:


df["JobTitle"].describe()


# In[64]:


df['EmployeeName'].value_counts().head(10)


# In[77]:


df.groupby('Year').max()['TotalPay']


# In[78]:


df.groupby(["EmployeeName"]).count()["OvertimePay"]


# In[79]:


df['OvertimePay'].describe()


# In[81]:


df.groupby('OvertimePay').mean()['TotalPayBenefits']


# In[84]:


df.groupby(["TotalPayBenefits"]).count()["OvertimePay"]


# In[93]:


df["Benefits"].value_counts().head(10)


# In[116]:


df['Benefits'] = df['TotalPay'].count()
df[['Benefits', 'TotalPay']].corr()


# In[103]:


df.groupby(["JobTitle"]).mean()["TotalPayBenefits"]


# In[105]:


df.groupby(["JobTitle"]).count()["EmployeeName"]


# In[107]:


df.groupby(["JobTitle"])["EmployeeName"].describe()


# In[119]:


df[''] = df['TotalPay'].count()
df[['Benefits', 'TotalPay']].corr()


# In[ ]:





# In[ ]:




