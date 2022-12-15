## Day 17 - While Loop

While loops are used when we want to do iteration but we don't know how many times do we need to do looping but that depends on some condition.

#### Syntax

```python
while condition:
    statements
```

For example:
```python
i = 10
while i>4:
    print(i)
    i-=1
```

Output:

```shell
10
9
8
7
6
5
```

>**Warn**
>
>While using while loop it may happen that you end up with infinite loop. One must be cautions about this.

## While with else

#### Syntax

```python
while condition:
    statements
else:
    statement
```

Only after the loop ends the else part is executed once. See [here](./main.ipynb) for more

#### Exercise - Emulate do while loop

---

#### References

- [CWH Python 100 days challenge - Day 18](https://youtu.be/-tCFyIyKVx0)