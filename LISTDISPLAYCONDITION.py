student=["ANU","ANI","BALA","RAVI","RAJU","JACK"]
cgpa=[56,66,47,88,78,69]
arrear=[0,2,3,2,0,0]
for i in range(6):
    if arrear[i]==0 and cgpa[i]>60:
        print(student[i])
