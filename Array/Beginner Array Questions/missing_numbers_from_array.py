def missingNumber_usingMath(arr):
        n = len(arr)
        # Calculate expected sum from 0 to n
        expectedSum = (n * (n + 1)) // 2
        # Calculate the actual sum of elements in the array
        actualSum = sum(arr)
        
        print(f"The missing number is : {expectedSum - actualSum}")

    

def missingNumber_usingXOR(arr):
        missing = len(arr)
        
        # XOR every index and every value
        for i, num in enumerate(arr):
            missing ^= i ^ num
            
        print(f"XOR result is : {missing}")



arr = [0,1,2,3,5,6]
size = len(arr)
missingNumber_usingMath(arr)
missingNumber_usingXOR(arr)