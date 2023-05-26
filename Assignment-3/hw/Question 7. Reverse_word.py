"""
Peter Mora-Stevens
12:45 pm

problem_name
Time: 20mins
Solution: 10 mins
Testcases: 10 mins

problem description

Given a string, return the string with the order of the space-separated words reversed

Algorithm/DS: Stack - add values to a stack return concatinated string
Time Complexity O(w+n) - where w is the number of words, and then combines the words together
Space Complexity O(w+n) - stores every word element, then concatinates it as a string

Approach pseduocode

- using a stack, we'll split the word given the hint "space seperated" words.
- append to the stack in reverse, concatinate, and return
"""

def word_reverse(words):
    # technically we could even just return words reversed which would do exactly what I did here
    words = words.split(" ")
    stack = []
    for word in words[::-1]:
        stack.append(word)
        
    return " ".join(stack)

if __name__ == "__main__":
    
    # provided
    words = "Emma lives in Brooklyn, New York."
    print("Actual: ", word_reverse(words), "   Expected: York. New Brooklyn, in lives Emma")
    
    words = "Uber Career Prep"
    print("Actual: ", word_reverse(words), "   Expected: Prep Career Uber")
    
    words = "Prep Career Uber"
    print("Actual: ", word_reverse(words), "   Expected: Uber Career Prep")
    
    words = "This_won't_change"
    print("Actual: ", word_reverse(words), "   Expected: This_won't_change")

    