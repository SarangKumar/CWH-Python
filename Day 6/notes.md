## Day 6 - Variable & Data Types

---

#### Variable

Variables are like containers that stores data in them. Now the stores data they can be accessed using these variables. These variables are stored in RAM.

##### Rules for Python variables:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive

**Syntax**

```python
a = 10
print(a)
# print(A) #error - As a and A are differently treated(case-sensitive)
b = "Python"
print(b)
c = None
print(c)
d = true
print(d)
```

##### More to know

```python
a1 = "first_name"
a2 = "second_name"
b1 = 12
b2 = 23
print(a1+a2) #valid
print(b1+b2) #valid
# print(a1+b1) #error -- since the datatypes of both are different
```

```python
# How to get the type of data(which maybe stored in a variable)
print(type("name"))

a = 100
print(type(a))
```

---

#### Data Types

Data are categoried into various types depending on it's nature and tha actions that can be performed with them. These are different types of values that a variable can store

Python has some built in data types

|    Category    | Data Type                         ||
| :------------: | :-------------------------------- |:---|
|   Text Type    | `str`                             |<ul><li>str: "This is a string", "Name"</li></ul>
|  Numeric Type  | `int`, `float`, `complex`         |<ul><li>int: 3, -2, 0</li><li>float: 7.356</li><li>complex: 4-3i</li></ul>
| Sequence Types | `list`, `tuple`, `range`          |<ul><li>list: [1, 2, -12.22, ["apple", "banana"], "string"]</li><li>tuple: ("element1", -2, 12e2, ("apple"), ['mango'])</li><li>range: </li></ul>|
|  Mapping Type  | `dict`                            |<ul><li>dict: {name: "first1", age: 20}</li></ul>|
|   Set Types    | `set`, `frozenset`                |<ul><li>set: {"value1", "value2", 3}</li></ul>
| Boolean Types  | `bool`                            |<ul><li>bool: false, true</li></ul>|
|  Binary Type   | `bytes`, `bytearra`, `memoryview` |
|   None Type    | `None`                            |<ul><li>None: None</li></ul>|

>*In Python everything is `object`, any data type is `object`*
>*You do not need to rememeber the list*

*We will be exploring all of these afterwards*


---

##### References

- [CWH Python 100 days challenge - Day 6](https://youtu.be/ORCuz7s5cCY)
- [W3 School - Python Variables](https://www.w3schools.com/python/gloss_python_variable_names.asp)

- [W3 School - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
