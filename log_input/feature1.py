#the first step would be import the dataset
import pandas as pd
import numpy as np
from collections import Counter
filename='log.txt'
data=pd.read_csv(filename,sep='^\t',header=None)
raw_data=[]
data_column1=[]
data_column2=[]
data_column3=[]
data_column4=[]
data_column5=[]
#parsing the data into respective columns
for index,data_row in data.itertuples():
        
         try:
          dat1,dat2,dat3=data_row.split('"')
         except:
            pass
         try:
           co1,column2=dat1.split('[')
         except:
            pass
         try:
            column1,column=co1.split('- -')
         except:
            pass
         try:
           sp,column5,column6=dat3.split(' ')
         except:
            pass
         data_column1.append(column1)
         data_column2.append(column2)
         data_column3.append(dat2)
         data_column4.append(column5)
         data_column5.append(column6)
raw_data=[data_column1,data_column2,data_column3,data_column4,data_column5]       
#counting in descending order the top 10 most active hosts/IP addresses that have accessed the site.    
#feature 1
frequency_websites=Counter(data_column1).most_common(10)
filename='host.txt'
with open(filename, 'w') as f:
     for s in frequency_websites:
         website,website_frequency=s;
         f.write("%s , %s \n " % (website,website_frequency))


   