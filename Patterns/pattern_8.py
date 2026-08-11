""" print 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""


def reverse_pattern(num):
    for i in range(num):
        # 1. Print leading spaces (multiplied by 2 for visual alignment)
        for j in range(2 * i):
            print(end=" ")
            
        # 2. Print stars with spaces in between
        for j in range(2 * (num - i) - 1):
            print("*", end=" ")
            
        # 3. Move to the next line
        print()

reverse_pattern(5)