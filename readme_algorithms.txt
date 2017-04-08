Objective:
  The objective of the report or as I call it my 'thought-flow' is make sure the reader 
  understands the code and the algorithmwhich went behind it so that they could use the code,improve the complexity of my code or 
  have a healthy discussion about better algorithm to implement.I have also included 
  future works section to note what could be done.I also hope to help first timers 
  who wish to get their hands deep in datasciene not to get overwhelmed by the problem but
  have a place to start and work from.
Feature 1:
Ques:List in descending order the top 10 most active hosts/IP addresses that have accessed the 
site.Write to a file, named hosts.txt, the 10 most active hosts/IP addresses in 
descending order and how many times they have accessed any part of the site.
There should be at most 10 lines in the file, and each line should include the host 
(or IP address) followed by a comma and then the number of times it accessed the site.
Algorithm:
 (1)This exercise is very simple,
 (2)Parse the dataset given and use Counter which helps us to find out the frequency of
 repeated websites which access the code and select the top 10.
 (3)This is saved to the file hosts.text
 ---------------------------------------------------------------------------------------
Feature 2
Ques:Identify the top 10 resources on the site that consume the most bandwidth. 
Bandwidth consumption can be extrapolated from bytes sent over the network and
 the frequency by which they were accessed.These most bandwidth-intensive resources,
  sorted in descending order and separated by a new line, should be written 
  to a file called resources.txt.
  
  Algorithm:
  (1)This exercise is slightly tricky but simple.
  (2)Parse the dataset given.
  (3)The reason I said slightly tricky is because if you dont choose 
  the right datastructure you are looking at a complicated problem.
  (4)You use Dictionary.This offers the idea of key (which would be your
  resource) and value(you keep updating this)pair.
  (5)Then you pick the top 10.
----------------------------------------------------------------------------------------
Feature 3
Ques:List in descending order the site’s 10 busiest (i.e. most frequently visited) 60-minute period.
Write to a file named hours.txt, the start of each 60-minute window followed by the
 number of times the site was accessed during that time period. The file should contain 
 at most 10 lines with each line containing the start of each 60-minute window, followed 
 by a comma and then the number of times the site was accessed during those 60 minutes. 
 The 10 lines should be listed in descending order with the busiest 60-minute window
  shown first.
  Algorithm:
   (1)Parse the data
   (2)The idea is have a sliding window and the minute you encounter a index in which
   one of the member of the sliding window is far from the index you dont consider the 
   element to be a part of the window anymore.
   (3)This is valid to files like ours where the data is indexes with respect to time.
    (4)You store the counts in a dictionary and pick the top 10.
-----------------------------------------------------------------------------------------
Feature 4
Ques:List in descending order the site’s 10 busiest (i.e. most frequently visited) 60-minute period.
Write to a file named hours.txt, the start of each 60-minute window followed by the
 number of times the site was accessed during that time period. The file should contain 
 at most 10 lines with each line containing the start of each 60-minute window, followed 
 by a comma and then the number of times the site was accessed during those 60 minutes. 
 The 10 lines should be listed in descending order with the busiest 60-minute window
  shown first.
  Algorithm:
   (1)Parse the data
   (2)The idea is have a sliding window and the minute you encounter a index in which
   one of the member of the sliding window is far from the index you dont consider the 
   element to be a part of the window anymore.
   (3)This is valid to files like ours where the data is indexes with respect to time.
    (4)You store the counts in a dictionary and pick the top 10.
        
    
  
  
  
  
    
   
   