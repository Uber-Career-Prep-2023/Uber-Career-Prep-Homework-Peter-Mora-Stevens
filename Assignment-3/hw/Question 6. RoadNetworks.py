"""
Peter Mora-Stevens
1:50 pm

Question 6. Road Networks
Time: __mins
Solution: __mins
Testcases: __mins

In some states, it is not possible to drive between any two towns because they are not connected to the same road network. 

Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. 

(For example, a state in which all towns are connected by roads has 1 road network, 
and a state in which none of the towns are connected by roads has 0 road networks.)


Algorithm/DS: Graph DFS w/ adjacency list
Time Complexity O(V + E) - where V is the number of vertices and E is the number of edges
Space Complexity O(V + E) - where V is the number of vertices and E is the number of edges

Approach pseduocode
    take a dfs approach to the list of connections.
    
    for all elements in the list of cities, call a dfs on them
    - base case, if we run into a visited node, return
    - if there is no more roads, return
    
    increment count if we call a dfs on a road which is not visited
    
    return count
"""

def num_networks(cities, roads):
    if not roads:
        return 0
    visit = set()
    count = 0
    adj = {city:[] for city in cities}
    for src, dst in roads:
        adj[src].append(dst)
        adj[dst].append(src)
    print(adj)

    def dfs(node):
        if node in visit:
            return
        
        visit.add(node)
        for road in adj[node]:
            dfs(road)
        return

    for city in cities:
        if adj[city] and city not in visit:
            count += 1
            dfs(city)
    return count
    
if __name__ == "__main__":
    
    # provided
    cities = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
    roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    print("Actual: ", num_networks(cities, roads), "Expected: 2")
    
    cities = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print("Actual: ", num_networks(cities, roads), "Expected: 3") # output from the document said 2, but this should be 3
    
    cities = ["This", "Should", "return", "0"]
    roads = []
    print("Actual: ", num_networks(cities, roads), "Expected: 0")
