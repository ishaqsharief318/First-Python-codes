import sys
import re

class Graph(object):
    
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

	
def create_graph(filename):
	filein = open(sys.argv[1], 'r')
	fileout = open(filename, 'w')

	for line in filein:
		if re.search('->', line):
			test= ' '.join(re.findall('[0-9]+', line))
			fileout.write(test)
			fileout.write(' \n')
	file2in = open('Clarified.dot', 'r')
	nodes = set()

	for line in file2in:
		nodes.add(re.split(" ",line)[0])
	#print nodes
	
	g = Graph()
	
	for node in nodes:
		g.add_node(node)

	#print g.nodes
	file2in = open('Clarified.dot', 'r')
	for line in file2in:
		#print (line)
		values = re.split(" ",line)
		#print (values)
		g.add_edge(values[0], values[1], values[2])

	for i in g.edges:
		print (i,":",g.edges[i])
		
	print g.distances
	return g

def dijkstra(g, initial_node):
    visited = {initial_node: 0}
    current_node = initial_node
    path = {}
    
    nodes = set(g.nodes)
    
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        cur_wt = visited[min_node]
        
        for edge in g.edges[min_node]:
            wt = cur_wt + g.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node
    		  #print path
    return visited, path

def shortest_path(g, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    route = [goal_node]

    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route
	

create_graph('Clarified.dot')
#print (dijkstra, path, shortest_path)