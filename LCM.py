a = int(input("enter no 1: "))
b = int(input("enter no 2: "))
temp_1= a
temp_2=b
while(b!= 0):
    rem=a%b
    a=b
    b=rem
lcm = (temp_1*temp_2)//a
print(lcm)
