import sys
import re
#import pickle

class Graph(object):
    
    def __init__(djk):
        djk.nodes = set()
        djk.edges = {}
        djk.weights = {}
    
    def add_node(djk, value):
        djk.nodes.add(value)

    def add_edge(djk, from_node, to_node, weights):
        djk.edges.setdefault(from_node, [])
        djk.edges[from_node].append(to_node)
        djk.weights[(from_node, to_node)] = weights

	
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
		g.add_edge(values[0], values[1], int(values[2]))

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
	 
		#print ("MinNode:",min_node)
        	nodes.remove(min_node)
		current_wt = visited[min_node]


		for edge in g.edges[min_node]:
			wt = current_wt + g.weights[(min_node, edge)]
			if edge not in visited or wt < visited[edge]:
                		visited[edge] = wt
				path[edge] = min_node
				#print path
	
	return visited, path

def shortest_path(g, initial_node, final_node):
    weights, paths = dijkstra(g, initial_node)
    route = [final_node]

    while final_node != initial_node:
        route.append(paths[final_node])
        final_node = paths[final_node]

    route.reverse()
    return route
	
start_node = "s"
g = create_graph('Clarified.dot')
fo = open("Dijkstras.dot",'a')
fo.write("\ndigraph classgraph \n{\n")

	
start_node = input("Enter the start node:")
ns= "//Path of %s//" % (start_node)
fo.write(ns)
fo.write('\n')
start_node = str(start_node)
visited, path = dijkstra(g, start_node)
#print visited
#print path
for v in visited:
	path = shortest_path(g, start_node, v)
	for i in range(len(path) - 1):
		#print(":P")
		djkpath =(path[i]," -> ",path[i+1], "[weight = ", g.weights[(path[i], path[i+1])],"]")
		#print(path[i] -> path[i+1] [weight = g.weights[(path[i], path[i+1])]])
		finaldjk = " ".join(map(str, djkpath))
		fo.write(finaldjk)
		fo.write('\n')

fo.write('\n')
fo.write("}")
fo.write('\n')
fo.close()

