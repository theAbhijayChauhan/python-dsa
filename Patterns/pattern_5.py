""" print * * * * *
          * * * * 
          * * *
          * * 
          *
"""

def pattern(num):
    for i in range(num):
        for j in range(num - i):
            print("*", end = " ")
        print()

num = int(input("Enter the number: "))
pattern(num)