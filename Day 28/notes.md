## Day 28 - f-String

`Python 3.6` onwards f-strings are introduced. They allow us to place the variables inside strings more conveniently. This is used to format strings.

Conventional way of writing strings with variables

##### Method 1 : using + operator

```python
name = 'Sarang'
country = 'India'
string = 'Hey! I am '+ name +' and I am from '+country+'.'
print(string)
```

Output
```shell
Hey! I am Sarang and I am from India.
```

##### Method 2 : using tuple join method

```python
name = 'Sarang'
country = 'India'
string = 'Hey! I am', name,'and I am from',country,'.'
# as string is now tuple - we need to convert it to string
string = ' '.join(string)
print(string)
```

Output
```shell
Hey! I am Sarang and I am from India.
```

##### Method 3 : using list join method

```python
name = 'Sarang'
country = 'India'
string = ['Hey! I am', name,'and I am from',country,'.']
string = ' '.join(string)
print(string)
```

Output
```shell
Hey! I am Sarang and I am from India.
```

##### Method 4 : Using string method

```python
name = 'Sarang'
country = 'India'
string = 'Hey! I am {} and I am from {}'.format(name, country)
print(string)
```

Output
```shell
Hey! I am Sarang and I am from India.
```

##### Method 5 : Using f-string

```python
name = 'Sarang'
country = 'India'
string = f'Hey! I am {name} and I am from {country}'
print(string)
```

Output
```shell
Hey! I am Sarang and I am from India.
```

Click [here](/Day%2028/main.ipynb) for more examples on f-strings

---

#### References

- [CWH Python 100 days challenge - Day 28](https://youtu.be/ixmxgUf8yIg)
