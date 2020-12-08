#Write a program that allows the user to test whether a positive number greater than 0 ends with a specified final digit.
#When the entered number is negative, you will give a message that the test will not be performed.
number=int(input("Enter a number:"))
if number<0:
    print("Negative numbers will not be tested")
else:
    final_digit = int(input("What final digit do you want to test with:"))
    if number%10==final_digit:
        print(number,"ends with",final_digit)
    else:
        print(number,"does not end with",final_digit)

