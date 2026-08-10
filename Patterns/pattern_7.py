""" print       *
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * *
"""

def pattern(num):
    for i in range(num):
        # Space
        for j in range(2 * (num-i-1)):      # The Star Formula (2 * i + 1): This always generates consecutive odd numbers
            print(end = " ")
        # Star
        for j in range(2*i+1):              # The Space Formula (num - i - 1): This decreases by exactly 1 on every row
            print("*", end = " ")
        print()

# num = int(input("Enter the number: "))
pattern(5)