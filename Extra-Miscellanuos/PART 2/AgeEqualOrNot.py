my_age = 11

user_age = round(float(input("What is your age? ")), 0)

if(user_age > my_age):
    print("You are older than me")
elif(user_age < my_age):
    print("You are younger than me")
else:
    print("We are of equal age")
