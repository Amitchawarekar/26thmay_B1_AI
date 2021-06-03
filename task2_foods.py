#!/usr/bin/env python
# coding: utf-8

# ## Task 2 

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


foods=pd.read_excel('foods_task2.xlsx')


# In[6]:


foods


# In[35]:


Taste= foods['Taste']


# In[37]:


Taste.str.capitalize()


# In[38]:


foods.columns


# In[39]:


foods.values


# In[40]:


c= foods[['Price','Cuisine']]
c


# In[41]:


Cuisine= c['Cuisine'].unique()


# In[42]:


Cuisine


# In[43]:


foods['Cuisine'].value_counts()


# ## 1.Costliest Food

# In[44]:


foods[['Food Name','Price','City','Color','Cuisine','Taste']][foods['Price']==foods['Price'].max()]


# ## 2.Cheapest Spicy Food

# In[45]:


foods[['Food Name','Price','City','Color','Cuisine','Taste']][(foods['Taste']=='Spicy') & (foods['Price'] == foods['Price'][foods['Taste']=='Spicy'].min())]


# ## 3.Most Popular Cuisine

# In[46]:


m=foods['Cuisine'].value_counts()
m


# In[33]:


foods['Cuisine'][foods['Cuisine'].value_counts().max()]


# ## 4.Count of Different tastes

# In[47]:


foods['Taste'].value_counts()


# ## 5.Foods which is available in Pune and is Spicy

# In[49]:


foods


# In[52]:


foods['Food Name'][(foods['City']=='Pune') & (foods['Taste']== 'spicy')]


# ## 6.list of south indian cuisine

# In[53]:


foods[foods['Cuisine'] == 'South Indian']


# In[ ]:




