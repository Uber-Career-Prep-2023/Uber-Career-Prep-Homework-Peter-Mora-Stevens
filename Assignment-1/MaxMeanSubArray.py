"""
Peter Mora-Stevens
1/28/2023 5:00pm

Time: 10mins for solution
    : 15mins for testcases
MaxMeanSubArray

Algorithm: Fixed-Size Sliding Window
Time Complexity: O(n^2) where n is the size of the input array and we create slices which are possibly up to size n every iteration
Space Complexity: O(n) slicing takes O(n) space as we have to create a new array potentially the size of the input

Information we know
    - Values can be negatives
    - Unsorted arrray
    - Output values can be floats

Edge Cases to Check
    - if the k input is larger than the len of array
    - if array is empty
    
Assumptions
    - if no valid solution, return -1
    
Inital Approach
    
    initalize a max mean value
    Use a fixed sliding window of size k, if input array is valid
    while loop to check the values in the window
    use max function to see if the previous max is greater than the new mean
    stop if the end of the window hits the end of the array
    itterate max mean depending on the values
"""


"""
First iteration of the question

def MaxMeanSubArray(inputArray, k):
    
    maxMean = -1
    endWindow = k - 1
    
    if (len(inputArray) < k) or (not inputArray):
        return maxMean
    
    
    while endWindow != len(inputArray):
        maxMean = max(maxMean, (sum(inputArray[endWindow - k + 1:endWindow + 1]) / k))
        endWindow += 1
    return maxMean
"""












# second iteration
# Time: O(n)
# Space: O(1)
def MaxMeanSubArray(arr, k):
    mean, res = 0, 0
    l = 0
    
    for r, n in enumerate(arr):
        mean += n
        
        if r < k-1: continue
        
        res = max(res, mean/k) # make sure its deci division
        mean -= arr[l]
        l += 1
        
    return res


# main statement for test cases
if __name__ == "__main__":
    # provided
    testcase, k = [4, 5, -3, 2, 6, 1], 2
    print("Actutal: ", MaxMeanSubArray(testcase, k), "Expected: 4.5")
    testcase, k = [4, 5, -3, 2, 6, 1], 3
    print("Actutal: ", MaxMeanSubArray(testcase, k), "Expected: 3")
    # origninally thought it would be 1 according to the test case example, but I can't find a case in which the max wouldn't be [-1, -1, 6] = 4 and 4/k(3) or 1.333
    testcase, k = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 3
    print("Actutal: ", round(MaxMeanSubArray(testcase, k), 3), "Expected: 1.333__")
    testcase, k = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 4
    print("Actutal: ", MaxMeanSubArray(testcase, k), "Expected: 1.5")
    
    # extra
    testcase, k = [1, 2, 3], 3 # exactly the same size as the array, only one possible output
    print("Actutal: ", MaxMeanSubArray(testcase, k), "Expected: 2")
    
    
    # edge-cases
    testcase, k = [2, 3], 3 # k is larger than input array
    print("Actutal: ", MaxMeanSubArray(testcase, k), "Expected: -1 (array too small)")
    testcase, k = [], 3 # array is empty
    print("Actutal: ", MaxMeanSubArray(testcase, k), "Expected: -1 (array is empty)")
    