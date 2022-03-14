import sys
weight = float(input("What is your weight in pounds? "))
height = float(input("What is your height in inches? "))

bmi = ((703 * weight)/(pow(height,2)))
bmi = str(round(bmi))

print("Your body mass index (BMI) is " + bmi + "%")