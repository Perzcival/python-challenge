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

with open("BankResults.txt",'w') as F:
	
        print(f"Total Months:{months}" ,file = F)

        print(f"Total:{total}",file = F)

        print(f"Average Change:{Avg_Change}:0.00",file = F)

        print(f"Greatest Increase in Profits:{most_date,most}",file = F)
    
        print(f"Greatsest Decrease in Profits:{least_date,least}",file = F)
        