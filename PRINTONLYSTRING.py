a=input("enter a string:")
res=" "
for i in a:
    if(i.isalpha()):
        res=res+i
res1=res.capitalize()
print(res)
