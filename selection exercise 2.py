#Write a program that reads the year of birth and then prints whether the user is an adult (at least 18 years old) or not.
# If someone turns 18 this year, you may also consider that person to be an adult.
year_of_birth=int(input("Enter your year of birth:"))
current_year=2020
age=current_year-year_of_birth
print("Your age=",age)
if age>=18:
    print("So you're an adult")
else:
    print("You're not an adult yet.")