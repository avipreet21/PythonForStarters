#Lab3

#exercise1
"""This function calculates the average marks of the students."""

def average_mark(midterm1, midterm2):
    average = (midterm1 + midterm2) / 2
    return average

assert average_mark(55, 25) == 40
assert average_mark(80, 60) == 70

#excercise2

""" This function converts marks into percentage"""

def convert_to_percentage(max_marks, your_marks):
    percentage = (your_marks / max_marks) * 100
    return percentage

assert convert_to_percentage(50, 40) == 80
assert convert_to_percentage(60, 54) == 90

#exercise3

""" This function converts marks of two midterms into average percentage"""

def calculate_average(mid1, total1, mid2, total2):
    percentage1 = convert_to_percentage(total1, mid1)
    percentage2 = convert_to_percentage(total2, mid2)
    average_percentage = average_mark(percentage1, percentage2)
    return average_percentage

assert calculate_average(40, 50, 54, 60) == 85
assert calculate_average(5, 10, 5, 10) == 50

#exercise4

""" this function calcualtes the percentage with max 20% """

def final_grade(marks1, max1, marks2, max2):
    percentage_grade = calculate_average(marks1 , max1, marks2, max2) *20/100
    return percentage_grade

assert final_grade(5, 10, 5, 10) == 10
assert final_grade(40, 50, 54, 60) == 17

#exercise5

""" function calculates the surface area of the cone"""

import math
def calculates_area(radius, height):
    area = 3.14 * radius * ( radius + math.sqrt( height**2 + radius**2 ) )
    return area

assert calculates_area(3, 4) == 75.36
assert round(calculates_area(5, 6), 2) == 201.12

#exercise6

"""This function calculates the amount user pay for the cans"""

def calculate_amount(cans):
    price = (cans//3)* 3 *1.25 + (cans%3) * 1.50
    return price

assert calculate_amount(8) == 10.50
assert calculate_amount(10) == 12.75

#exercise8

""" This function tells the user that these geo points are close or not"""
def geo_location( lat1, long1, lat2, long2):
    if lat1 - lat2 < 1 and long1 - long2 < 1 :
        return "These points are close"
    else:
        return "These points are not close"
    
assert geo_location( 30.75, -83.25, 31.25, -82.85) == "These points are close"
assert geo_location( 30.75, 83.25, 31.25, -82.85) == "These points are not close"    



 