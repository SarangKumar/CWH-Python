## Day 16 - Match Case

Introduced in python version 3.10. It is one of the newest feature that python has launched. The job of this match case is very similar(but not identical) to the job of switch case in `C` or `Js` or in most of the programming languages. 

#### Syntax

```python
match variable_name:
    case value1:
        statements
    case value2:
        statement
    case value3 [if condition]:
    case _: # for default
        statement
```

#### Working

Depending on the value of a variable there may be different statements that you want to execute. Previously one can do so using the if-elif-else ladder. But now the now this work is more simplified and advanced with the use of this match case.

A match statement will compare a given variable's value to different shape, also refered to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it find a match.

The case clause consists of a pattern to be matche to the vairblae, a condition to be evaluates if the pattern matches(not compulsary), and a set of statements to be executed if the pattern matches. The `_` here means the program should execute the statements under that if none of the cases match.

Example code:
```python
command = 'Hello, World!'
match command:
    case 'Hello, World!':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later')
    case other: #other does the same work as _
        print('No match found')
```

>**Note**
>The catch here is that unlike in other programming languages where the break keyword was required if we want to prevent further execution of the cases if a match is found here there is need to put the `break`. Python automatically comes out of the match case.
---

##### References

- [CWH Python 100 days challenge - Day 15](https://youtu.be/bthQCK1QAmQ)
