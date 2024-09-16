#!/usr/bin/env python
# coding: utf-8

# # Python Data Analysis (Pandas)

# ## Problem 2:
# #### Save your file as Surname_Pandas-P1.py
# #### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# 

# ### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars

# In[6]:


def selectdisplay(start_rowindex, end_rowindex, start_columnindex, df, end_columnindex = '', step=1):
    # Sets the value of the end_columnindex depending of what the user inputted
    # If the user wants to output all of the columns, he should put '' 
    if end_columnindex == '':
        end_columnindex = None
    # else he can input an integer to set the end_columnindex 
    else:
        end_columnindex = int(end_columnindex)
    # If the user inputted an empty space for the end_columnindex, the function will return this:
    if end_columnindex is None:
        # Uses the .iloc[] function to display five rows w/ odd-numbered columns of the cars_file dataframe
        # .iloc[] function was used because the method used was integer indexing
        return df.iloc[start_rowindex:end_rowindex,start_columnindex::step]
    # Else the function will return this:
    else:
        return df.iloc[start_rowindex:end_rowindex,start_columnindex:end_columnindex:step]
# The parameter 0 & 5 bounds the output to only display the first five rows (Start row, End row)
# The parameter cars_file is the variable wherein the dataframe is stored 
# The parameter 1 & '' ensures that the column startingh from index 1 to the end of the indices are displayed (Start column, End Column)
# The parameter 2 ensures that only the odd-numbered columns are displayed (Step size)
# '' and the stepsize are in the end part of the parameters due to the order of parameters of python wherein the ones with no default values are put first before the ones with default values
selectdisplay(0,5,1, cars,'',2)


# #### b. Display the row that contains the 'Model' of 'Mazda RX4'.

# In[8]:


# Defines a function DisplayCar()
def DisplayCar(car_name, df):
    # Filters the dataframe to the Model column of the DataFrame for rows where the value matches the car_name.
    return df.loc[df['Model']==car_name]
#Calls the DisplayCar() function with the name of the car & the variable wherein the dataframe is stored as its parameters
DisplayCar('Mazda RX4', cars)


# #### c. How many cylinders('cyl') does the car model 'Camaro Z28' have?

# In[17]:


# Defines a function ComplexQuery()
# The parameters are the car names the user wants to display and the variable wherein the dataframe is stored
# The columns variable are initially set to None to ensure that the function parameter is dynamic and not fixed to a default column lists
def ComplexQuery(df, car_names, columns=None):
    # This ensures that whenever the user did not input any for the columns parameter, it will use the default parameters
    if not columns:
        columns = ['Model', 'cyl', 'gear']
    # Calls the .loc function as well as .isin function to filter the rows and columns of the dataframe depending on the list of values(car_names) as well as the specific lists of columns
    return df.loc[df['Model'].isin(car_names), columns]

# Uses the ComplexQuery() function to determine the number of cylinders of Camaro Z28
# Added 'Model' to the columns to improve the readability and format of the output
ComplexQuery(cars, ['Camaro Z28'], ['Model','cyl'])


# #### d. Determine how many cylinders('cyl') and what gear type ('gear') do the car models 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic' Have.

# In[23]:


#outputs the Model, gear, and cylinder of the ff car models
ComplexQuery(cars, ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'], ['Model','cyl','gear'])


# In[ ]:




