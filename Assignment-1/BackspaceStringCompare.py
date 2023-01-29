"""
Peter Mora-Stevens
1/28/2023 10:50pm

Time: mins for solution
    : mins for testcases

BackspaceStringcompare
Algorithm: Two strings two-pointer
Time Complexity: O(n) where n is the size of the input string
Space Complexity: O(n) where n is the size of the input string, as we need to be able to remove values from the input string

Information we know
    - string contains letters which can be marked as ignored or deleted, denoted by a postfixed # sign

Edge Cases to Check
    - If the string turns out to be empty
    - If the removals make the string empty
    - Remove values that don't exist or first value is a #("#")
Assumptions
    - Even though characters such as nubmers or special characters appear, since we are using a string, their appearance won't impact the solution
    
Inital Approach
    - First, we will iterate through either string, checking for and removing values
    - which are marked as deleted
    - once the arrays are joined back we compare the len of the strings first
    - if they differ, return False
    - else, check the values and compare
    
"""
# remove backspaced values from strings
def removeBackspace(inputString):
    pointer = 0
    inputStringList = list(inputString)
    while pointer < len(inputStringList):
        if inputStringList[pointer] == "#" and pointer != 0:
            del inputStringList[pointer]
            del inputStringList[pointer - 1]
            pointer =- 1
        elif pointer == 0 and inputStringList[pointer] == "#":
            return False
        else:
            pointer += 1
            continue
    inputString = ''.join(inputStringList)
    return inputString

def BackspaceStringCompare(inputStringOne, inputStringTwo):
    if removeBackspace(inputStringOne) == False:
        return False
    else:
        inputStringOne = removeBackspace(inputStringOne)
    if removeBackspace(inputStringTwo) == False:
        return False
    else:
        inputStringTwo = removeBackspace(inputStringTwo)
    
    if len(inputStringOne) != len(inputStringTwo):
        return False
    else:
        i = 0
        while i < len(inputStringOne):
            if inputStringOne[i] == inputStringTwo[i]:
                i += 1
                continue
            else:
                return False
        return True
    
if __name__ == "__main__":
    
    # provided
    testcaseOne, testcaseTwo = "abcde", "abcde"
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: True")
    testcaseOne, testcaseTwo = "Uber Career Prep", "u#Uber Careee#r Prep"
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: True")
    testcaseOne, testcaseTwo = "abcdef###xyz", "abcw#xyz"
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: True")
    testcaseOne, testcaseTwo = "abcdef###xyz", "abcdefxyz###"
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: False")
    
    # edge-case
    testcaseOne, testcaseTwo = "abcde#####", "abcde#####" # Empty string
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: True")
    testcaseOne, testcaseTwo = "abcde#####", "abcde" # One empty string
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: False")
    testcaseOne, testcaseTwo = "", "" # two empty strings
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: True")
    testcaseOne, testcaseTwo = "#", "#" # value is deleting a value not there
    print("Actual: ", BackspaceStringCompare(testcaseOne, testcaseTwo), "Expected: False")