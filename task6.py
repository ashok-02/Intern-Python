l1=list(range(1,11))
print(f"list:{l1}")
l1=[i+2 for i in l1]
print(f"after updating the list:{l1}")

#pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

#fibonacci series
a,b,s=0,1,0
n=int(input("Enter the no of terms"))
for i in range(i,n+1):
    print(s,end=" ")
    a=b
    b=s
    s=a+b

#Armstrong number
print("Amrstrong");
def arm(n):
    z=list(n);
    m=[int(i) for i in z]
    y=int(n);
    x=0;
    for i in m:
        x=x+(i**3)
    if(x==y):
        print(f"{y} is an armstrong number");
    else:
        print(f"{y} is not an armstrong number");
q=input("enter a number to check armstrong possibility");
arm(q);

#Multiplication table of 9
i=9
for j in range(1,11):
    print(f"{i}*{j}={i*j}")

#To check whether a no. is positive or negative
n=int(input("Enter a number"))
if n > 0: print("Positive")
else : print("Negative")

#convert no.of days to ages
def ages(days):
    year=int(days/365)
    print(year)
    print("years")
ages(int(input("enter the number of days:")))

# trignometry
import math as m
a=m.sin(1/4)
b=m.cos(1/4)
sum = a**2+ b**2
print("trignometry")
print(round(sum,5))

#Simple calculator
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=input("Select the operator:*,+,-,/")
if c=='*':print(f"{a}*{b}={a*b}")
elif c=='/':print(f"{a}/{b}={a/b}")
elif c=='+':print(f"{a}+{b}={a+b}")
elif c=='-':print(f"{a}-{b}={a-b}")
