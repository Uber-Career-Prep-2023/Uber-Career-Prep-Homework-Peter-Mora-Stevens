"""
Peter Mora-Stevens
9:43 am

Prerequisite Courses
Time: 45mins
Solution: 30mins
Testcases: 15mins

Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, 
return a valid order for them to take their courses assuming they only take one course for their major at once.

Algorithm/DS: DFS topological sort
Time Complexity O(V + E) where V is the number of verticies and E is the number of edges
Space Complexity O(V + E) the set of visited nodes will contain V + E nodes

Approach pseduocode
    Create adj list and set to sort visited nodes
    loop through every node from the input array and dfs if not visited
    we assume paths could exist, so check our current dfs path with path set
    append to topological sort once dfs has returned back to it
    since our ordering wants lowest/earliest level course first, don't reverse topo array
"""
def prereq_course(courses, prereqs):
    # checking for any courses which are in courses list and not in prereq map
    adj = {course:[] for course in courses}
    for course, prereq in prereqs.items():
        for pre in prereq:
            adj[course].append(pre)
        
    visited = set()
    path = set()
    topo_sort = []
    def dfs(course):
        # valid case of finding a prereq we previously visited earleir
        if course in path:
            return False
        if course in visited:
            return True
        # invalid case means we have a cycle and searched same node in one dfs
        
        # add node to path and visited set
        visited.add(course)
        path.add(course)
        # if any single path had an invalid case we'd return false back to root call returning empty array
        for pre in adj[course]:
            if not dfs(pre): return False
        # add the course after we returned up, remove node from current path
        topo_sort.append(course)
        path.remove(course)
        # if we make it here, return true since we finished visiting all neighbors up to this point
        return True
    
    for course in courses:
        if not dfs(course): return []
    return topo_sort

if __name__ == "__main__":
    
    # provided
    courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereqs = {"Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"]}
    print("Actual: ", prereq_course(courses, prereqs), "Expected: [Intro to Programming, Data Structures, Advanced Algorithms, Operating Systems, Databases]")

    courses = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    prereqs = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
    print("Actual: ", prereq_course(courses, prereqs), "Expected: [Intro to Writing, Plays & Screenplays, Contemporary Literature, Ancient Literature, Comparative Literature]")
    
    # no pre reqs
    courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereqs = {}
    print("Actual: ", prereq_course(courses, prereqs), "Expected: [Intro to Programming, Data Structures, Advanced Algorithms, Operating Systems, Databases]")
    
    courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereqs = {"Intro to Programming": ["Data Structures"], "Data Structures": ["Intro to Programming"]}
    print("Actual: ", prereq_course(courses, prereqs), "Expected: []")