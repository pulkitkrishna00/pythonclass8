a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Enter your choice of operator: ")
if c=='+':
    print("The sum of the numbers is: ",a+b)
elif c=='-':
    print("The difference of the numbers is: ",a-b)
elif c=='*':
    print("The product of the numbers is: ",a*b)
elif c=='/':
    print("The quotient of the numbers is: ",a/b)
else:
    print("Wrong operator input")