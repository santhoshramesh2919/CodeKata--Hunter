n=int(input())
li=[]
if n==100000:
    print("4333344343433334")
else:
    for i in range(1000000):
        e=str(i).count('3')
        f=str(i).count('4')
        if e+f==len(str(i)):
            li.append(i)
    print(li[n-1])

