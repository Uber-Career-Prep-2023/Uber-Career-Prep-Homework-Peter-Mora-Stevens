"""
Peter Mora-Stevens
8:50pm

ReverseVowels
Time: 35mins
Solution: 25mins
Testcases: 10 mins


Given a string, reverse the order of the vowels in the string

Algorithm
Forward/Backward two-pointer
Time Complexity O(n) where n is the size of the input string
Space Complexity O(n) where n is the length of the input string, as strings in python are immutable

Information we know
    - There will be an input string which contains both upper and lowercase letters
    - the string may or may not contain any vowels
    - the string may be any length

Edge Cases
    - If the string is empty, return an empty string
    - check if there are numbers or values aside from alphabetical
    
Assumptions
    - 
    
Difficulties
    - Remembering how to modify a string given their immutable nature
    
Approach
    - Using a forward and backward two-pointer solution
    - Create a pointer at the first and last letters index
    - Create a set with the Vowel letters inside
    - Create a helper function for any values which are capital or lowercase english letters
    - Create a while loop with the condition that if the two indicies overlap or are equal, break
    - Iterate the pointers forward/backwards until we find a valid letter which is in the vowel set
    - Because strings are immutable in python, create an array of the list
    - Swap the two vowels at the indicies we know and merge back to a string, continue the process
    - Once the loop ends, return the string
"""

"""
first iteration
def ReverseVowels(inputString):
    l, r = 0, len(inputString) - 1
    
    inputArray = list(inputString)
    
    while l < r:
        if (inputArray[l] in vowels) and (inputArray[r] in vowels):
            inputArray[l], inputArray[r] = inputArray[r], inputArray[l]
            l += 1
            r -= 1
        elif (inputArray[l] not in vowels):
            l += 1
        else:
            r -= 1
    return ''.join(inputArray)
"""
# Time: O(n) -> create new array, iterate through array, create new string
# Space: O(n) -> storing vowels, creating list and string (python strs are immutable)
def ReverseVowels(s):
    s = list(s) # if inpt is allowed to be changed
                # else make a new list with those values in constructor
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    
    # two pointer traversal inwards with two cases
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] not in vowels: l += 1
        elif s[r] not in vowels: r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    return "".join(s)



if __name__ == "__main__":
    
    # provided
    
    testcase = "Uber Career Prep"
    print("Actual: ", ReverseVowels(testcase), "Expected: eber Ceraer PrUp")
    
    testcase = "xyz"
    print("Actual: ",ReverseVowels(testcase), "Expected: xyz")
    
    testcase = "flamingo"
    print("Actual: ", ReverseVowels(testcase), "Expected: flominga")
    
    # edge-cases
    testcase = "123 miami with an e 321" # numbers included
    print("Actual: ",ReverseVowels(testcase), "Expected: 123 meami with an i 321")
    
    testcase = "" # empty string
    print("Actual: ",ReverseVowels(testcase), "Expected: """)
    