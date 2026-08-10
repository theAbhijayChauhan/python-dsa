""" print 1
          1 2
          1 2 3
          1 2 3 4   
          1 2 3 4 5   
"""

def pattern(num):
    for i in range(num):
        for j in range(i + 1):
            print(i+1, end = " ")
        print()

num = int(input("Enter the number: "))
pattern(num)