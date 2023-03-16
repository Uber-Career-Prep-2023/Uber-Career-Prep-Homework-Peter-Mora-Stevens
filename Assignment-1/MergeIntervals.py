"""
Peter Mora-Stevens
12:14 pm

MergeIntervals
Time: 26mins
Solution: 21mins (forgot to sort... trouble shot for so long, need to slow down and think through my answer before I over work it)
Testcases: 5mins

Given a list of integer pairs representing the low and high end of an interval, inclusive,
return a list in which overlapping intervals are merged

Algorithm: sort then solve
Time Complexity O(nlogn) - sorting the input list takes nlogn time, and using a linear search is still linear, but the worst time complexity is nlogn so we don't care about the linear search
Space Complexity O(n) - our output array will be size n, where n is at worst case, the entire input array

Information we know
    - the input can be unsorted
    - 

Edge Cases
    - The input is null, the input is empty
    
Assumptions
    - 
    
Difficulties
    - 
    
Approach
    - first sort
    a) When we display the problem visually, it becomes fairly intuitive on how to solve this problem.
    b) since we know the rules of an interval, we can simply check two cases
        1) if the first value of the next pair is greater than the second value entirely of the previously appended value, we append and increment an indexing value
        2) if the next pair's first value is less than or equal to the previously appended pairs second value, we change to make the second value of previous pair the max value between the two's second values
            - we have to do this second because we want to append the first value and not mess up the mergeI index value
    c) return the output array

"""

def MergeIntervals(intervals):
    if not intervals or len(intervals) == 0:
        return []
    
    intervals.sort()
    
    merged = [list(intervals[0])]
    
    for interval in intervals:
        if interval[0] > merged[-1][1]:
            merged.append(list(interval))
        elif interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged



if __name__ == "__main__":
    
    # provided
    intervals = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
    print("Actual: ", MergeIntervals(intervals), "Expected: [(4, 8), (1, 3), (9, 12)]")
    
    intervals = [(5, 8), (6, 10), (2, 4), (3, 6)]
    print("Actual: ", MergeIntervals(intervals), "Expected: [(2, 10)]")
    
    intervals = [(10, 12), (5, 6), (7, 9), (1, 3)]
    print("Actual: ", MergeIntervals(intervals), "Expected: [(10, 12), (5, 6), (7, 9), (1, 3)]")
    
    
    # edgecases
    intervals = None
    print("Actual: ", MergeIntervals(intervals), "Expected: []")
    intervals = []
    print("Actual: ", MergeIntervals(intervals), "Expected: []")
    