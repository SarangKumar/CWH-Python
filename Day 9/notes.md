## Day 9 - Typecasting

Typcasting means conversion of one data type to another expectly.

Python has varity of built-in functions/methods(in terms of OOP) to do this task.

| Function  | Job                      |
| :-------: | :----------------------- |
|  `str()`  | to convert to string     |
|  `ord()`  | to get the ascii value   |
|  `hex()`  | to conver to hexadecimal |
|  `oct()`  | to convert to octal      |
|  `int()`  | to convert to int        |
| `float()` | to convert to float      |
| `tuple()` | to convert to tuple      |
| `list()`  | to convert to list       |
|  `set()`  | to convert to set        |
| `dict()`  | to convert to dictionary |

```python
a = '50'
b = '3'
print(a + b) #503

# how to get around this issue
print(int(a) + int(b))

a = 50
b = 3
print(a + b) #53
```

>**Note**
>
>Keep in mind that conversion should be valid.

```python
#Example for valid conversions
print(int('1'+int('23')))
print(int('12313')+23)

#Example for invalid conversions
print(int('my name'))
```

#### Types of typecasting

- **explicit type casting** Manually changing the type of data.
- **implicit type casting** Python does typecasting automatically. Datatypes in Python doesn't have the same order. So while performing operations involving different data types the datatypes may change to hight level data types

```python
#Explicit type casting
print(list((1, 2, 3)))

#Implicit type casting
print(1.2+3) # results in float type, 3->3.0
```

---

##### References

- [CWH Python 100 days challenge - Day 9](https://youtu.be/Pu5bqySSSS0)
