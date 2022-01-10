#7. WAP to check whether a number is a palindrome or not.
#    A number is said to be palindrome if the reverse of the number is equal to itself.
num=int(input('Enter a number:'))
temp=num
rev=0
while num!=0:
    rem=num % 10
    rev=rev*10+rem
    num//=10
if rev == temp:
    print(temp,'is a palindrome number')
else:
    print(temp,'is not a palindrome number')