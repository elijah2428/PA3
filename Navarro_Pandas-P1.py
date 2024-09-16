#!/usr/bin/env python
# coding: utf-8

# # Python Data Analysis (Pandas)

# ## Problem 1:

# #### Save you file as Surname_Pandas-P1.py

# #### Using knowledge obtained from the experiment and demonstrations:
# #### a. Load the Corresponding .csv file into a data frame named cars using pandas
# #### b. Display the first five and last five rows of the resulting cars.

# In[11]:


# Imports the pandas library 
import pandas as pd
# Reads the '.csv' file with the use of read_csv() function of the pandas library
# stores the .csv file into 'cars' variable
cars = pd.read_csv('cars.csv')
# calls the 'cars' variable to output the data 
cars


# In[12]:


#this calls the .head function to display the first five indeces of the dataframe from 'cars'
cars.head()


# In[13]:


#this calls the .tail function to display the first five indeces of the dataframe from 'cars'
cars.tail()

