# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:24:09 2024

Program   triangle.m_mannrw
Author    Raleigh Wilmore Mann
Date      8-27-24
Purpose   program takes three points input in pairs of x and y. 
          It then calculates the length of each side and the area 
          of the triangle between them using Heron's formula.

Notes     The outputs are rounded only for presentation using format strings.
          This ensures the perimeter and area are not affected by early rounding. 
"""

"""
Variables:
    
x1         x of first vertex
x2         x of second vertex
x3         x of third vertex

y1         y of first vertex
y2         y of second vertex
y3         y of third vertex

side12     side of triangle between vertex 1 and 2
side23     side of triangle between vertex 2 and 3
side31     side of triangle between vertex 3 and 1 

x          list of vertex x values
y          list of vertex y values

Perimeter  Perimeter of the triangle
SemPer     Semiperimeter of the triangle
Area       Area of the triangle
"""

#Imports    
import numpy as np
import matplotlib.pyplot as plt

#Verticies input    
x1 = float(input("x1: "))
y1 = float(input("y1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))

x3 = float(input("x3: "))
y3 = float(input("y3: "))

#Sides

#Calculates distance between the points and rounds to two decimal places
side12 = np.sqrt((x2-x1)**2+(y2-y1)**2)
side23 = np.sqrt((x3-x2)**2+(y3-y2)**2)
side31 = np.sqrt((x1-x3)**2+(y1-y3)**2)
print(f'The three side lengths are {side12:.3f}, {side23:.3f}, and {side31:.3f} units long. ')

#Perimiter 
Perimeter = side12 + side23 + side31
print(f'The Perimeter is {Perimeter:.3f} units long.')
#Area


#Semiperimeter
SemPer = Perimeter/2

#Uses Heron's Formula
Area = np.sqrt(SemPer*(SemPer-side12)*(SemPer-side23)*(SemPer-side31))
print(f'The Area of the triangle is {Area:.3f} units^2')

#Plotting

#x1 and y1 are repeated in order to draw the 3-1 side. 
x = [x1,x2,x3,x1]
y = [y1,y2,y3,y1]

#Plots triangle
plt.plot(x,y,'--c')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle')
