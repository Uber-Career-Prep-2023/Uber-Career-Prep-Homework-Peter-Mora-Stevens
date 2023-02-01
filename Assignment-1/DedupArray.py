
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
Space Complexity O(n) where n is the size of the input array

Information we know
    - we are given a list of duplicating integers

Edge Cases
    - Array is empty, return empty array
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    - create a set, store the input array in the set to remove duplicates, return the set as a list
    a) 

"""
def DedupArray(inputArray):
    inputSet = set(inputArray)
    return list(inputSet)


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