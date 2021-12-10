# Scope - The region of code a variable is accessible in
# Global Variables - Variables that are accessible everywhere
# Local variables - variables defined in a regional context (like a function)
# Shadowing - a local variable hiding the global variable's value

# an example of scope

a = 10    # a is defined globally      

def my_func(x):
    a = 11     # a is defined locally here
    b = 21     # b is defined locally here
    x *= 2     # x, the parameter, is being doubled 

    print(f"in my_func: a = {a}, b = {b}, x = {x}")  # prints the local a and local b

b = 20          # a global b is defined here   
my_func(b)      # the function is called with b as the actual parameter


print(f"in the main program: a={a}, b={b}") # should print the global a as 10, the global b as 20

def my_other_func():
    global a    # access the global a so that we can change it
    a *= 1.5    # global a gets scaled by 1.5
    print(f"in my_other_func: a={a}, b={b}")   
    # global a gets printed and global b is printed since there no local b shadowing the global b

my_other_func()
print(f"In the main program: a={a}, b={b}")  # both are global, a is 15, b is 20   