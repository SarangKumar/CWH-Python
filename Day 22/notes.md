## Day 24 - Python Lists

List is one of the data types in python. If we want to store data that are inter-related then it becomes tedious to create individual variable for each. Instead we can use `List`. List is a data type that is capable to store many entities in itself.

- They are a ordered collection of items.
- They are changeable/mutable.
- They allowd dublicate values.
- They can have other data types as it's elements.

They can we declared using `[` (Open square bracket) at the start and `]` (Closing square bracket) at the end. The elements are stored inside the brackets separated by `,` (commaa)

#### Syntax: 

```python
l = [1, 2, 3]
print(l)
```

Output:
```shell
[1, 2, 3]
```

---

Imagine creating variables to store their marks in each subject in a semester. Then it will look something like this.

```python
# for student A
studentA_maths = 50
studentA_physics = 70
studentA_mechanics = 90
studentA_ece = 80

# for student B
studentB_maths = 70
studentB_physics = 50
studentB_mechanics = 30
studentB_ece = 40
```

As you can see it's tedious to follow this method. It further becomes more hectic to do operations on them. Let's see the same approach using lists.

```python
# Creating a list of marks for each subject

maths = [50, 70]
physics = [70, 50]
mechanics = [90, 30]
ece = [80, 40]


# Creating list of students with their marks

StudentA = [50, 70, 90, 80]
StudentB = [70, 50, 30, 40]
```

For more detailed use click [here](/Day%2022/main.ipynb)

<details>
<summary><strong>FAQ</strong></summary>

- What is ordered data type?

They are those data types that can be indexed. Some examples include tuple, string, lists, ..

- What is immutable data type?

They are those data types whose values cannot be changed once it is initialized.
</details>


## List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

It makes the short syntax of python even shorter.

For examples click [here](/Day%2022//main.ipynb)

---

#### References

- [CWH Python 100 days challenge - Day 22](https://youtu.be/eF6nK5bSlmg)
- [W3School - Python lists](https://www.w3schools.com/python/python_lists.asp)
- [W3School - Python list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)