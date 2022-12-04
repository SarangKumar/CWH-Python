# Arithmetic operators
# ----------------------------------

print(3+2) #addition operator
print(3-2) #subtraction operator
print(3*2) #multiplication operator
print(3/2) #division operator
print(3//2) #floor division
print(3%2) #modulus operator
print(3**2) #power operator

# ----------------------------------

a = 4
b = 3
o = '+'

if(o=='+'):
    print("The addition of",a, 'and', b, "is", a+b)
elif(o=='-'):
    print("The subtraction of",a, 'and', b, "is", a-b)
elif(o=='*'):
    print("The multiplication of",a, 'and', b, "is", a*b)
elif(o=='/'):
    print("The division of",a, 'and', b, "is", a/b)
else:
    print("Operation not valid")