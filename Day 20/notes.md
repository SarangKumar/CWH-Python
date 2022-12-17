## Day 20 - Functions

As a programmer there is one saying - DRY (Don't Repeat Yourself). If you find yourself repeating a part of code then it means you are doing it the wrong way. At times there is a need to repeat code. Then what one can do is repeat the code in it's entirety or write a `function` and call it as many times in the function. 

Functions allows programmers to partition the code. There may be some function that does one think and other function can do other work. It also help in debuggin' the code easily. Also during colaboration it makes the work of distributing the code easier.

There are two kinds of function:
- Built-in functions
- User defined functions

#### Buil-in functions

As the name says these are functions that are already written and are just supposed to used. Some example are as follows: `print()`, `list()`, `str()`, `ord()`, `chr()` and many more.

#### User defined functions

Most of the times we need to write our own function so that we can reuse that block of code again in the program. The way how we do it is: 

#### Syntax

```python
# Declaring a function
def function_name(arguments):
    statements

#Calling a function
function_name(arguments)
```

<details>
  <summary><strong>Working</strong></summary>
  
In the above code `def` is a keywork that is used to tell the interpretor that a function is going to be declated. Following that is the name of the function then in the parenthesis we write the arguments(these are those values that we want to operate with in the function, like the numbers are to be added in add function) then we write the statements after colon and proper indentation.

After making a function one must use it, in programming terms it is called calling a function. To call a function one should write the function name and its argument values in brackets.
</details>

For Example:

```python
# Declaring a function
def greaterLesser(a,b):
    if a>b:
        print(a, 'is greater than',b)
    else:
        print(b, 'is greater than or equal to', a)

#Calling a function
greaterLesser(4,3)
```

Output: 
```shell
4 is greater than 3
```

Fo more examples click [here](/Day%2020/main.ipynb)


#### Return

After we are done with the calculation then we may need to store the calcuated value to some variable. For this purpose we use `return`. After the flow of execution encounters return keyword it stops executing any code below that like. *Acts like break in loops*.

For example:

```python
def add(a,b):
    return a+b
new = add(4,3)
print(new)
```

Output:
```shell
7
```


#### More to know

If we want to just declare the functions and not write the complete code then we can do it as follows.

```python
def someFunction():
    pass
```

What the above funcition does is it creates a function and doesn't do anything, cause if we leave it empty then the error will error. Same `pass` can also be used in other cases too - in if else if we want to write some code later then we can do that. 

```python
if(6>3):
    pass
else:
    print('Nothing')
```

Output: 

```shell

```

---

#### References

- [CWH Python 100 days challenge - Day 20](https://youtu.be/dyvxxJSGUsE)