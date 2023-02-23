
"""
Peter Mora-Stevens
12:02 am

DedupArray
Time: 7mins # This feels like cheating, probably a coding solution which is better than my solution which requires an algorithm
Solution: 4mins
Testcases: 3mins

problem description

Algorithm: ...using sets as they're implemented in python, probably not the most efficient method, if there's anything better than O(n)
Time Complexity O(n) where n is the size of the input array
Space Complexity O(n) where n the amount of unique elements in the set

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
def DedupArray(inputArray):
    
    dupSet = set()
    
    inputSize = len(inputArray) - 1
    i = 0
    while i < inputSize:
        while i <= inputSize and inputArray[i] in dupSet:
            inputArray.pop(i)
            inputSize -= 1
            
        if i <= inputSize and inputArray[i] not in dupSet:
            dupSet.add(inputArray[i])
            i += 1
            
    return inputArray
                


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