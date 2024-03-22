# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:28:27 2024

@author: mitch_ct6va4o
"""
import os
import csv

budget_data = os.path.join("PyBank/Resources/budget_data.csv")

Total_Number_of_Months=[]
Avg_Change = 0
most = 0
least = 0
total= 0
number= 0
value= 0
row_count=0
most_date=[]
least_date=[]
date=[]



with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
   
    print(csv_reader)
    
    csv_header = next(csvfile)
    
    print(f"CSV Header: {csv_header}")

        
    for row in csv_reader:
        
        print (row[0],int(row[1]))                     
        
        row_count=row_count+1
        
        value = int(row[1])        
        
        date= row[0]
    
        months= row_count
        
        
        if most < value:
           
            most = value 
            
            most_date = date
            
        elif least >= value:
            
            least = value
            
            least_date=date
            
        if int(row[1]) !=0:

            number= value + number
            
            total = number
            
            Avg_Change=(number/months)
    
    print(f" Total Months:{months}")

    print(f"Total:{total}")

    print(f"Average Change:{Avg_Change}:0.00")

    print(f"Greatest Increase in Profits:{most_date,most}")
    
    print(f"Greatsest Decrease in Profits:{least_date,least}")
        

#================================================================================================


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
        
    print(f" Total Votes:{Total_Votes}")

    print(f"Charles Casper Stockham:{Votes_1_Per:0.00%},{Votes_1}")

    print(f"Diana DeGette:{Votes_2_Per:0.00%},{Votes_2}")

    print(f"Raymond Anthony Doane:{Votes_3_Per:0.00%}{Votes_3}")
    
    print(f"Winner:{Winner}")
        


