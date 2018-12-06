
# coding: utf-8

# In[46]:


""" -------------------------------------------------------------------------------------------------------
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ APPLIED DATA SCIENCE: FINAL PROJECT! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    -------------------------------------------------------------------------------------------------------
        
                        # =================== Final Project: Parts 2 & 3 ====================
                        # ============ Author: Savannah McCoy, Azeezah Muhammad =============
                        # ================ Howard University -- Fall 2018 ===================
                        # ================ CSCI 473: Applied Data Science ===================

"""

import matplotlib as mpl
mpl.use('TkAgg')

import os, sys, json, math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
from scipy import stats
from tabulate import tabulate
    
    
def part_2a(df):
    
    df['date'] = df['reference_period_desc'] + df['year']		# add 'year' to 'reference period'(month) for full date
    df['date'] = pd.to_datetime(df['date'])						# convert 'date' string to date format
    df['Value'] = df['Value'].apply(to_float)					# convert 'Value' column to float

    fig, ax = plt.subplots()
    df.plot(x='date', y='Value', style='-', figsize=(15,8), ax=ax)
    plt.xlim(pd.Timestamp('1989-01-01'), pd.Timestamp('2002-12-31'))
    
    # Save plot to '/plots' directory
    #plt.show(); 
    path_to_dir = os.path.join(os.getcwd(), '.', 'plots/') 
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)
    fig.savefig(path_to_dir + '1989-2002_Values.png'); plt.close(fig)
    
    return df

    
    
def part_3a(df):
    
    df_2017 = df[(df['date'] > '2017-1-1') & (df['date'] <= '2017-12-31')]		# filter 2017 values
    dates = list(df_2017['date'])
    x = np.arange(0, len(df_2017.index))
    y = df_2017['Value']
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)		# calculate linear reg
    line = slope*x + intercept													# linear reg line  
    return x, y, line, dates


def part_3b(line, dates):
    
    
    
    print('-'*15 + " LINEAR REGRESSION PREDICTIONS " + '-'*15 + '\n')
#     for i in range(len(line)):
#         print("Date: " + dt.datetime.strftime(dates[i], '%b, %Y') + "\t Prediciton: " + str(line[i]))
    print(tabulate([dates, line], headers=['Date', 'Prediction'], tablefmt='orgtbl'))
    nov_pred = line[len(line) - 2]						#extract Nov point from linear reg. line
    print("\nPREDICTION VALUE FOR NOV-2017: \t", str(nov_pred))
    return



def part_3c(df):
    return df

def part_3d(df):
    return df

def part_3e(x, y, line):
    fig = plt.figure(figsize=(15,8))
    plt.plot(x, y,'-', x, line)
    #plt.show();
    path_to_dir = os.path.join(os.getcwd(), '.', 'plots/')
    fig.savefig(path_to_dir + 'Line_Reg.png'); plt.close(fig)
    return


def to_float(x):
    num = x.replace(",", "")
    return float(num)


def to_dataframe(file_name):
    json_df = pd.read_json(os.getcwd() + "/" + file_name)	# read json file to dataframe
    return json_df['data'].apply(pd.Series)					# turn 'data' column into its own dataframe


if __name__ == "__main__":
    file = 'data.json'
    df = to_dataframe(file)
    df 					= part_2a(df)
    x, y, line, dates 	= part_3a(df)
    
    part_3b(line, dates)
#     df = part_3c(df)
#     df = part_3d(df)
    part_3e(x, y, line)
    

