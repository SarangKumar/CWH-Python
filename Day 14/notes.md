## Day 14 - If else conditionals


Often there is requirement to generate different output that depends on some conditions. For example one may carry umbrella **if** *it's raining* `or` **if** *the weather forecast recommends so* **else** there is no need of umbrella. 

In python you can do so by using `if`, `elif` and `else` keyword. This will become more clear with the following example.

#### Syntax
```python
if condition1: #condition- that evaluates to true or false only.
    statement
elif condition2: #if the condition1 evaluates to false then condition 2 is checked
    statement
elif condition3: # if the previous condition also evaluates to false then condition3 is checked
    statement
else:
    statement
```

Condition in programming means some constraints that evaluates to either `True` or `False` but nothing in between.

#### Working 

The statements that are indented in the if,elif and else block belongs to the corresponding block. In python indentation is used to tell that the code belongs to this block unlike most programming languages where parenthesis is used.
If the condition1 in the above code evaluates to true only then the statement corresponding to that block is executed and execution flow comes out of the if else conditions.If the condition1 evaluates to false then condition2 is checked and it's block is executed only when that condition is true. If no condition evaluates to true then else block is executed. The execution jumps from `if` to `elif` to `else` but only one block of statements is executed rest are ignored.

`elif` and `else` are not compulsary.

#### Types

Based on these cases the conditional statements are further classified into following types: 
- if
- if-else
- if-elif-else/else-if ladder
- nested if-elif-else

Consider a case when one wants to write a code that displays if the user is eligible to get driving license. Then there is a need to use conditionals. The corresponding code is as follows: 

```python
age = 17
if age>=18:
    print('You can get driving license')
else:
    print('You cannot get DL.')
```
>Refer main.ipynb file to see more example codes

#### Operators in if-else

- Comparison operator
If we want to compare two numerical type quanties then we can use comparison operators like `==`,`!=`, `>`, `>=`, `<` or `<=`.
The above operators always evaluates the expression either **true** or **false**

- Logical operator
If our condition are depends upon 2 or more expression then those sub conditions can be joined using `and`, `or` and `not` keywords.
    - `and` is used when both the expressions are true. It will check the second expression only if the first expression is true else it won't check the second expression
    - `or` is used when we want either of the expressions to be true to give the final output as true. It will check the second expession only if the first expression is false else it won't check the second expression
    - `not` is used to negate the 

---

##### References

- [CWH Python 100 days challenge - Day 14](https://youtu.be/ceiuLR2ysas)
