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
Time Complexity O(n*b) # we will be taking a single slide through the input string but also be searching the average len of the searched Set using the issubset function
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
"""

def ShortestSubstring(inputString, inputSubString):
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