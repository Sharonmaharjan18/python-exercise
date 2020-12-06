three_digit_number=int(input('Enter a three-digit number:'))
#half=int(input('Half:'))
#double=int(input('Double:'))
#third_power=int(input('Third power:'))
#tenfold=int(input('Tenfold:'))

half=three_digit_number/2
print(half)
double=three_digit_number*2
print(double)
third_power=three_digit_number**3
print(third_power)
tenfold=three_digit_number*10
print(tenfold)

first_number=three_digit_number/10/10
second_number=(three_digit_number/10)%10
third_number=three_digit_number%10


print("The digits are:",int(first_number),int(second_number),int(third_number))