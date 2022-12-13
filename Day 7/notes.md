## Day 7 - Exercise 1 : Calculator

---
<!-- ## Expression

Expressions are a part of code that gives some useful output -->

## Operators

These are symbols that used to join (generally) 2 or more operands and performs some action on those.

#### Arithmetic Operators

| Operators | Description                  | Example |
| :-------: | :--------------------------- | :------ |
|    `+`    | Addition                     | `3+2`   |
|    `-`    | Subtraction                  | `3-2`   |
|    `*`    | Multiplication               | `3*2`   |
|   `**`    | Exponentiation (ES2016)      | `3**2`  |
|    `/`    | Division                     | `3/2`   |
|   `//`    | Floor Division               | `3//2`  |
|    `%`    | Modulus (Division Remainder) | `3+2`   |

```python
a = 10
b = 3
print("a+b= ", a + b)
print("a-b= ", a - b)
print("a/b= ", a / b)
print("a*b= ", a * b)
print("a**b= ", a ** b)
print("a%b= ", a % b)
```

## Exercise 1 - Create a Calculator

Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!


#### Solution
This includes some advace topics that are not covered in the lessons yet 😅. Sorry for that.

```python
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# o = input("Enter the operator: ")

# Hardcoded values
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
```

---

##### References

- [CWH Python 100 days challenge - Day 7](https://youtu.be/FLVqcxnJP_E)