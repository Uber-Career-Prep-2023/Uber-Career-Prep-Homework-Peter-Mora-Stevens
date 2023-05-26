from collections import deque

"""
Peter Mora-Stevens
11:45 am

problem_name
Time: 30 mins
Solution: 15 mins
Testcases: 15 mins

problem description

Algorithm/DS: graph bfs
Time Complexity O(n*m) we must visit every node in the graph worst case
Space Complexity O(n*m) worst case is that we must store every node in the visited set
Updated Space (1) - does not have any memory used

Assumptions - I'm going to be using strings for the numbers

Approach pseduocode
- iterate through 2d matrix, if we see land, represented by 1's, add one to count and add all land nodes to visit set
    - updated approach, reduce time complexity down to O(1) by changing visited value to 0's
- cases to check: if the nodes neighbors are out of bounds, water, or in the visited set, don't add to queue
"""

def num_islands(board):
    ROW, COL = len(board), len(board[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    count = 0
    
    def bfs(r, c):
        q = deque()
        # start bfs by appending the first node to the queue
        q.append((r,c))
        # and set first node to 0, as to not visit it again
        board[r][c] = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                # if any of the movements are out of bounds or not an island node, skip
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if ((min(row, col) < 0) or
                        (row == ROW or col == COL) or
                        (board[row][col] != 1)):
                        continue
                    
                    # if the node is confirmed in-range and island node, add to q
                    # turn to node to a 0, as we'll be just checking it's neighbors and the node itself
                    q.append((row,col))
                    board[row][col] = 0
                    
                           
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 1:
                count += 1
                bfs(r, c)
    return count

if __name__ == "__main__":
    
    # provided
    board = [[1,1,1,1,0],
             [1,1,0,1,0],
             [1,1,0,0,0],
             [0,0,0,0,0]]
    
    print("Actual: ", num_islands(board), "Expected: 1")
    
    board = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
    print("Actual: ", num_islands(board), "Expected: 3")
    
    board = [[1,0,1,1,1],
            [1,1,0,1,1],
            [0,1,0,0,0],
            [0,0,0,1,1],
            [0,1,0,0,0]]
    print("Actual: ", num_islands(board), "Expected: 4")
    
    board = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    print("Actual: ", num_islands(board), "Expected: 0")
    
    board = [[1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]]
    print("Actual: ", num_islands(board), "Expected: 1")