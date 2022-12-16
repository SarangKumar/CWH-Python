## Day 17 - For Loop

## What is looping

Sometimes we need to do a certain task repeatedly and it becomes tedious and some times hectic we go with the normal way. For example we want to print numbers from 1 to 10000 then it is not humanly possible to do this task quicky and withour error. Here is where looping comes. 

The work of the loops is to execute a code block repeatedly for certain number of times(`for`) or based on some condition(`while`). Based on this condition there are mainly 2 kinds of loops.

- for loop
- while loop

#### For loop

This type of loop is used when we know how many iterations are to be done.
Using for loop we can iterate over any iterable - `string`, `list`, `tuple`, etc. We will learn about all those and more in comming lessons.

#### Syntax

```python
for variable_name in iterable:
    statement
    #during each iteration the variable_name will take one part of the iterable.
```

For example:

```python
name = 'Ronit'
for i in name:
    print(i, end=',')
```

Output:

```shell
R,o,n,i,t
```

> For more examples see the main file

#### FAQ

- What is range() ?

If we want to print numbers form 1 to 100 using looping then how can we do this. Do we need to create a list that has numbers from 1 to 100. Here is where the range jumps in. You can think of this as it kind of creates a list having elements from 1 to 100.

More about range function:
- range function takes 3 argumens out of which 2 in optional.
- range(start, end, skip)
- by default start value is 0 i.e. the iteration starts from 0
- end is compulary argument and end-1 is the ending value in the iteration
- skip is another optional argument. it makes the iteration skip some steps. if skip is 2 then the iteration will be like 0, 2, 4, so on. It's default value is 1


---

#### References

- [CWH Python 100 days challenge - Day 17](https://youtu.be/fIYVzKp0q5w)