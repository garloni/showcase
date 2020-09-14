# Automate the Boring stuff
## Resources
- pastebin.com
- gist.github.com

## Python basics
| Operator | Operation | 
| --- | --- | 
| `**` | Exponent | 
| `%` | Modulus/Remainder | 
| `//` | Integer division/floored quotient | 
| `/` | Division | 
| `*` | Multiplication | 
| `-` | Subtraction | 
| `+` | Addition | 

Data types:  
- Integers
- Floating-point
- Strings
  - Concatenation: Operators are polyvalent. For example the addition operator when used on two string values, it joins the strings.
  - Replication: 

Functions:
`print()`
`input()`
`len()`
`str()`
`int()`
`float()`
`round()`
`abs()`

## Flow control
Diagrams:
- Start/End: Rounded rectangles
- Decision: Diamond
- Action: Rectangle

<abbr title="Named after mathematician George Boole">Boolean</abbr>:  

- `True`
- `False`


| Operator | Meaning | 
| --- | --- |
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

Truths tables:

And table:  

| Input | Output |
| --- | --- |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |

Or table:  

| Input | Output |
| --- | --- |
| True or True | True | 
| True or False | True | 
| False or True | True |
| False or False | False |

Not Table

| Input | Output |
| --- | --- |
| not True | False |
| not False | True | 


Blocks of code:  
There are three rules: 
1. Blocks begin when indentation increases
2. Blocks can contain other blocks
3. Blocks end when the indentation decreases to zero or to a containing block's indentation

While clause always consists of the following:
- The `while` keyword
- A condition, an expression that evaluates to `True` or `False`
- A colon
- Starting on the next line, an indented block of code called the `while` clause

`import` statement consist of the following:
- The `import` keyword
- The name of the module
- Optionally, more module names, as long as they are separed by commas

## Functions
A major purpose of functions is to group code that gets executed multiple times.  
In general you always want to avoid duplicating code.

When you call `print()` or `len()` function, you pass them values, called *arguments*, by typing them between the parentheses. You can also define your own functions that accept arguments.

```
def hello(name):
  print('Hello, ' + name)

hello('Alice')
hello('Bob')
```

**Parameters**: Are variables that contain arguments. When a function is called with arguments, they are stored in the parameters.  
One thing to remember is that the value stored in a parameter is forgotten when the function returns.

- **Define**: A function is to create it.
- **Call**: Executes or "calls" the function.
- **Pass**: Pass the chosen string value to the function.
- **Argument**: Is a value being passed to a function in a function call.
- **Parameter**: They are values that have arguments assigned to them.

The `None` value: Represents the absence of a value. It must be typed with a capital N.  
`sep` keyword argument  

The call stack is how Python remembers where to return the execution after each function call. The call stack isn't stored in a variable in your program; rather it creates a frame object on the top of the call stack. These objects store the line number of the original function call so that Python can remember where to return. If another function call is made, Python puts another frame object on the call stack above the other one.

When a function call returns, Python removes a frame object from the top of the stack and moves the execution to the line number stored in it.

> Note that frame objects are always added and removed from the top of the stack and not from any other place.

Local scope: Parameters and variables that are assigned in a called function
Global scope: Variables that are assigned outside all functions

When a scope is destroyed, all the values stored in the scope's variables are forgotten. 
There is only one global scope, and it is created when your program begins. When your program terminates, the global scope is destroyed, and all its variables are forgotten.  

A local scope is created whenever a function is called. Any variables assigned in the functino exist within the function's local scope. When the function returns, the local scope is destroyed, and these variables are forgotten.

Scopes matter for several reasons:
- Code in the global scope, outside of all functions, cannot use any local variables
- However, code in a local scope can access global variables
- Code in a function's local scope cannot use variables in any other local scope
- You can use the same name for different variables if they are in different scopes. That is there can be a local variable named `spam` and a global variable also named `spam`.

Errors can be handled with `try` and `except` statements. When the code inside causes an error the program execution immediately moves to the code in the `except` clause. After running that code, the execution continues as normal. 




## Lists
## Dictionaries and structuring data
## Manipulating strings
## Pattern matching with regular expressions
## Input validation
## Reading and writing files
## Organizing files
## Debugging
## Web scraping
## Working with excel spreadsheets
## Working with google sheets
## Working with pdf and word documents
## Working with csv files and json data
## Keeping time, scheduling tasks and launching programs
## Sending email and text messages
## Manipulating images
## Controlling the keyboard and mouse with GUI automation