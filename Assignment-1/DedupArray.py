
"""
Peter Mora-Stevens
12:02 am

DedupArray
Time: 7mins
Solution: 4mins
Testcases: 3mins

problem description

Algorithm: linear search
Time Complexity O(n^2) where n is the size of the input array since we need to look at every element of the array and n^2
                        because the pop op is only O(1) if the item being popped is at the end of an array (like a stack)
Space Complexity O(1) as we only need to see if we've seen the same value, if any value is higher, we assign the higher value to the variable

Information we know
    - we are given a list of duplicating integers

Edge Cases
    - Array is empty, return empty array
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    a) we will need to look at every element of the array
    b) to tell if we have a duplicate, we add it to a set
    c) if ever seen again, we pop at the current index until no more values appear and iterate index
        use a while loop to make sure we don't index out of bounds

"""
"""def DedupArray(inputArray):
    
    maxSeen = 0
    
    inputSize = len(inputArray) - 1
    i = 0
    while i < inputSize:
        while i <= inputSize and inputArray[i] == maxSeen:
            inputArray.pop(i)
            inputSize -= 1
            
        if i <= inputSize and inputArray[i] != maxSeen:
            maxSeen = inputArray[i]
            i += 1
            
    return inputArray"""
                
                
                
# Second iteration
# Time: O(n)
# Space: O(1)
def DedupArray(arr):
    
    l = 0
    for r in range(len(arr)):
        if arr[l] != arr[r]:
            l += 1
            arr[l] = arr[r]
    while len(arr) > l + 1: arr.pop()
    return arr
    


if __name__ == "__main__":
    
    # provided
    testcase = [1, 2, 2, 3, 3, 4, 4, 4, 4]
    print("Actual: ", DedupArray(testcase), "Expected: [1, 2, 3, 4]")
    testcase = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
    print("Actual: ", DedupArray(testcase), "Expected: [0, 1, 4, 5, 8, 9, 10, 11, 15]")
    testcase = [1, 3, 4, 8, 10, 12]
    print("Actual: ", DedupArray(testcase), "Expected: [1, 3, 4, 8, 10, 12]")
    
    # edge-cases
    testcase = [] # empty array
    print("Actual: ", DedupArray(testcase), "Expected: []")
    testcase = [1] # a single value
    print("Actual: ", DedupArray(testcase), "Expected: [1]")