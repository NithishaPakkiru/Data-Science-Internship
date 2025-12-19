#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing required librarries

import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# reading SuperMarket Sales dataset

df = pd.read_csv(r"C:\Users\nithi\Downloads\SuperMarket Analysis.csv")


# In[3]:


# displaying the dataset
df


# In[4]:


# displaying the number of rows and columns of the dataset

df.shape


# In[5]:


# displaying top 5 rows of the dataset 

df.head()


# In[6]:


# displaying descriptive statistics of the dataset

df.describe()


# In[7]:


# checking the datatypes of the columns and checking for any nulls

df.info()


# In[8]:


# removing the columns which are not required for our analysis
df = df.drop(columns= ['Time', 'gross margin percentage', 'Invoice ID'], axis=1)
df


# In[9]:


# finding total_sales

total_sales = df['Sales'].sum()
total_sales


# In[10]:


# finding best selling product

best_selling_product = df.groupby('Product line')['Sales'].sum().sort_values(ascending = True)


# In[11]:


# plotting Product Performance

best_selling_product.plot(kind='barh', figsize=(10,5))
plt.title('Total sales by Product line')
plt.xlabel('Product line')
plt.ylabel('Sales')
plt.show()


# In[12]:


# Bar plot displaying total sales across branches 

branch_sales = df.groupby('Branch')['Sales'].sum().sort_values(ascending = False)
branch_sales.plot(kind='bar', figsize=(10,5), color = 'pink')
plt.title('Total sales by Branch')
plt.ylabel('Sales')
plt.show()


# In[13]:


gender_sales = df.groupby("Gender")["Sales"].sum()

# Pie Plot to show the Gender impact on Sales

y = gender_sales
plt.title("Total Sales by Gender")
plt.pie(y, labels = gender_sales.index, autopct='%1.1f%%')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




