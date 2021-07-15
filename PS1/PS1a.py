# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:06:39 2021

PSet1, Part A: House Hunting

@author: A. Mongy
"""
import math

# User input annual salary, portion saved, and the cost of the home
annual_salary = float(input('Enter your annual Salary: '))
portion_saved = float(input('Enter the portion saved each month in decimal form (i.e. 0.1 for 10%) :' ))
Total_Cost = float(input('Enter the total cost of your dream home : '))

# Needed variable assumptions
portion_down_payment = 0.25 #the portion of the cost needed for a down payment
Current_Savings= 0.00 #savings at the end of each month


#Output calc

No_months = 0
while Current_Savings < (portion_down_payment*Total_Cost):
    Current_Savings += Current_Savings*0.04/12
    Current_Savings += portion_saved*annual_salary/12
    No_months += 1
print("Number of months need to save the down payment = ", No_months) 
    
    

