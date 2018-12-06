
# coding: utf-8

# In[22]:


""" -------------------------------------------------------------------------------------------------------
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ APPLIED DATA SCIENCE: FINAL PROJECT! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    -------------------------------------------------------------------------------------------------------
        
                        # =================== Final Project: Parts 2 & 3 ====================
                        # ============ Author: Savannah McCoy, Azeezah Muhammad =============
                        # ================ Howard University -- Fall 2018 ===================
                        # ================ CSCI 473: Applied Data Science ===================

"""

try:
  import os, sys, json, math, time
  import matplotlib.pyplot as plt
  import pandas as pd
  import numpy as np
  import datetime as dt
  from scipy import stats
  from prettytable import PrettyTable
except ImportError as e:
  # work around for Mac OS
  if str(e).startswith('Python is not installed as a framework. The Mac OS X backend will not'):
    import matplotlib as mpl
    mpl.use('TkAgg')
    import os, sys, json, math, time
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import datetime as dt
    from scipy import stats
    from prettytable import PrettyTable

    
def part_2a(df):
    
    df['date'] = df['reference_period_desc'] + df['year']		# add 'year' to 'reference period'(month) for full date
    df['date'] = pd.to_datetime(df['date'])						# convert 'date' string to date format
    df['Value'] = df['Value'].apply(to_float)					# convert 'Value' column to float

    fig, ax = plt.subplots()
    df.plot(x='date', y='Value', style='-', figsize=(15,8), ax=ax, color='xkcd:aqua')
    plt.xlim(pd.Timestamp('1989-01-01'), pd.Timestamp('2002-12-31'))
    plt.title('1989 - 2002 Turkey Slaughters')
    plt.xlabel('Year')
    plt.ylabel('Number of Turkeys')
    #plt.show()
    path_to_dir = os.path.join(os.getcwd(), '.', 'plots/') 		# Save plot to '/plots' directory
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)
    fig.savefig(path_to_dir + '1989-2002_Values.png'); print(".........Part 2a Plot Saved!\n"); plt.close(fig)
    return df

def part_2c(df):
    dfy = df.groupby('year')
    means = [df[1]['Value'].mean() for df in dfy]
    medians = [df[1]['Value'].median() for df in dfy]
    
    t = PrettyTable()
    t.add_column(column=sorted(map(int, dfy.groups.keys())), fieldname='Year') 
    t.add_column(column=means, fieldname='Mean')
    t.add_column(column=medians, fieldname='Median')
    print(t)

def part_3a(df):
    df_2017 = df[(df['date'] > '2017-1-1') & (df['date'] <= '2017-12-31')]		# filter 2017 values
    
    x = np.arange(0, len(df_2017.index))
    y = df_2017['Value']
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)		# calculate linear reg
    line = slope*x + intercept													# linear reg line  
    return x, y, r_value, line, df_2017


def part_3b(line, df_2017):
    
    dates = list(df_2017['date'])
    form_dates = [dt.datetime.strftime(date, '%b, %Y') for date in dates]		# format date objects to nice strings
    
    print("-----------------------------")
    print("LINEAR REGRESSION PREDICTIONS")

    t = PrettyTable()															# tabulate line reg predictions
    t.add_column(column=form_dates, fieldname='Date') 
    t.add_column(column=line, fieldname='Predicted Slaughters')
    print(t)
    nov_pred = line[len(line) - 2]												# extract Nov point from linear reg. line
    print("\nPREDICTION VALUE FOR NOV-2017:\t", str(nov_pred))
   
    return


def part_3c(line, df_2017):
    
    real_vals = list(df_2017['Value'])				
    real_val = real_vals[len(line) - 2]				# extract real value for Nov point from dataframe
    nov_pred = line[len(line) - 2]					# extract Nov point from linear reg. line
    abs_err = abs(real_val - nov_pred)				# calculate absolute error
    print("ABSOLUTE ERROR:\t\t\t", str(abs_err))
    
    return real_val, nov_pred



def part_3d(r_value):
    print("R_SQUARED VALUE:\t\t", r_value**2)



def part_3e(x, y, line):
    fig = plt.figure(figsize=(15,8))
    l1, l2 = plt.plot(x, line,'--', x, y)								# plot everthing on the same figure
    plt.title('Turkey Slaughters in 2017')
    plt.xlabel('Month')
    plt.ylabel('Number of Turkeys')
    plt.xticks(x, ["Feb", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    plt.setp(l1, linewidth=2, color="xkcd:aquamarine")  # line1 is thick and red
    plt.setp(l2, linewidth=1, color='xkcd:turquoise')  # line2 is thinner and green
    path_to_dir = os.path.join(os.getcwd(), '.', 'plots/')	# Save to plots folder
    fig.savefig(path_to_dir + 'Line_Reg.png'); print("\n.........Part 3e Plot Saved!"); plt.close(fig)
    return


def to_float(x):											#helper function to remove commas from Value strings
    num = x.replace(",", "")
    return float(num)


def to_dataframe(file_name):
    json_df = pd.read_json(os.getcwd() + "/" + file_name)	# read json file to dataframe
    return json_df['data'].apply(pd.Series)					# turn 'data' column into its own dataframe

def analyze():
    print("\n" + "="*25 + " APPLIED DATA SCIENCE: FINAL PROJECT " + "="*25 + "\n")
    
    start = time.time()
    
    filepath = 'data.json'
    df = to_dataframe(filepath)
    df = part_2a(df)
    x, y,  r_value, line, df_2017 = part_3a(df)
    part_2c(df)
    part_3b(line, df_2017)
    part_3c(line, df_2017)
    part_3d(r_value)
    part_3e(x, y, line)
    
    end = time.time()
    print("\n" + "="*35 + " Done Processing Data " + "="*35 + "\n")
    print("TOTAL ANALYSIS TIME: " + str(dt.timedelta(seconds=(end - start))))
    

