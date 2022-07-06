weight = round(float(input("Enter your weight in kilograms: ")), 2)
height = round(float(input("Enter your height in metres: ")), 2)
BMI = round(weight/(height * height), 2)

print("Your BMI is: ", BMI)

if(BMI <= 18.5):
    print("You are UNDERWEIGHT")
elif(BMI > 18.5 or BMI <= 18.5):
    print("You have NORMAL WEIGHT")
elif(BMI > 18.5 or BMI <= 29.9):
    print("You are OVERWEIGHT")
else:
    print("You are OBESE")
    
