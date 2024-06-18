# Functions

Example of function definition:

```commandline
def my_function(int: param1, int: param2):
    output = param1 + param2
    return output
```
  * By default, function returns *None* when there's no `return` statement


Example of function call:

```commandline
myfunction(1,1) #returns 2
```

## Built-in Functions

```commandline
print("Hello") # return: Hello

name = input("Enter your name: ") #assigns input value to variable name

```

|Built-in Function | Explain                                            | Example call | Outcome          |
|---|----------------------------------------------------|---|------------------|
|print(value) | display value in console                           | print("Hello World")| \>\> Hello World |
|input(prompt) | display prompt in console and collect user input   |name = input("Name: ") | name = user_input|
|dir(object)| get all attributes of object                       | dir("John") | ['capitalize', 'casefold', ...] |
|type(object) | get class name of object                           |
|id(object)| specific location of object in memory              |
|len(object) | length of collection (e.g string, list, dict, etc) |
|round(number) | |
|str(object) | create a string from object | |
