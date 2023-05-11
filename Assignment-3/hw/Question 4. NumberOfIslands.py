"""
Peter Mora-Stevens
00:00 am/pm

problem_name
Time: __mins
Solution: __mins
Testcases: __mins

problem description

Algorithm/DS: graph bfs
Time Complexity O(n*m) we must visit every node in the graph
Space Complexity O(n*m) worst case is that we must store every node in the visited set

Approach pseduocode
- iterate through 2d matrix, if we see land, represented by 1's, add one to count and add all land nodes to visit set
- cases to check: if the nodes neighbors are out of bounds, water, or in the visited set, don't add to queue
"""


if __name__ == "__main__":
    
    # provided
    testcase = ""
    print("Actual: ", function(), "Expected: ")