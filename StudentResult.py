#8. WAP to store the marks of N subjects of a student in a LIST and calculate the percentage, average, and grade/division.
# Take max mark is 100. Print Invalid Mark of user input more than 100.
num=int(input('Enter number of subjects :'))
student=[].append(num)
for i in range(0,num):
    student[i]=int(input('Enter mark of subject {0}'.format(i+1)))
print(student)