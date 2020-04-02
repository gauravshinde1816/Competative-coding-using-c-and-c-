# a,b=0,1
# sum=0
# for i in range(n):
#     if i<=1:
#         print(i , end=" ")
#     sum=a+b
#     a=b
#     b=sum
#     print(sum , end=" ")

#fibbonacci sequence using recursion#

# n = int(input("enter the number"))
# def fibbo(n):
#     if n<=1:
       
#         return n

#     else:
#         return (fibbo(n-1)+fibbo(n-2))

# if n<=0:
#     print("enter the valid number")
# else:
#     print("Fibonacci sequence is :")
#     for i in range(n):
#         print(fibbo(i) , end=" ")


#finding factorial of entered number

# n = int(input("enter the number"))
# mul=1
# for i in range(1,n+1):
#     mul =i*mul


# print(mul)

#finding the factorials by using recursion

n = int(input("enter the number"))

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))








        