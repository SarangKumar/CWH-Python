## Day 10 - Taking user input

---

The way to make python(or in general anything interactive) is to make it interactiv i.e. make it perfrom some task based on the provided input.

In Python the way to do this is by using `input()` function.

This function always returns string/character value.

```python
a = input()
print(a)

print(type(a)) #<class 'str'>
```

```python
a = input('Enter our name: ') #will give a prompt that is written while taking the input
print(a)
```

```python
a1 = input('Enter first number: ')
a2 = input('Enter second number: ')
print(a1+a2) #ouput: a1a2 and not a1+a2

print(int(a1)+int(a2))
```

---

####More about input

- The type of a1 and a2 are of type string so the above function preforms concatenation.
Another way around this problem - **typecasting**

```python
a1 = int(input('Enter first number'))
a2 = int(input('Enter second number'))
print(a1+a2)
```

- What happends if we preform arithmetic operations on strings

|Operations|Example|Output|Result|
|:---:|:---:|:---|:---|
|`+`|`string1`+`string2`|`string1string2`|Concatation|
|`-`|`string1`-`string2`|Error|unsupported operand type(s) for -: 'str' and 'str'|
|`*`|`string1`*`string2`|Error|can't multiply sequence by non-int of type 'str'|
|`/`|`string1`/`string2`|Error|unsupported operand type(s) for /: 'str' and 'str'|

- What happends if we preform arithmetic operations on strings and int

|Operations|Example|Output|Result|
|:---:|:---:|:---|:---|
|`+`|`string1`+`2`|Error|can only concatenate str (not "int") to str|
|`-`|`string1`-`2`|Error|unsupported operand type(s) for -: 'str' and 'int'|
|`*`|`string1`*`2`|`string1string1`|String is repeated for that number of times|
|`/`|`string1`/`2`|Error|unsupported operand type(s) for /: 'str' and 'int'|

---

##### References

- [CWH Python 100 days challenge - Day 10](https://youtu.be/WvG-R-xXouA)
