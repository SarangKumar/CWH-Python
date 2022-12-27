## Day 25 - Tuple Methods

Since tuple is one of the most used data types it becomes obvious to be familiar with the methods of lists.

One trick that can be done here to do more with tuple is first convert it to list, perform the operation and then convert it back to tuple. This open more for tuple manipulation.

```python
temp = ('Apple', 'Banana', 'Tomato', 'Ladyfinger')
fruits = list(temp).pop()
fruits = tuple(temp)
print(fruits)
```


For examples click [here](/Day%2025//main.ipynb)

---

#### References

- [CWH Python 100 days challenge - Day 24](https://youtu.be/PipsOUDKrVk)
- [W3School - Python tuples](https://profile.w3schools.com/refresh-session?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fpython%2Fpython_tuples.asp)