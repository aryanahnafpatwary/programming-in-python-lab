N=int(input("Enter N: "))
a=0
b=1
output=""
while a<N:
    output=output+str(a)+" "
    c=a+b
    a=b
    b=c
print("Fibonacci sequence:", output)