"""
Peter Mora-Stevens
11:19 pm

MissingInteger
Time: 20mins for linear solution
Solution: 11mins
Testcases: 9mins

Given an integer n and a sorted array of integers size n-1 containing all integers in the range 1-n, find the missing integer

Algorithm: Binary Search
Time Complexity O(n) where n is the size of the given input array
Space Complexity O(n) where n is the length of the input array

Information we know
    - 

Edge Cases
    - the array is a single value, or empty, the output being 2 (if just 1) or 1, if empty
    
Assumptions
    - given that the ranges all start at the value 1, I'm going to assume that the problem is looking to have 1 be the starting input
    
Difficulties
    - 
    
Inital Approach
    - I know that a binary search solution is possible, but I can't think of how to implement it in time, so I will be starting with
    - a slower, linear time algorithm, essencially a sliding window.
    a) create a set to store the full range of the provided array, allowing for constant time lookup
    b) create a for loop and iterate through the provided range value
    c) return the value which does not appear in the set

"""
def MissingInteger(missingIntArray, rangeVal):
    searchSet = set(missingIntArray)
    
    # python range function is not inclusive, and starts at 0, this hard codes 1 as the first value checked,
    # and the +1 makes it inclusive, so at min, we're searching 1 to 1.
    for num in range(1, rangeVal + 1):
        if num in searchSet:
            continue
        else:
            return num

if __name__ == "__main__":
    
    # provided
    testcase, rangeVal = [1, 2, 3, 4, 6, 7], 7
    print("Actual: ", MissingInteger(testcase, rangeVal), "Expected: 5")
    testcase, rangeVal = [1], 2
    print("Actual: ", MissingInteger(testcase, rangeVal), "Expected: 2")
    testcase, rangeVal = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12
    print("Actual: ", MissingInteger(testcase, rangeVal), "Expected: 9")
    
    # edge-cases
    testcase, rangeVal = [], 1
    print("Actual: ", MissingInteger(testcase, rangeVal), "Expected: 1")
    