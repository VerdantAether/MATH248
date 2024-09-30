# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:05:10 2024

Program: grade_calc.py
Authors: Raleigh Mann, Grant Fell
Date: 9-26-24
Purpose: To take in the grades of a student, calculate what grade they have before the final
and then determine what grade they need on the final to get a certain course grade.

Variables:
grades_weights_labels: Name of each catagory. 1D array
grades_weights_values: Point weighting of each catagory. 1D array

Student_grades: The percent the student has in each catagory. Initialized as 100. 1D array
Absences: The number of Absences the student has. int

Grade: Holder for the students prefinal grade. float
Letter: The Letter grade that the student has. string

Desired: The grade the student wants in the course. float
Target_Grades: The course grades being tested. 1D array
Required_Grades: The final grades required to get each course grade. 1D array
Grade_p: The grade from everything except the exam 2 and exam 3 catagory. float

Final_catagory: How many points are needed from the exam 2 and exam 3 catagory to get the desired grade. float
Req_final: The required grade on the final to get your desired course grade. float

maxgrade: The course grade obtained with a 100 on the final. float
mingrade: The course grade obtained with a 0 on the final. float

"""
import matplotlib.pyplot as plt


# Imported from MATH 105 Syllabus
grades_weights_labels = ['Attendance', 'Directed Readings', 'Homework and in class', 'Exam 1', 'Exam 2 and Exam 3']
grades_weights_values = [0.06, 0.12, 0.27, 0.15, 0.4]

#Initializes Student with 100 in all catagories
Student_grades = [100.0,100.0,100.0,100.0,100.0]

#Introduce the program
print("This program is used to calculate a students possible course grades and what score is needed on the final to get that. ")
print("Input the students percents (0-100) in each catagory. ")
print()


#Introduce to the weights
print("The Math 105 weights are: ")
for n in range(len(grades_weights_labels)):
    print(f'{grades_weights_labels[n]} : {grades_weights_values[n]*100}%')
print()

# Create a pie chart
plt.pie(grades_weights_values, labels=grades_weights_labels, autopct='%1.1f%%')
plt.title('Grade Weights')
plt.show()

#Import Student_grades
for n in range(len(Student_grades)-1):
    Student_grades[n+1] = float(input(f'What percent do you have in {grades_weights_labels[n+1]}? (0-100): '))
#Ask for absences
Absences = int(input('How many Absences? '))

#Absence piecewise; updates the weighting 
if Absences <= 1: 
    grades_weights_values[0] = 0.06
elif Absences == 2:
    grades_weights_values[0] = 0.04
elif Absences == 3:
    grades_weights_values[0] = 0.02
else:
    grades_weights_values[0] = 0.00
    
#Pre-final calculation
Grade = 0.0
for n in range(len(Student_grades)):
    Grade = Grade + (Student_grades[n]*grades_weights_values[n])

Letter = ''
#Grade to Letter Piecewise
if Grade > 92:
    Letter = 'A'
elif Grade >= 90 and Grade < 92:
    Letter = 'A-'
elif Grade >= 88 and Grade < 90:
    Letter = 'B+'
elif Grade >= 82 and Grade < 88:
    Letter = 'B'
elif Grade >= 80 and Grade < 82:
    Letter = 'B-'
elif Grade >= 78 and Grade < 80:
    Letter = 'C+'
elif Grade >= 72 and Grade < 78:
    Letter = 'C'
elif Grade >= 70 and Grade < 72:
    Letter = 'C-'
elif Grade >= 68 and Grade < 70:
    Letter = 'D+'
elif Grade >= 62 and Grade < 68:
    Letter = 'D'
elif Grade >= 60 and Grade < 62:
    Letter = 'D-'
else:
    Letter = 'F'

#Prints the grade before the final is input
print(f'Your pre-final grade is {Grade}% which is a {Letter}')
print()

#Calculates possible outcomes of the Final Exam
def final_grade (Student_grades,Desired):
    Grade_p = 0
    for n in range(len(Student_grades)-1):
        Grade_p = Grade_p + (Student_grades[n]*grades_weights_values[n])
    
    #Gives four basic outcomes plus the input desired grade.
    Target_Grades = [60,70,80,90,Desired]
    Required_Grades = []
    
    #Loops over each possible grade
    for n in range(len(Target_Grades)):
        Final_category = Target_Grades[n] - Grade_p 
    
        #Calculates the grade on the final required to get your wanted grade
        Req_Final = ((2*Final_category) - Student_grades[4]*grades_weights_values[4])/0.4
        Required_Grades.append(Req_Final)
        
        #If you need more than a 100, the grade is above your range of outcomes.
        if Req_Final > 100.0:
            print(f'Getting a {Target_Grades[n]} is impossible unfortunately. ')
        #If you need less than a 0, the grade is below your range of outcomes.    
        elif Req_Final < 0:
            print(f'Getting a {Target_Grades[n]} is fortunately impossible.')
        #Returns possible grades and what exam result is needed to get them.
        else: 
            print(f'To get a {Target_Grades[n]}, you need a {Req_Final:.3f} on the final.')
     
    #Max and Min possible final grade based on exam outcome.
    maxgrade = ((100 + Student_grades[4])/2)*0.4 + Grade_p
    mingrade = ((0 + Student_grades[4])/2)*0.4 + Grade_p
    print()
    print(f'The minimum grade you can get in this course is a {mingrade:.3f} and the maximum is a {maxgrade:.3f}.')
    
    #Plots the required exam grades for each final grade
    plt.bar(Target_Grades,Required_Grades)
    plt.xlabel("Desired Grade")
    plt.ylabel("Required Final Grade")
    
#Collects Input for what grade you want in the course
Desired = float(input("What is your desired grade for this course? "))
print()
#Calls final_grade
final_grade(Student_grades,Desired)

