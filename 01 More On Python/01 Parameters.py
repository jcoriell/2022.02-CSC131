# An example of Formal Parameters vs Actual Parameters

# A formal parameter is defined as part of a function heard
# An actual parameter (or argument) is the value that is passed into the function when it is called

def average(a, b):          # a and b are formal parameters
    return (a + b) / 2

val1 = 10
val2 = 20

avg = average(val1, val2)   # val1 and val2 are actual parameters
print(avg)