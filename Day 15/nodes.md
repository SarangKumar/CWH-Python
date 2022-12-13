## Day 15 - Exercise 2

## Exercise 2 - Good Morning Sir

Create a python program capable og greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

#### Solution

```python
import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(0<=timestamp<12):
    print('Good Morning')
elif(12<=timestamp<15):
    print('Good Afternoon')
else:
    print('Good Evening')
```

---

##### References

- [CWH Python 100 days challenge - Day 15](https://youtu.be/d7ng_aV4qdI)
- [Python doc for Time module](https://docs.python.org/3/library/time.html)