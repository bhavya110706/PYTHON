lower=int(input("enter a number1:"))
upper=int(input("enter no 2:"))
print("prime numbers between",lower ,"and",upper,"is:")
for i in range(lower,upper+1):
    if i>1:
     for j in range(2,i):
       if(i%j==0):
         break
     else:
         print(i)



'''
lower=int(input("enter a number1:"))
upper=int(input("enter no 2:"))
print("prime numbers between",lower ,"and",upper,"is:")
for i in range(lower,upper+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
    if(count==0):
        print(i,end=" ")
'''
