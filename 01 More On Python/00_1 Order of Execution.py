# Example of Order of Execution

def min(a,b):
    if a < b:
        return a
    else:
        return b
 
def max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another number: "))
print(f"The smaller is {min(num1, num2)}")
print(f"The larger is {max(num1, num2)}")

# Order of execution if a < b: 
# 15, 16, 17, 3, 4, 5, 18, 9, 10, 12, 13

# Order of execution if a > b:
# 15, 16, 17, 3, 4, 6, 7, 18, 9, 10, 11