## Day 19 - Break and Continue

In loop sometimes we want to `break` out of the loop or skip some iteration depening upon some condition and `continue` with next iteration

#### Break 

When is used when we want to end the loop depending upon some condition(in programming terms breaking out of the loop). Number of iterations left are matter of least concern.

Example: 
```python
for i in range(10):
    print(i)
    if(i==5):
        print('Not gonna cross 5')
        break
```

Output:
```shell
0
1
2
3
4
5
Not gonna cross 5
```

#### Continue

When we want to skip an iteration not the entire loop then we use continue.

Example:
```python
for i in range(1, 21):
    if(i%2==0):
        continue
    print(i)
```

Output:
```shell
1
3
5
7
9
11
13
15
17
19
```

#### Emulating do while loop: Solution to previous lecture question

```python
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
```

---

#### References

- [CWH Python 100 days challenge - Day 19](https://youtu.be/RkwJnjdrm70)