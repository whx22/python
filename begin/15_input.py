# int constructor and int function
user_age = int(input("Enter your age: "))
user_age_after_10_years = user_age + 10
print("Your age after 10 years will be: ", str(user_age_after_10_years) + ".")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")