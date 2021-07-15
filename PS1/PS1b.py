# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:47:16 2021

PSet1, Part B: Saving, with a raise

@author: A. Mongy
"""
import math

# User input annual salary, portion saved, the cost of the home, and the semi annual raise perecnt
annual_salary = float(input('Enter your annual Salary: '))
portion_saved = float(input('Enter the portion saved each month in decimal form (i.e. 0.1 for 10%) :' ))
Total_Cost = float(input('Enter the total cost of your dream home : '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))

# Needed variable assumptions
portion_down_payment = 0.25 #the portion of the cost needed for a down payment
Current_Savings= 0.00 #savings at the end of each month

#Output calc

No_months = 0
while Current_Savings < (portion_down_payment*Total_Cost) and No_months < 36:
    Current_Savings += Current_Savings*0.04/12
    Current_Savings += portion_saved*annual_salary/12
    No_months += 1
    if No_months != 0 and No_months % 6 == 0:
       annual_salary += semi_annual_raise*annual_salary
print("Number of months need to save the down payment = ", No_months) 
print("You saved ", Current_Savings, "and you ony need to save", (portion_down_payment*Total_Cost) )
    
    

