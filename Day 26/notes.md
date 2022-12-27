## Day 26 - Solution 2: [Good Morning Sir](/Day%2015/nodes.md)


#### Solution code

```python
import time
hour = int(time.strftime('%H'))

if hour >=0 and hour<12:
    print('Good Morning Sir')
elif hour>=12 and hour<17:
    print('Good Afternoon Sir')
else:
    print('Good Evening Sir')
```

```shell
Good Morning Sir
```

---

#### References

- [CWH Python 100 days challenge - Day 26](https://youtu.be/IZBKXWrbqBM)
