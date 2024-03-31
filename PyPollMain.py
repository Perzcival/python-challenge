# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:28:27 2024

@author: mitch_ct6va4o
"""
import os
import csv

budget_data = os.path.join("PyPoll/Resources/election_data.csv")

Total_Votes=0

Canidate_1 = 'Charles Casper Stockham'
Canidate_2 = 'Diana DeGette'
Canidate_3 = 'Raymon Anthony Doane'

total_1= 0
total_2=0
total_3=0
total_4=0

number= 0

Votes_1= 0
    
Votes_2= 0

Votes_3= 0



with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
   
    print(csv_reader)
    
    csv_header = next(csv_reader)
    
    print(f"CSV Header: {csv_header}")

    for row in csv_reader:

        

        print (row[0],row[1],row[2])                     
    
        
        if  Canidate_1 == row[2]:
           
            Votes_1 = Votes_1 + 1 
            
        if Canidate_2 ==  row[2]:
            
            Votes_2 = Votes_2 + 1 
            
        if Canidate_3 == row[2] :

            Votes_3 = Votes_3 + 1 
        
        if Votes_1 > Votes_2 and Votes_1 > Votes_3:
            Winner=Canidate_1,Votes_1
        
        elif Votes_2 > Votes_1 and Votes_2 > Votes_3:
            Winner=Canidate_2,Votes_2
        
        elif Votes_3 > Votes_2 and Votes_3 > Votes_1:
            Winner=Canidate_3,Votes_3
        
        Total_Votes = Votes_1+Votes_2+Votes_3
            
        Votes_1_Per= (Votes_1/Total_Votes)     

        Votes_2_Per=(Votes_2/Total_Votes)

        Votes_3_Per=(Votes_3/Total_Votes)    


with open("PollMain.txt",'w') as F:
        
    print(f" Total Votes:{Total_Votes}",file = F)

    print(f"Charles Casper Stockham:{Votes_1_Per:0.00%},{Votes_1}",file = F)

    print(f"Diana DeGette:{Votes_2_Per:0.00%},{Votes_2}",file = F)

    print(f"Raymond Anthony Doane:{Votes_3_Per:0.00%}{Votes_3}",file = F)
    
    print(f"Winner:{Winner}",file = F)
        


