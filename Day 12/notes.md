## Day 12 - Slicing in String

---

String is one of the most import and is most widely used data type. So it becomes important to know more about it and knowing what can we do with it.

### Slicing

It refers to cutting or trimming of a string by that what i mean is you can access a sub-string(just a part of the string).

#### Syntax
```python
'string'[start,end,step]
```


Using the above method you can access that part of the string that is between the start and end indices-1. *The end index is not counted.* If we want to skip particular sequence of characters then there is an optional third parameter in the function too.

### Length

It is often required to know the length of a string for one or the other instructions. Here is how we can do it.

```python
fruit = 'mango'
print(fruit, 'is a', len(fruit), 'character word')
```

---

#### More about string

- How can we get the length of a datatype in python

Using `len` built-in function in Python we can get the length of any datatype in python.

Example:
```python
length = len('my name')
print(length)
```

What happends if we don't specify the indices in the length function.

1. If we don't give the start index in the length function then by default it will take the start index as 0

```python
print('pythonstring'[:5])
print('pythonstring'[0:5])
#both will give the same result
```

2. If we don't give the end index in the length function then by default it will take the end index/length of that string.

```python
print('pythonstring'[3:])
print('pythonstring'[3:len('pythonstring')])
#both will give the same result
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

##### Negative indexed slicing

|String|Indexing|Indexing|Indexing|Indexing|Indexing|Indexing
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|python|<table><tr><td>0</td><td>-6</td></tr><tr><td colspan='2'>p</td></tr></table>|<table><tr><td>1</td><td>-5</td></tr><tr><td colspan='2'>y</td></tr></table>|<table><tr><td>2</td><td>-4</td></tr><tr><td colspan='2'>t</td></tr></table>|<table><tr><td>3</td><td>-3</td></tr><tr><td colspan='2'>h</td></tr></table>|<table><tr><td>4</td><td>-2</td></tr><tr><td colspan='2'>o</td></tr></table>|<table><tr><td>5</td><td>-1</td></tr><tr><td colspan='2'>n</td></tr></table>|


```python
string = 'python'
print(string[2:4])
print(string[-4:-2])
# both will give the same result
```

##Quick Quiz

Guess the output

```python
nm = 'Harry'
print(nm[-4:-2])
```

---

##### References

- [CWH Python 100 days challenge - Day 12](https://youtu.be/8jW7lpT8HW8?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)

- [W3 School - Python Strings](https://www.w3schools.com/python/python_strings.asp)