# print * * * *
#       * * * *
#       * * * *
#       * * * *

def pattern(row, col):
    for i in range(row):
        for j in range(col):
            print("*", end=" ")
        print()

row = int(input("Ente the number of rows: "))
col = int(input("Ente the number of rows: "))
pattern(row, col)