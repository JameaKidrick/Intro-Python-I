Navigating git/terminal
- fork and clone using `git bash`
- open `Powershell` and `cd` into folder
- run `code .`
- open `Powershell` in VS Code
- to run print in terminal: 
  - run `python` then `print (<INSERT CODE>)`
    - example: 
    
      ---
      `> python`  
      
      `>>> print('Hello, world')`
      
      Hello, world

      ---

- to run print from file:
  - run `python3 <file name>`
    - example:

      ---
        `> python3 00_hello.py`
        
        Hello, world!
        
      ---

Help
- use help to get a list of the methods you can use with a specific data type
  - for example, `help(array)` **if array = [ ]** will show a short list of array methods that you could use


Lists
- = JS arrays
- order matters
- starts at 0



<!-- 
>>> x = [1, 2, 3]
>>> x
[1, 2, 3]
>>> help(x.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> x.insert(3, 4)
>>> x
[1, 2, 3, 4] 

-->