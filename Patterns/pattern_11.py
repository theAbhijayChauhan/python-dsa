""" print
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

"""

def pattern(num):
    for i in range(num):
        for j in range(i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

pattern(5)