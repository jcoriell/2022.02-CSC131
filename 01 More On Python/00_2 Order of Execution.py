# Order of Execution Example 2

for a in range(1, 4):
    for b in range(1, 5):
        print(f"{a} * {b} = {a*b}")


# Order of execution:
# 3, 4, 5, 4, 5, 4, 5, 4, 5 -- 3, 4, 5, 4, 5, 4, 5, 4, 5 -- 3, 4, 5, 4, 5, 4, 5, 4, 5