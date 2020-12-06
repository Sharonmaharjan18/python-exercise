yes=int(input("How many people voted YES:"))
no=int(input("How many people voted no:"))
blank=int(input("Number of blank votes:"))

total=int(yes+no+blank)
#print(total)
yes_voted=yes/total*100
no_voted=no/total*100
blank_voted=blank/total*100

print('Yes:',yes_voted,"%")
print('No:',no_voted,"%")
print('Blank:',blank_voted,"%")