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

---
### **COLLECTIONS**

Lists
- === JS arrays
- group of items referenced by index
- order matters
- starts at 0
- mutable
- allows duplicate items
- methods:
  - `.insert()`
  - `.append()`
  - `.remove()`
  - `.pop()`
  - `del`
  - traverse
    - for i in range()
  - slice
    - array = [1, 2, 3]
    - newArray = array[0:2] or newArray = array[ :2]
      - omits the 2nd index (3)
    - newArray = array[1: ]
      - omits the 0th index (1)

Tuples 

- use parentheses
- order does not matter
- immutable

Dictionaries

- === JS objects
- contains key:value pairs
- immutable
- keys can be strings, numbers, or tuples that contain immutable types such as strings, numbers, or other tuples unless those tuples include a mutable object
  - lists can not be used as keys since they can be modified using indeces, slices, or methods (append/extend)
- keys have to be unique within one dictionary
- use `list(dictionary)` to get a list of all the keys
- use `sorted(dictionary)` to get a list of all the keys sorted
- use `in` (example: word in dictionary) to check if the dictionary includes that key (returns boolean)


Functions

- `positional arguments`: arguments mapped to parameters based solely on their order
  - example: def function(name, age, skill)
    - when calling function - function('Jane', 24, 'typing')
    - so name = Jane, age = 24, skill = typing

- `arbitrary arguments`: used when the amount of arguments that will be passed to the function are unknown; so an asterisk is used before the name of the parameter to declare the parameter arbitrary
  - example: def function(*attendees)
    - when calling function - function('Jane', 'Jill', 'John', 'James', 'Jeremy', 'Jack')
    - although there is one parameter, you can give as many arguments as you want

- `keyword arguments`: allows arguments to be out of order 
      _Note - you should either use positional or keyword, not a mix of both unless the keyword argument follows the positional argument. I can't think of a case when you would want this since that essentially makes it a positional argument_
  - example: def function(pet, diet, age)
    - when calling function - function(pet='cat', diet='carnivorous', age=3)
    - you set the parameter equal to the argument given thereby defining the parameter using its keyword

- `default arguments`: function arguments can be given default values 
      _Note - you can not have non-default arguments following default arguments (BAD -> def test(num1 = 2, num2))_
  - example: def function(name, greeting='Hello!')
    - when calling function - function(Jim) or function(Jim, 'Howdy!')
    - give the parameter(s) an argument which will allow omission of that parameter when calling the function

Packing/Unpacking Argument lists
https://docs.python.org/3.7/tutorial/controlflow.html#unpacking-argument-lists