# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:51:58 2024


program: Fibbonacci.py
@author: Raleigh Mann
date: 8-30-24
purpose: To print out n values of the fibbonacci sequence

Variables:
NumFib:  The index of the target term in the fibbonacci sequence
NumFiO: The original input of NumFib before NumFib is decremeted. 
Num1: Fn      first number of sequence
Num2: Fn+1    second number of sequence
summed: The placeholder sum of the first two numbers
Fiblist: List of all Fibbonacci Values
FibFlag: A flag to switch between all values or just the final value of the sequence
"""
#Asks for number of values
NumFib = int(input("What value of the fibbonacci sequence would you like? "))
NumFibO = NumFib

#Asks if All values or just the final are requested
FibFlag = input("Would you like only the 'FINAL' value or 'ALL'? ")

#Initializes Fn and Fn+1
Num1 = 0
Num2 = 1

#Sum of the first two variables
summed = 1
Fiblist = [Num1 , Num2]


#Clears special cases when asking for the first or first two values
if NumFib == 1:
    Fiblist = [0]
elif NumFib == 2: 
    Fiblist
else:
    #Loop runs the fibbonacci sequence and appends each new value to the Fiblist
    while NumFib > 2: 
        summed = Num1 + Num2
        Fiblist.append(summed)
        Num1 = Num2
        Num2 = summed
        NumFib-=1
    
#Switches what is printed based on FibFlag    
if FibFlag == "ALL":
    print(f'The first {NumFibO} values of the Fibbonacci squence are {Fiblist}')
elif FibFlag == "FINAL":
    print(f'Value {NumFibO} of the Fibbonacci sequence is {summed}')
else:
    print("Please input FINAL or ALL.")