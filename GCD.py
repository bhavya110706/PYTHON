a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(a)
