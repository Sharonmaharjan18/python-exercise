"""Write a program that prints the larger of two numbers. If the numbers are negative, then you use the
opposite number.
But: if both numbers are divisible by 5, then you have to print the smaller of both numbers. If both
numbers are equal then the answer is just 0."""
first_number=int(input("First number:"))
second_number=int(input("Second number:"))

if first_number < 0 or second_number < 0:
    if first_number < second_number:
        print("The answers for the numbers", first_number, "and", second_number, "=", first_number)
    else:
        print("The answers for the numbers", first_number, "and", second_number, "=", second_number)

else:
    if first_number == second_number:
        print("The answers for the numbers", first_number, "and", second_number, "= 0")

    elif first_number % 5 == 0 and second_number % 5 == 0:
        if first_number < second_number:
            print("The answers for the numbers", first_number, "and", second_number, "=", first_number)
        else:
            print("The answers for the numbers", first_number, "and", second_number, "=", second_number)

    else:
        if first_number > second_number:
            print("The answers for the numbers", first_number, "and", second_number, "=", first_number)
        else:
            print("The answers for the numbers", first_number, "and", second_number, "=", second_number)