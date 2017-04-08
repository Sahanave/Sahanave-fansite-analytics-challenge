#the first step would be import the dataset
import pandas as pd
import numpy as np
from collections import Counter
from collections import OrderedDict
filename='log.txt'
data=pd.read_csv(filename,sep='^\t',header=None)
raw_data=[]
data_column1=[]
data_column2=[]
data_column3=[]
data_column4=[]
data_column5=[]
resources_and_their_bandwidths={}
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
         try:
          dat1,dat2=dat2.split('GET /')
         except:
          pass
         try:
          dat2,temp2=dat2.split('HTTP/')
         except:
             pass
         data_column1.append(column1)
         data_column2.append(column2)
         data_column3.append(dat2)
         data_column4.append(column5)
      
         data_column5.append(column6)
    
raw_data=[data_column1,data_column2,data_column3,data_column4,data_column5]     
###feature 2      
### the top 10 resources on the site that consume the most bandwidth
#resources_and_their_bandwidths_unsorted=[]
for i in range(len(data_column3)):
      if(data_column3[i]!='\ '):
         resources_and_their_bandwidths[data_column3[i]]=0  
for i in range(len(data_column3)):
    if((data_column5[i]!='-')and(data_column3[i]!='\ ')):
       resources_and_their_bandwidths[data_column3[i]]+=int(data_column5[i]) 
       
resources_and_their_bandwidths_sorted=OrderedDict(sorted(resources_and_their_bandwidths.items(), key=lambda x: x[1],reverse=True))
filename='resources.txt'
count=0;
with open(filename, 'w') as f:
  for s in resources_and_their_bandwidths_sorted:
    website=s;
    if(website!=" "):
      f.write("\n %s" %(website))
      count=count+1
    if(count>=10):
      break
    
             

                 