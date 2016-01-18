# Enter your code here. Read input from STDIN. Print output to STDOUT


cases = int(raw_input())

def short(graph, start, end, visited=[], distances={},predecessors={}):
    if start == end:
        path = []
        while end != None:
            path.append(end)
            end = predecessors.get(end,None)
        if not distances[start]:
            print -1
            return
        print distances[start]
        return distances[start], path[::-1]
    
    if not visited: distances[start] = 0
    try:
        for node in graph[start]:
            if node not in visited:
                nodedist = distances.get(node,101)
                tentdist = distances[start] + graph[start][node]
                if tentdist < nodedist:
                    distances[node] = tentdist
                    predecessors[node] = start
        visited.append(start)
        unvisiteds = dict((k, distances.get(k,101)) for k in graph if k not in visited)
        closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
        return short(graph,closestnode,end,visited,distances,predecessors)
    except:
        print -1
        return -1
    
for case in xrange(cases):
    boost = {} # dictionary for snakes / ladders
    graph = {} # dictionary of lists for graph of board
    
    # ladders        
    l = int(raw_input())
    for j in xrange(l):
        x,y = [int(x) for x in raw_input().split()]
        boost[x] = y
        
    # snakes
    s = int(raw_input())
    for k in xrange(s):
        x,y = [int(x) for x in raw_input().split()]
        boost[x] = y    
#    print 
    # normal dice roll (remove start points of snake and ladders)
    for i in xrange(1,101):
        if i not in graph: 
            graph[i] = {}
    #        print graph[i]
            for j in xrange(1,7):
                di = {}
                new = i + j            
                if new < 101 and new not in boost:
                    di[new] = 1
                    graph[i].update(di)
                
                # if destination is start of ladder or snake
                elif new in boost:
                    di[boost[new]] = 1  # replace destination with ladder/snake destination
                    graph[i].update(di)
                    graph[new] = {}   # start point of ladder or snakes should be isolated
    #print graph
    short(graph,1,100,[],{},{})
