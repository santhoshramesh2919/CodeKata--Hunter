# First repeted element...
n=int(input())
li=list(map(int,input().split()))
li2=[]
for i in li:
    if i in li2:
        print(i)
        break
    else:
        li2.append(i)
else:
    print("unique")
