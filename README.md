*This project has been created as part of the 42 curriculum by khhammou*

## Description
Imports required:

1_ functools is a module that contains advanced tools for functional programming:
reduce: combine a list of values into one using a function like sum or multiply
partial: fix some arguments of a function to create a new specialized function
wraps: preserves metadata when creating decorators
lru_cache: memorizes function results for performance

2_ operator which is the functional equivalent for common operations:
operator.add
operator.mul
operator.max
etc...
Can be used with reduce instead of writing your own functions

3_ itertools which is advanced iterations patterns:
product, permutations, combinations, chain, etc..
Useful for generating sequences in a functional style

4_ math and time for measuring execution or math for calculations

New concepts introduced:
| Concept                         | What it is                                                                        | Example Use                                                 |
| ------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Lambda / Anonymous Function** | A small, unnamed function written inline.                                         | `lambda x: x * 2`                                           |
| **Higher-Order Function**       | A function that takes another function as input or returns a function.            | `map(lambda x: x*2, my_list)`                               |
| **Closure / Lexical Scope**     | Functions that “remember” variables from the environment where they were created. | `def counter(): n=0; def inc(): nonlocal n; n+=1; return n` |
| **functools.reduce**            | Combines all elements of a list into a single value using a function.             | `reduce(operator.add, [1,2,3]) → 6`                         |
| **functools.partial**           | Creates a new function with some arguments fixed.                                 | `partial(pow, 2) → lambda x: pow(2, x)`                     |
| **functools.lru_cache**         | Caches results of a function to improve repeated calls.                           | Fibonacci example                                           |
| **functools.singledispatch**    | Create a function that behaves differently depending on input type.               | Can handle int, str, list differently                       |
| **Decorators**                  | Functions that wrap other functions to modify behavior.                           | `@my_decorator`                                             |
| **@staticmethod**               | A method in a class that doesn’t access `self`.                                   | Utility function inside a class                             |
| **Type Hints**                  | Optional hints for variables and function signatures.                             | `def f(x: int) -> float:`                                   |

## Functions are treated in python like normal data
you can store them in variables
pass them as arguments
return them from other functions
store them in lists/dictionaries
Example:
def fireball(target):
    return f"Fireball hits {target}"
spell = fireball
print(spell("Dragon"))

## Lambda functions (Anonymous functions)
A lambda is a small function with no name
Syntax:
Lambda arguments: expression
Example:
lambda x: x * 2
Equivalent to:
def double(x):
    return x * 2
Notes:
lambda can only contain one expression
lambda x: x + 1 is valid
lambda x:
    y = x + 1
    return y
IS INVALID

## Functional Iteration Tools
#### map()
Applies a function to each element
Example:
numbers = [1,2,3]
list(map(lambda x: x * 2, numbers))
Result:
[2,4,6]

#### filter()
keeps elements that pass a condition
Example:
numbers =[1,2,3,4]
list(filter(lambda x: x > 2, numbers))
Result:
[3,4]

#### sorted() with key
Sort objects using a function
Example:
items = [{"power":5},{"power":10}]
sorted(items, key=lambda x: x["power"])

#### Higher-Order Functions
A higher-order function:
1_ receives a function as argument
2_ or returns a function
EXample:
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply
Usage:
times3 = multiplier(3)
print(times3(10))
Result:
30

#### Closures and Lexical Scope
A closure happens when a function remembers variables from where it was created
Example:
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
Usage:
c = counter()

c() -> 1
c() -> 2
c() -> 3
The inner function remembers count

Important keyword: nonlocal
It allows modifying variables from the outer function

## functools module
functional utilities

#### reduce()
Combines a list into one value

Example:
from functools import reduce
from operator

numbers = [1,2,3,4]

reduce(operator.add, numbers)
Result:
10
the process: ((1 + 2) + 3) + 4

#### partial()
Creates a new function with fixed arguments

Example:
from functools import partial

def enchant(power, element, target):
    return f"{element} enchant {target} with {power}"

fire_enchant = partial(enchant, 50, "fire")

fire_enchant("sword)

Result:
fire enchant sword with 50

#### lru_cache
Caches results of expensive functions

Example fibonacci:
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
Now repeated calls become much faster

#### singledispatch
Allows functions to behave differently depending on argument type
Example:
from functools import singledispatch

@singledispatch
def spell(x):
    return "unknown"

@spell.register(int)
def _(x):
    return f"damage {x}"

@spell.register(str)
def _(x):
    return f"enchant {x}"

#### Decorators
A decorator modifies a function without changing its code
Structure:
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper
Usage:
@decorator
def fireball():
    print("boom")

Execution:
before
bloom
after

#### functools.wraps
When writing decorators you must preserve the original function metadata
Example:
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

without wraps, python loses the original function name and documentation

#### Parameterized Decorators
Decorators that receive arguments
Example:
def validator(min_power):

    def decorator(func):

        def wrapper(power):
            if power < min_power:
                return "too weak"
            return func(power)

        return wrapper

    return decorator
Usage:
@validator(10)
def cast(power):
    return f"cast with {power}"

#### static methods
Inside classes:
instance method -> uses self
static method -> does not use self

Example:
class Mage:

    @staticmethod
    def validate(name):
        return len(name) >= 3
Call:
Mage.validate("Alex")
No object required




Go crazy:
autopep8 --in-place --aggressive --aggressive ft_garden_management.py
### Instructions

You run this code by doing python3 file_name.py

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors