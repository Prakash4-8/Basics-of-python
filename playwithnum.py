# Subtract the Product and Sum of Digits of an Integer
x= int
input("Enter the number")
temp=x
while(len(x)!=0):
    rem=x%10
    x=x/10
    sum=sum+rem
print(sum)