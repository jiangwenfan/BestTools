
num = [9,2,7,3,4,1,5,6,8]

print("initial---------"+str(num))

t = len(num)-1 #趟数

for i in range(t):
    for j in range(len(num)-1-i):
        if(num[j]>num[j+1]):
            num[j],num[j+1] = num[j+1],num[j]
        j+=1
    print("每趟: "+str(num))

print("result:-------"+str(num))
