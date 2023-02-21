"""
Peter Mora-Stevens
11:34 am

TwoSum
Time: __mins
Solution: __mins
Testcases: __mins

problem description

Algorithm: Variable size sliding window 
Time Complexity O(n^2) - where n is the size of the array and we need to look at every element once per loop and we do n loop
Space Complexity O(1) - no extra memory will be allocated to this solution

Information we know
    - There are two inputs, nums and k, where nums is the list of numbers and k is the value we're trying to sum to
    - we return the count of k sums in the array

Edge Cases
    - the input array is Null, the input array is empty, there is no k sum in the array 
    
Assumptions
    - the input array is unsorted
    
Difficulties
    - finding a more efficient method of searching the array using a hashmap, can't think of one off the top of my head
    
Approach
    -
    a) set a right pointer starting on the end of the array,
    b) initialize a for loop L which starts from the beginning of an array.
       while loop internally, check while r > l, decrement right and check if the sum of the current value of both is == to k
    c) if we find a combo, add to count

"""


def TwoSum(nums, k):
    
    if not nums or len(nums) == 0:
        return 0
    
    numPairs = 0
    
    for l in range(len(nums)):
        r = len(nums) - 1
        while r > l:
            if (nums[l] + nums[r]) == k:
                numPairs += 1
            r -= 1
                
    return numPairs


if __name__ == "__main__":
    
    # provided
    nums, k =  [1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10
    print("Actual: ", TwoSum(nums, k), "Expected: 3")
    
    nums, k = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8
    print("Actual: ", TwoSum(nums, k), "Expected: 3")
    
    nums, k = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6
    print("Actual: ", TwoSum(nums, k), "Expected: 5") # 5 expected even though 6 was there, the pairs show this on the page
    
    nums, k = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1
    print("Actual: ", TwoSum(nums, k), "Expected: 0") # no values can ve found
    
    # edge cases
    nums, k = [], 3
    print("Actual: ", TwoSum(nums, k), "Expected: 0") # nums is empty
    
    nums, k = None, 1
    print("Actual: ", TwoSum(nums, k), "Expected: 0") # nums is null