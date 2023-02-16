"""
Peter Mora-Stevens
2:02 pm

ZeroSumSubArrays
Time: 17mins
Solution: 11mins
Testcases: 6mins

Thinking a solution: Significantly longer, thinking of possible solutions over multipule days and it finally clicked

Given an array of integers, count the # of sub arrays which sum to 0

Algorithm: variable size sliding window
Time Complexity O(n) where n is the length of the input array
Space Complexity O(n) where n is the size of the set

Information we know
    - The input will have negative, positive, or zero value integers

Edge Cases
    - The input is NULL or empty
        if so, return 0
    - The first value is a 0, if so add 1 to count
    
Assumptions
    - 
    
Difficulties
    - Finding a way to create a solution in linear time and not creating a solution in 0(m*n) or finding every combination
    
Approach
    -
    a) Given the input, we can create a set to store the values we come across
    b) we know that as we increment a value, we can store the value created and compare with future iterations
    c) for example, 4 + 5 = 9, store this value in the set, and we know if the total value is ever == 9, there is a subset which == 0
    d) the set is used because we know that the set will have 0(1) look up time

"""

def ZeroSumSubArrays(inputArray):
    
    count = 0
    subArraySum = 0 # the value being checked against values in the set to see if we ever repeat values which means we have a subset which == 0
    storeSet = set()
    storeSet.add(0) # if 0 is seen, we know 0 is a 0 subarray
    
    # have not inputArray first as otherwise left to right checks throw an error
    if not inputArray or len(inputArray) == 0:
        return count
    
    for num in inputArray:
        subArraySum += num
        if subArraySum in storeSet:
            count += 1
        else:
            storeSet.add(subArraySum)
            
    return count


if __name__ == "__main__":
    
    # provided
    testcase = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    print("Actual: ", ZeroSumSubArrays(testcase), "Expected: 2")
    testcase = [1, 8, 7, 3, 11, 9]
    print("Actual: ", ZeroSumSubArrays(testcase), "Expected: 0 - input is only positive values")
    testcase = [8, -5, 0, -2, 3, -4]
    print("Actual: ", ZeroSumSubArrays(testcase), "Expected: 2 - was shown as 0, but I believe there are two cases")
    
    # edge cases
    testcase = []
    print("Actual: ", ZeroSumSubArrays(testcase), "Expected: 0 - input is empty")
    
    testcase = None # input is none
    print("Actual: ", ZeroSumSubArrays(testcase), "Expected: 0 - input is none")
    
    testcase = [1,-1,1,-1,1,-1,1,-1]
    print("Actual: ", ZeroSumSubArrays(testcase), "Expected: 4")
    
    