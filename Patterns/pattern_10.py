""" print
*
* *
* * *
* * * *
* * * * * 
* * * *
* * *
* *
*

"""

def pattern(num):
    for i in range(num):
        for j in range(i + 1):
            print("*", end=" ")
        print()
        
    for i in range(1, num):
        for j in range(num - i):
            print("*", end=" ")
        print()

pattern(5)




# By Math Formula :
def pattern_math(num):
    # Total rows = 2 * 5 - 1 = 9
    for i in range(1, 2 * num):
        # Math formula to flip the direction after reaching the peak
        stars = i if i <= num else (2 * num - i)
        
        print("* " * stars)

pattern_math(6)
