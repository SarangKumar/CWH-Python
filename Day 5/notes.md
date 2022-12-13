## Day 5 - Comments, Escape Sequence, More about print

#### Comments

- These are lines that are overlooked by the interpreter and hence not executed.
- They are like reference that may be used to tell what is the use of the code snippet - for your future self, or other users.

**Syntax**

```python
# this is a comment - single line comment

print('this will be executed') #this wouldn't be executed

"""
This is a multiline comment - though it is a string but since it is not stored anywhere it will behave/work as comments
We may also use triple single quotes for the same
"""
```

**Tips**
In vs code you may use the shortcut `Ctrl+/` while to comment the selected line of code: only single line comments will be used
This can also be used to undo the single line comments.

#### Escape Sequence Character

- They are special keywords that doesn't represent itself but have special meaning when used in string
- They are written inside string - inside single/double quotes

**Some escape sequence in python**

| **Code** |   **Result**    | **Code** |   **Result**    | **Code** |   **Result**    |
| :------: | :-------------: | :------: | :-------------: | :------: | :-------------: |
|    `\'`  |  Single Quote   |    `\r`  | Carriage Return |    `\f`  |    Form Feed    |
|    `\\`  |    Backslash    |    `\t`  |       Tab       |   `\ooo` |   Octal Value   |
|    `\n`  |    New Line     |    `\b`  |    Backspace    |   `\xhh` |    Hex value    |

#### Syntax

```python
print("Output: new\nline")
# Output: new
# line

print("It's an apple") #No error
# print('It's an apple') #Error
# print("It"s an error") #Error
print("It\"s an apple") #No error

# Use ' inside " " or use " inside ' '
```

#### More about print

- It is one of the built in functions in python
- What ever write in the print function will be displayed in the cmd.

#### Syntax

```python
print(object(s), [sep=seperator, end=end, file=file, flush=flush])
```

| Key | Work |
| :-----: | :------- |
| object  | <ul><li>this is the statement that you want to print</li></ul> |
|   sep   | <ul><li>Optional</li><li>This specifies that should be the seperator in the object. Which character will be between 2 words of the object.</li><li>Default value is space, `sep=" "`</li></ul> |
|   end   | <ul><li>Optional</li><li>This specifies what should be the end character in the print statement, i.e. what is the seperator between 2 print functions</li><li>Default value is new line character, `end='\n'`</li></ul>|
|file|<ul><li>An object with a write method</li><li>Default value is `sys.stdout`</li></ul>|
|flush|<ul><li>Optional</li><li>Will be discussed later</li><li>Default value is new line character, `flush=false`</li></ul>|
|   sep   | <ul><li>Optional</li><li>this specifies that should be the seperator in the object. Which character will be between 2 words of the object.</li><li>Default value is space, `sep=" "`</li> | </ul> |
|   end   | <ul><li>Optional</li><li>This specifies what should be the end character in the print statement, i.e. what is the seperator between 2 print functions</li><li>Default value is new line character, `end='\n'`</li></ul>|
|file|<ul><li>Optional</li><li>An object with a write method</li><li>Default calue is `sys.stdout`</li></ul>|
|flush|<ul><li>Optional</li><li>Will be discussed later</li></ul>|

---
##### References
- [CWH Python 100 days challenge - Day 5](https://youtu.be/qxPMmW93eDs?list=TLPQMDIxMjIwMjIyZJARBd2Aqg)
