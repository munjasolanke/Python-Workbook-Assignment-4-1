#!/usr/bin/env python
# coding: utf-8

# In[2]:


#WEEK 7 - Python Workbook Assignment 4-1
import pandas as pd
df = pd.read_csv(r"C:\MUNJA_DATA\Courses\Data Visualization\Week-7\learn-data-analysis-w-python-master\datasets\gradedata.csv")
df.head()


# In[3]:


# Create the bin dividers
bins = [0, 80, 100]
# Create names for the four groups
group_names = ['Fail', 'Pass']


# In[4]:


df['Pass/Fail'] = pd.cut(df['grade'], bins,
labels=group_names, right=False)


# In[5]:


df.head()


# In[ ]:




