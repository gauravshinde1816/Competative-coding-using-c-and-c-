n =int(input("enter the number"))
a,b=0,1
sum=0
for i in range(n):
    if i<=1:
        print(i , end=" ")
    sum=a+b
    a=b
    b=sum
    print(sum , end=" ")
