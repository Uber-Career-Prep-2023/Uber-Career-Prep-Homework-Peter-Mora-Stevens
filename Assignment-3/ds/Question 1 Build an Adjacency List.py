"""
Peter Mora-Stevens

Question 1: Build an Adjacency List/Set Representation of a Graph

Given an array of pairs of values representing edges in an unweighted graph, 
create the equivalent adjacency list/set representation (a map from element to a list or set of elements). 
Pairs represent directed edges: (A, B) means there is an edge from A to B. 
If the pair (B, A) is also provided then there is an undirected edge between A and B. For simplicity, 
you may assume that each node of the graph stores an integer rather than a generic data type and that the elements are distinct. 
Implement a basic DFS and BFS searching for a target value and a topological sort (using either DFS or Kahn’s algorithm).

Algorithm/DS: Adjacency List - HashMap, DFS, Topological Sort

Approach pseduocode
    Given the array of pairs - representing edges, if either of the nodes (both source and destination) aren't in the map, add them,
    use empty array's as values.
"""

def make_adj_list(edges):
    nodes = {}
    
    for src, dst in edges:
        if src not in nodes:
            nodes[src] = []
        if dst not in nodes:
            nodes[dst] = []
        nodes[src].append(dst)
    
    return nodes
    
def dfs(node, target, adj_list, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adj_list[node]:
        count += dfs(neighbor, target, adj_list, visit)
    visit.remove(node)
    
    return count

if __name__ == "__main__":
    
    # provided
    testcase = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    print("Actual: ", make_adj_list(testcase), "Expected: 0: [], 1: [2, 3], 2: [0, 3], 3: [2]")
    print(dfs(1, 3, make_adj_list(testcase), set()))
    
    testcase = [("Hello", "Friend"), ("Bye", "Guy"), ("Lie", "Chai"), ("Lie", "Bye")]
    print("Actual: ", make_adj_list(testcase), "Expected: Hello: [Friend], Bye: [Guy], Lie: [Chai, Bye], Guy: [], Chai: []")
    