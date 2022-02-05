my_string = "hElLo WoRlD"
my_other_string = "hello"

# Capitalize Method
print(my_string.capitalize()) # returns the string with the first letter capitalized, lower everything else.
print(my_other_string.capitalize())
print()

# Find Method - finds the index of the specified substring. returns -1 if it doesn't exist
print(my_string)
print(my_string.find("W"))
print()

# Determining if we have numerical information
val='094'
print(val.isnumeric())
print(val.isdecimal())
print(val.isdigit())
print()

val = '½'
print(val.isnumeric())
print(val.isdecimal())
print(val.isdigit())
print()

# Other
all_caps = "HELLEO"
print(all_caps.lower())
print(all_caps.split("E"))
print("78".zfill(6))
print("      hi            ")
print("      hi            ".strip())
print("hello".upper())
print("Mumbo".replace("M","W"))
