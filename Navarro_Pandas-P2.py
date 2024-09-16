#!/usr/bin/env python
# coding: utf-8

# # Python Data Analysis (Pandas)

# ## Problem 2:
# #### Save your file as Surname_Pandas-P1.py
# #### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# 

# In[4]:


# Imports the pandas library 
import pandas as pd
# Reads the '.csv' file with the use of read_csv() function of the pandas library
# stores the .csv file into 'cars' variable
cars = pd.read_csv('cars.csv')
# calls the 'cars' variable to output the data 
cars


# ### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars

# In[5]:


#To display the first five rows with odd-numbered columns, # This code selects rows 0 to 4 and every second column
cars.loc[0:4,::2]


# #### b. Display the row that contains the 'Model' of 'Mazda RX4'.

# In[7]:


#This code filters the cars DataFrame to return all rows where the value in the 'Model' column is equal to 'Mazda RX4'
cars.loc[cars['Model'] == 'Mazda RX4']


# #### c. How many cylinders('cyl') does the car model 'Camaro Z28' have?

# In[8]:


# This code filters the DataFrame for rows where the 'Model' is 'Camaro Z28' and selects only the 'Model' and 'cyl' columns.
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]


# #### d. Determine how many cylinders('cyl') and what gear type ('gear') do the car models 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic' Have.

# In[9]:


# This code filters the DataFrame to select rows where the 'Model' is either 'Mazda RX4 Wag', 'Ford Pantera L', or 'Honda Civic', and retrieves only the 'Model', 'cyl', and 'gear' columns.
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L')|
         (cars['Model'] == 'Honda Civic') ,['Model','cyl','gear']]


# In[ ]:




