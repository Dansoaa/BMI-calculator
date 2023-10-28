# A simple Python program to calculate BMI


#Get the user's weight and height 
weight=float(input("Enter your weight in kilograms: ")) 
height = float(input("Enter your height in meters: ")) 

# Calculate the BMI 
bmi = weight / (height * height) 

# Print the BMI to the console
print("Your BMI is:", bmi) 

# Interpret the BMI
if bmi < 18.5:    
     print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:    
     print("You are a healthy weight.")
elif bmi >= 25 and bmi < 30:     
     print("You are overweight.")
elif bmi >= 30:    
     print("You are obese.")