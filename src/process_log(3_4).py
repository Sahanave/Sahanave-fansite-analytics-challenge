import pandas as pd
import numpy as np
from collections import Counter
from datetime import datetime
from time import strftime
import heapq
import os, sys
filename='log.txt'
data=pd.read_csv(filename,sep='^\t',header=None)
blocks_file = open('blocked.txt', 'w')
raw_data=[]
time_data=[]
data_column1=[]
data_column2=[]
data_column3=[]
data_column4=[]
data_column5=[]
original={}
def time_format(input_data):
# This is a function to convert timedata format into something like timestamp so
#that it can be processed
#Args:Timedata format
#Output:Timestamp'''    
         indx=[0,0,0]
         check=[0,0,0]
         struct_time=datetime.strptime(str(input_data),'%d/%b/%Y:%H:%M:%S  %z') 
         indx[0]=struct_time.hour
         indx[1]=struct_time.minute
         indx[2]=struct_time.second
         check[0]=struct_time.day
         check[1]=struct_time.month
         check[2]=struct_time.year
         timestamp_of_data=[indx[0],indx[1],indx[2],check[0],check[1],check[1]]
         return timestamp_of_data


def difference(input1, input2):
    #This function calculates the difference between two time stamps
    #Args:Two time stamps
    #Output:Their difference
    index1=[0,0,0]
    index2=[0,0,0]
    check1=[0,0,0]
    check2=[0,0,0]
    index1[0:3]=input1[0:3]
    index2[0:3]=input2[0:3]
    check1[0:3]=input1[3:6]
    check2[0:3]=input2[3:6]
    if(check1==check2):
     time_difference = 3600*(index1[0]-index2[0])+60*(index1[1]-index2[1])+(index1[2]-index2[2])
    else:
     time_differnce='NAN'
    return time_difference
      
#parsing the data into respective columns
for indi,data_row in data.itertuples():
        
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
          column2,sp=column2.split(']')
         except:
             pass
         
         
         
         
    
         data_column1.append(column1)
         data_column2.append(column2)
         data_column3.append(dat2)
         data_column4.append(column5)
         data_column5.append(column6)

raw_data=[data_column1,data_column2,data_column3,data_column4,data_column5]     
         
#Feature 3         
count_times={}
visited=[]
raw_time=[]
window_start=time_format(time_data[0])
raw_time.append(time_data[0])
visited.append(window_start)
for i in range(len(time_data)):
         count_times[time_data[i]]=0 
for i in range(1,len(time_data)):
   diff=0
   for visit in range(len(visited)):
        window_end=time_format(time_data[i])   
        diff=difference(visited[visit],window_end)
        if(diff<3600):
          visit_full=raw_time[visit]
          count_times[visit_full]+=1
        if(diff>3600):
           del visited[visit][0:6]
           del raw_data[visit]
   visited.append(window_end)
   raw_time.append(time_data[i])   
count_times_sorted=OrderedDict(sorted(count_times.items(), key=lambda x: x[1],reverse=True))

count=0;
with open('hours.txt', 'w') as f:
  for s in count_times_sorted:
    website=s;
    if(website!=" "):
      f.write("\n %s" %(website))
      count=count+1
    if(count>=10):
      break   
#Feature 4
data_for_blocking=[data_column1,data_column2,data_column4] 
blocklist={}  
while i <(len(data_for_blocking)):
        index = data_for_blocking[i][0]
        code = data_for_blocking[i][3]
        time_arr=time_format(data_for_blocking[i][2])
        window=20
        if code == '200' and index not in blocklist:
            i += 1
            continue
        elif code == '200' and index in blocklist and difference(blocklist[index][0], time_arr) > window:
            del blocklist[index]
            i += 1
            continue
        elif protocol1 == '200' and index in blocklist and difference(blocklist[index][0], time_arr) < window:
            if blocklist[index][1] >= 3:
                blocks_file.write('\n',raw_data[i])
            i += 1
            continue
        elif protocol1 == '401' and index in blocklist and difference(blocklist[index][0], time_arr) > window:
            del blocklist[index]
            blocklist[index] = [data_for_blocking[i][0], 1]
            i += 1
            continue
        elif protocol1 == '401' and index not in blocklist:
            blocklist[index] = [data_for_blocking[i][0], 1]
            i += 1
            continue
        elif protocol1 == '401' and ip1 in blocklist and difference(blocklist[ip1][0], time_arr) < window:
            tryCount = blocklist[index][1] + 1
            blocklist[index][1] = tryCount
            if tryCount > 3:
              blocks_file.write('\n',raw_data[i])
            i += 1
            continue

        i += 1
           