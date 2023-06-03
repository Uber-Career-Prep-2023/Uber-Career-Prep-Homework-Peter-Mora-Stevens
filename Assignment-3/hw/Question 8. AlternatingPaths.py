from collections import deque

"""
Peter Mora-Stevens
12:20 pm

Question 8. Alternating Paths
Time: 40mins
Solution: 30mins
Testcases: 10mins

Question 8: AlternatingPath
Given an origin and a destination in a directed graph in which edges can be blue or red,
determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color.
Return -1 if no such path exists.


Algorithm/DS: Graph BFS w/ searching case of switching paths
Time Complexity O(V + E)
Space Complexity O(V + E)

Create a bfs which starts from the input node, which goes to the result node.
Only add nodes which are not the current color, as we know that would be the other color (red/blue).
return target if found, if search is done and no target found, return -1
"""

def alternating_paths(start, target, edges):
    if not edges: return -1
    
    adj = {}
    for src, dst, color in edges:
        adj[src] = adj.get(src, []) + [[dst, color]]
    
    visit = set()
    q = deque()
    # set to 0, as it's a default node and allows me to explore any path
    q.append((start, 0, 0))
    
    while q:
        for _ in range(len(q)):
            src, color, level = q.popleft()
            if src == target: return level
            
            visit.add((src, color))
            for neigh, n_color in adj[src]:
                if n_color != color and (neigh, n_color) not in visit: q.append((neigh, n_color, level + 1))
    return -1
        


if __name__ == "__main__":
    
    # provided
    edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
    start, target = "A", "E"
    print("Actual: ", alternating_paths(start, target, edges), "Expected: 4")
    
    edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
    start, target = "E", "D"
    print("Actual: ", alternating_paths(start, target, edges), "Expected: -1")
    
    # my own, but just testing logic w/ new node
    edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red"), ("E", "Z", "red")]
    start, target = "A", "Z"
    print("Actual: ", alternating_paths(start, target, edges), "Expected: 5")
    
    edges = []
    start, target = "E", "B"
    print("Actual: ", alternating_paths(start, target, edges), "Expected: -1")
    edges = None
    start, target = "E", "B"
    print("Actual: ", alternating_paths(start, target, edges), "Expected: -1")
    
    
    
    