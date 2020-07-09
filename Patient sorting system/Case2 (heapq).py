# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 06:38:18 2020
Case TWO HEAPQUEUE
@author: Dani-PC
"""
    
def callnext(queue):
    return heapq.heappop(queue)

def update(queue,time):
    upqueue=[]
    while queue:
        updatepatient = heapq.heappop(queue)
        if time-updatepatient[1][2]<18:
            heapq.heappush(upqueue,(pres[updatepatient[1][1]][0]+(time-updatepatient[1][2])*pres[updatepatient[1][1]][1],updatepatient[1]))
        else:
            #print("Someone is approaching the 4 hour time limit!")
            heapq.heappush(upqueue,(-9999999+updatepatient[1][2],updatepatient[1]))
        if time-updatepatient[1][2]>24:
            pass
            #print ("£10,000 FINE!")
    return list(upqueue)
        
#%%
#PROBLEM 1:  CREATE A PRESENTATION "TABLE"
pres={
     "Loss of Consciousness": (-24,-6),
     "Fits or Seizures":(-30,-7),
     "Chest Pain":(-42,-8),
     "Breathing Difficulties":(-60,-10),
     "Severe Bleeding":(-48,-10),
     "Allergic Reactions":(-12,-3),
     "Burns or Scalds":(-18,-4),
     "Stroke":(-36,-2),
     "Road Traffic Accident":(-54,-5),
     "Broken Arm":(-6,-2)
     }
#   we create a dictionary where we store the information about each possible presentation, 
#we keep the priorities in a tuple where the value on index 0 is the entry priority and the one on
#index 1 is the increase/10mins 

#print(pres["Broken Arm"][0]) #should print 6, the entry priority for broken arm
#%%
#PROBLEM 2: CREATE A PRIORITY QUEUE

import heapq
patients=[]
time=0
closingtime=36
masspatients=10
nomedstaff=1 #number of medical staff available (how many patients are being taken in every 10 minutes)
for i in range(0,masspatients):
    heapq.heappush(patients,(pres["Loss of Consciousness"][0],("Sleeping Giant","Loss of Consciousness",0)))
    heapq.heappush(patients,(pres["Fits or Seizures"][0],("Epileptic guy","Fits or Seizures",0)))
    heapq.heappush(patients,(pres["Chest Pain"][0],("Angry old man","Chest Pain",0)))
    heapq.heappush(patients,(pres["Breathing Difficulties"][0],("Siren","Breathing Difficulties",0)))
    heapq.heappush(patients,(pres["Severe Bleeding"][0],("Sword Eater","Severe Bleeding",0)))
    heapq.heappush(patients,(pres["Allergic Reactions"][0],("Peanut lover","Allergic Reactions",0)))

#we add some patients. the 1st value is their priority, then we have info about them, their name, their problem, and the time they show up
#%%
#PROBLEM 3: UPDATE THE PRIORITY QUEUE


while time<=closingtime:
    print ("-------------------------------")
    print ("TIME:", int(time/6%24),':',time%6*10)
    print ("-------------------------------")
    if time==12:
        print("THE FIRE MAGES ARE FIGHING INSIDE THE HOSPITAL!")
        for i in range(0,masspatients):
            heapq.heappush(patients,(pres["Burns or Scalds"][0],("Pyromancer","Burns or Scalds",time)))
    if time==16:
        print("------Stroke Guys arrived!------")
        for i in range(0,masspatients):
            heapq.heappush(patients,(pres["Stroke"][0],("ababbsadhj","Stroke",time)))
    elif time==20:
        print("-There was a traffic accident!-")
        for i in range(0,masspatients):
            heapq.heappush(patients,(pres["Road Traffic Accident"][0],("Reckless Driver","Road Traffic Accident",time)))
    elif time==5:
        print("-----A brawl has started!------")
        for i in range(0,masspatients*2):
            heapq.heappush(patients,(pres["Broken Arm"][0],("funny guy, no humerus","Broken Arm",time)))
    
    patients=update(patients,time)
    for k in range(0,nomedstaff):
        if patients:
            nxt=callnext(patients)
            print ("NEXT:", nxt[1][0])
            print ("Priority:",-nxt[0])
        else:
            print ("NO ONE LEFT TO CALL") 
    time+=1
#we empty the priority queue and add the patients back with updated priorities.
#every 30 minutes the next patient gets called 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    