""" print
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1

"""

def pattern(num):
    for i in range(num):
        # 1. Left side numbers (increasing)
        for j in range(1, i + 2):
            print(j, end=" ")
            
        # 2. Middle spaces (Adjusted to print TWO spaces per step)
        for j in range(2 * (num - i - 1)):
            print("  ", end="")  # <--- Changed " " to "  " (two spaces) for better output !
            
        # 3. Right side numbers (decreasing)
        for j in range(i + 1, 0, -1):
            print(j, end=" ")
            
        print()

pattern(4)