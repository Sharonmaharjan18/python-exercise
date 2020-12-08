#Write a program that allows the user to test if it  is possible that one of the three numbers
# he reads is the sum of the other two numbers.
number_one=int(input("Number 1:"))
number_two=int(input("Number 2:"))
number_three=int(input("Number 3:"))
if number_one+number_two==number_three:
    print("This works")
elif number_two+number_three== number_one:
    print('This works')
elif number_three+number_one==number_two:
    print('This works')
else:
    print("This won't work")