#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt


# In[6]:


#processing time of each step
process=list(map(float,input("Start at the 1st process, please enter multiple processing time (hour/unit):").split()))

#Iterating over a list and find the bottleneck
for i in process:
    print (f"processing time is {i} hour/unit.")
process.sort()
#get the seperate bottleneck value
bottleneck=1/(process[-1])
print (f"bottleneck (throughput rate) is: {bottleneck} unit/hour")


# In[7]:


#calculate the critical wip
critical_wip=bottleneck*(sum(process))
print (f"Critical WIP is {critical_wip} unit(s)")

#define the inventory
wip1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
wip2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#calculate the throughput rate pwc
throughput_list1=[]

for x in wip1:
    throughput_pwc=(x*bottleneck)/(critical_wip+x-1)
    throughput_list1.append(throughput_pwc)


#throughput rate in no variation case
throughput_list2=[]
for y in wip2:
    if (y>=critical_wip):
        throughput_no_variation=bottleneck
    else:
        throughput_no_variation=(bottleneck/critical_wip)*y
    throughput_list2.append(throughput_no_variation)
    
#add critical wip element
wip2.append(critical_wip)
throughput_list2.append(bottleneck)
wip2.sort()
throughput_list2.sort()


# In[8]:


#plot the pwc WIP-Throughput rate
x1=wip1
y1=throughput_list1
x2=wip2
y2=throughput_list2

plt.xlabel("Inventory")
plt.ylabel("Throughput rate (unit/hour)")
plt.title("WIP-Inventroy Relationship")
plt.plot(x1,y1,label = "pwc",marker='d')
plt.plot(x2,y2,label = "no variation",marker='o')
plt.legend()


# In[ ]:




