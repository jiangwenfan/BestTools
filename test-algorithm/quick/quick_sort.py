
num = [4,9,2,7,3,8,5,6,1]

def fenqu(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right]>=tmp:
            right -= 1
        #print("")
        #li[right]<tmp
        li[left]=li[right]
        while left < right and li[left]<=tmp:
            left +=1
        #li[left]>tmp
        li[right]=li[left]
    #left = right
    li[left]=tmp
    print("--1--")

print("-----"+str(num))
fenqu(num,0,len(num)-1)
print("-----"+str(num))
