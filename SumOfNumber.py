# Program to find the sum of N number using for loop

N = int(input('Enter the value of N: '))

# you will also learn how to use for loop
SUM = 0
for i in range(1, N+1):         # i will start from 1 to N
    SUM += i

print(SUM, "is the sum of first ", N, 'natural numbers')
