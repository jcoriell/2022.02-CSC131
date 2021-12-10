# Logical Operators - and, or, not
# a and b - returns a if a is False, b otherwise
# a or b - returns b if a is False, a otherwise
# not a - returns False if a is True, True otherwise
# and and or are short circuit operators - minimum number of inputs required is evaluated

a = True
b = False

print(f"a and b is {a and b}")
print(f"a or b is {a or b}")
print(f"not a is {not a}")

# Truthiness of numbers
print(True == 1) # evaluates to True
print(False == 0) # evaluates to True
print(True == 5) # evaluate to False
print(True == bool(5)) # evaluate to True

# Membership Operators - 'in' and 'not in'
print(5 in [1,2,3,4,5])
print(5 not in [1,2,3,4,5])