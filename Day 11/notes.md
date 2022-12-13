## Day 11 - String

String is one of the data types in python(or in any other languages). 

They are enclosed within single quotes or double quotes

Example:

```python
a = 'Hello, world' # or "Hello, world"
print(a) #output: 'Hello, world
```

There are times when uses wants to use single quotes(double quotes) inside a string. To achieve this one should use double quotes(single quotes) and then use single(double) quotes inside.

```python
str1 = "Hi, it's an apple"
str2 = 'No"s'
#both are valid strings
```

#### Indexing in strings

- String is made up of characters. The individual unit is called character. 
    - Example: for string "Hello" the characters are {'H', 'e', 'e', 'l', 'o'}

- Now we can also access these individual strings using indexing.

- Indexing starts from 0 and ends in length of string - 1

```python
name = 'Rohan'
print(name[0]) #'R'
print(name[3]) #'a'

# print(name[10]) #Error: string index out of range
```

- Python also allows you to use negative indexing where the range is from -1 to - length of string. Where characters at index -1 is the last character of the string and the characters at index -length of string is the first character of the string.

```python
name = 'Rohan'
print(name[-1]) #'n'
print(name[-3]) #'h'

# print(name[-10]) #Error: string index out of range
```

#### More about input

- The methods mentioned above are only used for single line strings then what about multiline strings?

Use triple single(double quotes). Using this method also enables you to use double quotes or single quotes

```python
a1 = """ this is a multi
line
string
"""
print(a1)
``` 

- How to get all the characters of the string?

Using loops:

>**Note**
>
>We will study about loops in future sessions

```python
for character in 'string':
    print(character)
```



---

##### References

- [CWH Python 100 days challenge - Day 11](https://youtu.be/kMNFQYArrLg)

- [W3 School - Python Strings](https://www.w3schools.com/python/python_strings.asp)