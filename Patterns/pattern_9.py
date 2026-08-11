""" print
                *
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * * 
          * * * * * * * 
            * * * * * 
              * * * 
                * 
"""

def pattern(num):
    for i in range(num):
        for j in range(2 * (num - i -1)):
            print(end = " ")
        for j in range(2 * i + 1):
            print("*", end = " ")
        print()
    
    for i in range(1, num):
        for j in range(2 * i):
            print(end = " ")
        for j in range(2 * (num - i) - 1):
            print("*", end=" ")
        print()

pattern(5)