"""
Peter Mora-Stevens
2:08 pm

Vacation Desinations
Time: 40mins
Solution: 40+mins -> uncomplete, recieving values less than expected according to provided testcases
Testcases: 5mins

Given an origin city, a value k - which represents the maximum travel time, and a list of three values, a pair, which represent the destinations which can reach eachother
and a single value representing the time it takes to go between the two. We can assume that traveling between any city adds 1 hour of stop over time as well

Return the number of locations you can visit within k time from the origin city

Algorithm/DS: BFS -> undirected graph
Time Complexity O(V + E)
Space Complexity O(V + E)

Approach pseduocode
We will approach this problem with a BFS on a graph

Create adj list

case to skip current search -> if we've visited that city, don't add again -> continue
stop our search/return false if we reach a point where our k value is too large, return what we have at that point

"""

import collections

def vacationDest(origin, dest, k):
    if not dest or not k: return 0
    
    # populates the adj list -> undirected
    adj = collections.defaultdict(list)
    for src, dst, time in dest:
        adj[src].append((dst, time))
        adj[dst].append((src, time))
    
    # bfs
    count = 0
    visit = set()
    
    q = collections.deque([[origin, 0]])
    while q:
        for _ in range(len(q)):
            curr_city, curr_time = q.popleft()
            if curr_city in visit: continue
            if curr_time > k: continue
            visit.add(curr_city)
            
            for nei, time in adj[curr_city]:
                q.append((nei, time + curr_time + 1))
            if curr_city != origin:
                count += 1
    return count

if __name__ == "__main__":
    
    {'Boston': [('New York', 4), ('Newport', 1.5), ('Portland', 2.5)], 'New York': [('Boston', 4), ('Philadelphia.', 2)], 
     'Philadelphia': [('New York', 2), [("Washington, D.C.", 2.5)]], 'Newport': [('Boston', 1.5)], 'Washington, D.C.': [("Harper's Ferry", 1), ('Philadelphia', 2.5)], 
     "Harper's Ferry": [('Washington, D.C.', 1)], 'Portland': [('Boston', 2.5)], 'Philadelphia': [('Washington, D.C.', 2.5)]}
    
    # provided
    testcase = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
    
    origin, k = "New York", 5
    print("Actual: ", vacationDest(origin, testcase, k), "Expected: 2")
    
    origin, k = "New York", 7
    print("Actual: ", vacationDest(origin, testcase, k), "Expected: 4")
    
    origin, k = "New York", 8
    print("Actual: ", vacationDest(origin, testcase, k), "Expected: 5")