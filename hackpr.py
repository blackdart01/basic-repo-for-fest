#game started

i=int(input("enter no of issues:"))
print("enter list:")

a=[]

for j in range(i):
    a[j]=int(input())

x=0

for j in range(i):
    if a[j]%2==0 and j%2==0:
        print("valid password")
        x+=1
    else:
        print("")

print("result = ")

#game over