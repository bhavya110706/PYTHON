stud=["BHAVYA","SANGEETHA","RUCHI","JHANVI"]
mark=[[45,56,78,35],[58,39,27,89],[54,63,79,80],[38,97,52,40]]
per=[]
for i in mark:
    d=sum(i)//4
    per.append(d)
for i in range(4):
    print("{}.{}:{}%".format(i+1,stud[i],per[i]))
