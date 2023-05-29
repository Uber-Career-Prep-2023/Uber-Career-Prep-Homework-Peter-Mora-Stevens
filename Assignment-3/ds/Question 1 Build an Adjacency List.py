from collections import deque

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

# dfs from one node to target
# O(E) - time (where E is the number of edges in the graph)
# O(E) - space (call stack - recursion)
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


# bfs checking the path from the starting node to the target node is in the graph
# O(E) time - where E is the number of Edges in the graph
# O(E) space - queue could hold all Edges in the graph
def bfs(start, target, neighbors):
    q = deque([start])
    visit = set()
    
    if not start:
        return False
    
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            visit.add(start)
            
            for neighbor in neighbors[curr]:
                if neighbor == target:
                    return True
                q.append(neighbor)
    return False

# this assumes our input is numbered in the range 0 to n
# Time Complexity - O(V + E) that is, the number of Vertices and the number of Edges
def topological(num_edges, adj):
    res = []
    visit = set()
    path = set()
    def topo_dfs(node):
        if node in path:
            # we have a cycle
            return False
        if node in visit:
            # just fine, we've visited before, just don't add again
            return True

        path.add(node)
        visit.add(node)
        # check all the neighbors until we reach end of the search
        for neighbor in adj[node]:
            topo_dfs(neighbor)
        path.remove(node)
        res.append(node)
        return True
    
    for i in range(1, num_edges):
        # this would mean an invalid topological sort
        if not topo_dfs(i): return []
    #res.reverse()
    return res

if __name__ == "__main__":
    
    # provided
    testcase = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    print("Actual: ", make_adj_list(testcase), "Expected: 0: [], 1: [0], 2: [0], 3: [2,1]")
    print(dfs(1, 3, make_adj_list(testcase), set()), "DFS")
    print(bfs(1, 0, make_adj_list(testcase)), "BFS")
    #testcase = [[1,0],[2,0],[3,1],[3,2]]
    #print(topological(4, make_adj_list(testcase)), "Topological sort")
    testcase = [[6,3],[6,5],[3,2],[5,4],[3,2],[4,1],[2,1]]
    print(topological(7, make_adj_list(testcase)), "Topological sort")
    
    testcase = [("Hello", "Friend"), ("Bye", "Guy"), ("Lie", "Chai"), ("Lie", "Bye")]
    print("Actual: ", make_adj_list(testcase), "Expected: Hello: [Friend], Bye: [Guy], Lie: [Chai, Bye], Guy: [], Chai: []")