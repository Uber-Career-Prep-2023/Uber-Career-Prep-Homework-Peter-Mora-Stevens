"""
Peter Mora-Stevens
5:12 pm

KAnagrams
Time: 17mins
Solution: 8mins
Testcases: 9mins

Two strings are given, find if with k changes, you can create a valid anagram

Algorithm: Two moving pointers
Time Complexity O(n) where n is the length of the two strings
Space Complexity O(n) where n is the number of elements in the strings

Information we know
    - 

Edge Cases
    - If the two inputs aren't the same length, return false
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    -
    a) loop through both the inputs and store in two hashmaps
    b) create a count variable
    c) check through the first input and check if the second one has the value
    d) if not, increase count variable, if count variable is greater than k return false
    e) once done, return true
"""

def KAnagrams(k, inputStringOne, inputStringTwo):
    mapOne, mapTwo = {}, {}
    count = 0
    
    if len(inputStringOne) != len(inputStringTwo):
        return False
    
    for i in range(len(inputStringOne)):
        mapOne[inputStringOne[i]] = 1 + mapOne.get(inputStringOne, 0)
        mapTwo[inputStringTwo[i]] = 1 + mapTwo.get(inputStringTwo, 0)
    for c in mapOne:
        if mapOne[c] != mapTwo.get(c, 0):
            count += 1
            if count > k:
                return False
    return True
        
if __name__ == "__main__":
    
    # provided
    k, inputStringOne, inputStringTwo = 1, "apple", "peach"
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: False")
    
    k, inputStringOne, inputStringTwo = 2, "apple", "peach"
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: True")
    
    k, inputStringOne, inputStringTwo = 3, "dog", "cat"
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: True")
    
    k, inputStringOne, inputStringTwo = 1, "debit curd", "bad credit"
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: True")
    
    k, inputStringOne, inputStringTwo = 2, "baseball", "basketball" # different sizes
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: False")
    
    # edge-case
    k, inputStringOne, inputStringTwo = 1, "", "" # two empty strings
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: True")
    
    k, inputStringOne, inputStringTwo = 5, "", "peach" # one empty string, but not the same size
    print("Actual: ", KAnagrams(k, inputStringOne, inputStringTwo), "Expected: False")
    