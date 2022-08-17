#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[24]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[25]:



df=pd.read_csv("salaries1.csv")


# ** Check the head of the DataFrame. **

# In[26]:


df.head()


# ** Use the .info() method to find out how many entries there are.**

# In[3]:


df.info()


# **What is the average BasePay ?**

# In[4]:


df["BasePay"].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[5]:


df["OvertimePay"].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[7]:


df[df["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"]


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[8]:


df[df["EmployeeName"]=="JOSEPH DRISCOLL"]["TotalPayBenefits"]


# ** What is the name of highest paid person (including benefits)?**

# In[10]:


df[df["TotalPayBenefits"]==df["TotalPayBenefits"].max()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[11]:


df[df["TotalPayBenefits"]==df["TotalPayBenefits"].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[13]:


df.groupby("Year").mean()["BasePay"]


# ** How many unique job titles are there? **

# In[16]:


df["JobTitle"].nunique()


# ** What are the top 5 most common jobs? **

# In[17]:


jobs=df.groupby("JobTitle").count()
top=jobs.sort_values(by="Id", ascending=False)[:5]
top["Id"]


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[20]:


year=df[df["Year"]==2013]
group=year.groupby("JobTitle").count()
count=group[group["Id"]==1]
count.count()["Id"]


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[22]:


def fun(job_title):
    if "chief" in job_title.lower().split():
        return True
    else:
        return False
df=pd.read_csv("salaries1.csv")
sum(df["JobTitle"].apply(lambda x: fun(x)))


# In[ ]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[22]:





# In[23]:


df["title_len"]=df["JobTitle"].apply(len)
df[["title_len","TotalPayBenefits"]].corr()


# # Great Job!
