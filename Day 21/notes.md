## Day 28 - Function Argument in Python

Functions make the code reuseable but almost everytime we need to pass parameter to it. We want to make the function more dynamic and not rigid to give the same output every time it is called.

There are 4 types of arguments that can be provided in the function.
- Default Arguments
- Keyword Arguments
- Required Arguments
- Variable Arguments

#### Default Arguments

We can provide a function with some default value so that if no argument is passed on to the function then it will use the default values else will use the given values and hence also doesn't raise any error.

```python
def average(a=10, b=20):
    print('The average is', (a+b)/2)

average()
average(1,2)
```

Output

```shell
The average is 15.0
The average is 1.5
```

#### Keyword Arguments

We can provide arguments with key=value, this way the interpreter can recognise the arguments by the paramater name. Hence, the order in which the argumetns are passed doesn't matter.

```python
def hi(fname, mname, lname):
    print('Hi', fname, mname, lname)

hi('Aditya', 'Roy', 'Kapoor')
hi('Aditya', lname='Kapoor', mname='Roy')
hi(lname='Kapoor', mname='Roy', fname='Aditya')
```

Output
```shell
Hi Aditya Roy Kapoor
Hi Aditya Roy Kapoor
Hi Aditya Roy Kapoor
```


#### Required Arguments

In case we don't pass the arguments with a key=value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual functional definition.

```python
def pricing(items, price):
    print('Your purchase of',items,'items costs Rs',price)

pricing(5,100)
```

Output
```shell
Your purchase of 5 items costs Rs 100
```

#### Variable Arguments

Sometimes we may need to pass more arguments then those defined in the actual function. this can be done using variable-length arguments.

There are 2 ways to achieve it:

**Arbitary Arguments**

While creating a function, pass a `*` before the parameter name while defining the function. the function accessed the arguments by processing them in the form of `tuple`. 

```python
def varAvg(*numbers):
    print(numbers, type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print(sum)
varAvg(1,2,3,3,5)
```

Output
```shell
(1, 2, 3, 3, 5) <class 'tuple'>
14
```

**Keyword Arbitary Arguments**

While creating a function, pass a `*` before the parameter name while defining the function. the function accessed the arguments by processing them in the form of `dictionary`.

*dictionary will be discussed in later lessons*

```python
def name(**name):
    print(name, type(name))
    print('Hello👋', name['fname'], name['mname'], name['lname'])

name(fname='Neel', mname='Nitin', lname='Mukesh')
```

Output
```shell
{'fname': 'Neel', 'mname': 'Nitin', 'lname': 'Mukesh'} <class 'dict'>
Hello👋 Neel Nitin Mukesh
```


Click [here](/Day%2021/main.ipynb) for more examples on Functional Arguments

---

#### References

- [CWH Python 100 days challenge - Day 21](https://youtu.be/0d6b6fFuCkE)
