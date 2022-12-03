## Day 3 - Module and pip in python

---

#### What are modules
- These are small pieces of reuseable code.
- Used to borrow codes that others have made

- It' of 2 types
    - *External*
    That are available but needs to be downloaded first
        - They are interesting

    - *Build-in* 
        That are available but need not be downloaded to use
        - Error free
        -  Reliable

---

#### What is pip
It's a package manager that has a collection of modules and is used to be download modules

#### How to download external modules

>pip install *modulename*

alternatively you may also use the below command to be version specific

>pip3 install *modulename*

Example 

>pip install pandas
*or*
>pip3 install pandas

---

*If your pip is not working then one of the reasons can be you have not checked the pip part while installing python setup. Try reinstalling the same*
*If that doesn't help then [this might help](https://builtin.com/software-engineering-perspectives/pip-command-not-found)*

---

Example of some of the build in modules

- math
- random
- time
- fs

---

#### How to use moodules in python script

```python
import modulename
import modulename as alias
from modulename import functionname
from modulename import functionname as alias
from modulename import functionname1, functionname2
```

---

##### References
- [CWH Python 100 days challenge - Day 3](https://youtu.be/xwKO_y2gHxQ?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
- [More about Modules](https://docs.python.org/3/tutorial/modules.html)