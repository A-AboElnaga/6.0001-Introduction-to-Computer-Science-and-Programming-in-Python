# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:29:36 2021

PSet1, Part C: Finding the right amount to save away

@author: A. Mongy
"""
import math

# User input annual salary, the cost of the home, the semi annual raise perecnt
annual_salary = float(input('Enter your annual Salary: '))
Total_Cost = float(input('Enter the total cost of your dream home : '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))
Margin_of_error = float(input('Enter how close you want to be to the down payment(enter in dollors, typiclly 100:'))

# Needed variables and assumptions
portion_down_payment = 0.25 #the portion of the cost needed for a down payment
Current_Savings= 0.00 #savings at the end of each month
MinSaving =0.00 #Minimum saving possible, nothing is saved
MaxSaving=10000 #Maximun saving possible, all is saved
Gss = (MinSaving + MaxSaving)/ 2 #Guessing the first value
StepsNum= 0 #Number of steps of bisection search counter
annual_salary1= annual_salary #Used to rest the annual salary after a geuss was wrong to start a new geuss
No_months = 0 #Counting Number of months

#Output calculations

while Current_Savings < (portion_down_payment*Total_Cost) or No_months < 36 :  
    portion_saved = Gss/10000 #converts the guess to a decimal to be used in calcualtions
    Current_Savings += Current_Savings*0.04/12 #income from monthly investments
    Current_Savings += portion_saved*annual_salary1/12 #Salary income
    No_months += 1
    if No_months == 36 and abs(Current_Savings - (portion_down_payment*Total_Cost)) <= Margin_of_error: #checking if the guess meets the requirements
          print("")
          print("Here is an estimation based on your data")
          print("Best savings rate:", portion_saved)
          print("You will save", Current_Savings, "in 36 months and you need exactly", (portion_down_payment*Total_Cost) )
          print("Num of Steps of Bisection Search", StepsNum )
          break
    
          
    elif No_months <= 36 and (Current_Savings - (portion_down_payment*Total_Cost)) > Margin_of_error  : #if we saved more than we want then our next guess must be lower than the current 
        annual_salary1= annual_salary #reseting data 
        No_months = 0 #reseting data
        MaxSaving = Gss #Since this guess exceeded what we want to save, we set this as Maximum guess
        Gss = (Gss + MinSaving)/2 #getting a new guess
        Current_Savings= 0.00 #reseting data
        StepsNum += 1  #counting number of guesses we made
    elif No_months >= 36 and (Current_Savings - (portion_down_payment*Total_Cost)) < -Margin_of_error  : #similar to the previous elif but oppisite cases
        annual_salary1= annual_salary
        No_months = 0
        MinSaving = Gss
        Gss = (Gss + MaxSaving)/2
        Current_Savings= 0.00
        StepsNum += 1 
    
    if No_months != 0 and No_months % 6 == 0: #semi-annual salary increase
       annual_salary1 += semi_annual_raise*annual_salary1 
    if Gss >= 9999 and Current_Savings < (portion_down_payment*Total_Cost)  : #checking if it is not possible to save
        print("It is not possible to pay the down payment in three years on this salary.")
        break

