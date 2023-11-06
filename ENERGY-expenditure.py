#Project1
""" This program calculates the total daily estimated energy expenditure of a person by taking six inputs which are weight, height,age,gender
daily calories intake and activity level."""
"""authors - Avipreet Singh"""
"""last modified = October 11, 2022"""
#starts here
"""This prints activity level table(took help from internet) so that user can choose its activity level before puting input"""

a =[[1, 'Sedentary - mostly resting with little or no activity'],
    [2, 'Light - occasional unplanned activity '],
    [3, 'Moderate - daily planned activity such as short jogs, brisk walk'],
    [4, 'Heavy - daily planned workouts']]
 
print ("{:<15} {:<15} ".format( 'level', 'discription'))

for i in a:
    level, discription = i
    print ("{:<15} {:<15} ".format( level, discription))

#first function
    
def weight_kgs(weight_pound):
    """This function will converts weight from pounds to kgs"""
    kgs = weight_pound / 2.2
    return round (kgs, 2)
assert weight_kgs(155) == 70.45
assert weight_kgs(110) == 50.00

#Second function

def height_cms(height_inches):
    """This function converts height from inches to cms"""
    cms = height_inches * 2.54
    return cms

assert height_cms(70) == 177.8
assert height_cms(80) == 203.2

#Third function

def basal_metabolic_rate(weight_pound, height_inches, age, gender):
    """This function calculate the bmr for both men and women by using the first and second function to convert the unit first."""
    weight = weight_kgs(weight_pound)
    height = height_cms(height_inches)
    if gender == "M":
        bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
    if gender == "F":
        bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
    return bmr

assert round(basal_metabolic_rate(155, 70, 47, "M"), 2) == 1600.57
assert round(basal_metabolic_rate(155, 70, 47, "F"), 2) == 1430.46

#Fourth function

def physical_activity(activity_level, weight_pound, height_inches, age, gender):
    """This function calculates the physcial activity on the basis of activity level, given by the user as input. It also uses the fourth function."""
    if activity_level == 1:
        outcome = 0.25 * basal_metabolic_rate(weight_pound, height_inches, age, gender)
    if activity_level == 2:
        outcome = 0.375 * basal_metabolic_rate(weight_pound, height_inches, age, gender)
    if activity_level == 3:
        outcome = 0.55 * basal_metabolic_rate(weight_pound, height_inches, age, gender)
    if activity_level == 4:
        outcome = 0.775 * basal_metabolic_rate(weight_pound, height_inches, age, gender)
    return outcome

assert round(physical_activity(3, 155, 70, 47, "M"), 2) == 880.31
assert round(physical_activity(3, 155, 70, 47, "F"), 2) == 786.75

#Fifth function

def thermal_effect(calories_intake):
    """ This function calculates the thermal effect of the food and calories intake as a input. """
    result = calories_intake * 5/100
    return round(result, 2)

assert round(thermal_effect(2631.56), 2)== 131.58
assert round(thermal_effect(1876), 2) == 93.80

#sixth function

def daily_energy_expenditure(activity_level, weight_pound, height_inches, age, gender, calories_intake):
    """ This function calculates the daily estimated energy expenditure by adding the function third,fourth and fifth."""
    total_energy = basal_metabolic_rate(weight_pound, height_inches, age, gender) + physical_activity(activity_level, weight_pound, height_inches, age, gender,) + thermal_effect(calories_intake)
    return round(total_energy, 2)

assert round(daily_energy_expenditure(3, 155, 70, 47, "M", 2631.56), 2) == 2612.46
assert round(daily_energy_expenditure(3, 155, 70, 47, "F", 1876), 2) == 2311.01


def main():
    """ This program's last step is to take all the inputs from the user"""
    
    weight_pound    = int(input("What is your weight(lbs)?"))
    height_inches   = float(input("what is your height(inches)?"))
    gender          = str(input("what is your gender?(M/F)"))
    age             = int(input("what is your age?"))
    calories_intake = float(input("what is the average calories you consume in a day?"))
    activity_level  = int(input("what is your daily basic activity level? (1-4)"))
    print("your daily energy expenditure is:", daily_energy_expenditure(activity_level, weight_pound, height_inches, age, gender, calories_intake))

if __name__ == "__main__":
    main()
