"""

UNABLE TO FIND RIGHT ANSWER

Stuck on finding the correct way to compare a slice of a string to the characters in another subString

Peter Mora-Stevens
11:51 pm

ShortestSubstring
Time: __mins
Solution: ~40mins (no time to do anything else)
Testcases: unable to get to (added after the 40 minutes just to test my solution for my own curiosity of if it worked)

problem description

Algorithm: Variable Size Sliding Window
Time Complexity O(n^2) # we will be taking a single slide through the input string but also be searching the average len of the searched Set using the issubset function
Space Complexity O(k) # where k is the average len of the substrings searched

Edge Cases
    - If the input is empty
    - If the input is Null
    - If the sub string is empty but the input is valid
    
Assumptions
    - I assume that the input string will always be >= the substring
    
Difficulties
    - Finding a way to efficiently search for the characters
    - Knowing how to compare two sets
    
Inital Approach - Not entirely used
    - using a variable size sliding window
    - a) Create a set to store the searched substring
    - b) initialize two pointers, at 0 and 1 and a count variable to store min len of the substring searched
         start a while loop which ends once right pointer reaches the end of the string
    - c) if input substring is in the set, store the difference of right index - left in the count variable
    - d) once the substring is in the set, iterate the left pointer until the substring is no longer in the set
    - e) once the substring is no longer in the set, iterate right pointer and continue algorithm
    - f) return the count variable
    
New Approach - counting value occurances
    - a) create two maps for character counting
         while all the elements of the inputSubSequence aren't in section of the main string
         continue adding characters
    - b) once there are values all the values
         start incrementing the left pointer and removing the values at that index from the count map
         keep a count variable which updates each time a value is removed storing the min value
    - c) return the count value
         
         
Final Approach - check if we have all required values for checking.
        using have and need, we can see if we are able to search the map (have must == need)
        if yes, then loop and iterate count to be the smallest window
        remove the value at left pointer from the counter map
        if that value is less than the substring counter map decrement have
        decrement left and continue while loop or go back to forloop
"""

def ShortestSubstring(inputString, inputSubString):
    
    if (not inputString or not inputSubString) or (len(inputString) == 0 or len(inputSubString) == 0):
        return 0
    
    inputStringMap = {}
    inputSubStringMap = {}
    
    count = len(inputString)
    
    for c in inputSubString:
        inputSubStringMap[c] = 1 + inputSubStringMap.get(c, 0)
    
    l = 0
    have, need = 0, len(inputSubStringMap)
    
    for r in range(len(inputString)):
        inputStringMap[inputString[r]] = 1 + inputStringMap.get(inputString[r], 0)
        if inputStringMap[inputString[r]] == inputSubStringMap.get(inputString[r], 0):
            have += 1
        
        while have == need:
            count = min(count, (r - l + 1))
            inputStringMap[inputString[l]] -= 1
            if inputStringMap.get(inputString[l], 0) < inputSubStringMap.get(inputString[l], 0):
                have -= 1
            l += 1
        
    return count
                    
    
    """
    matchSet = set()
    minSubString = 0
    
    l, r = 0, 1

    for c in inputSubString:
        matchSet.add(c)
    
    while r < len(inputString):
        searchSet = set()
        for c in inputString[l:r + 1]:
            searchSet.add(c)
        if matchSet.issubset(searchSet):
            minSubString = (r + 1) - l
            l += 1
        else:
            r += 1
    return minSubString
    """
if __name__ == "__main__":
    
    # provided
    inputString, inputSubString = "abracadabra", "abc"

    print("Actual: ", ShortestSubstring(inputString, inputSubString), "Expected: 4")
    inputString, inputSubString = "zxycbaabcdwxyzzxwdcbxyzabcvbazyx", "zzyzx"
    print("Actual: ", ShortestSubstring(inputString, inputSubString), "Expected: 10")
    inputString, inputSubString = "dog", "god"
    print("Actual: ", ShortestSubstring(inputString, inputSubString), "Expected: 3")
    
    # edge-cases
    inputString, inputSubString = "", "abc"
    print("Actual: ", ShortestSubstring(inputString, inputSubString), "Expected: 0")
    inputString, inputSubString = "abracadabra", ""
    print("Actual: ", ShortestSubstring(inputString, inputSubString), "Expected: 0")
    
    inputString, inputSubString = "ccccccab", "abc"
    print("Actual: ", ShortestSubstring(inputString, inputSubString), "Expected: 3")