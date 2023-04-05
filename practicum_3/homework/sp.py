from typing import Any

import networkx as nx

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {source_node: [None, 0]} 
    paths = {source_node: [source_node]} # key = destination node, value = list of intermediate nodes
    
    current = source_node
    visited = set()
    
    while len(shortest_paths) < len(G.nodes()):
    	visited.add(current)
    	
    	weightToCurrent = shortest_paths[current][1]
    	
    	for next in G.neighbors(current):
    		weight = G[current][next]['weight'] + weightToCurrent
    		
    		if next not in shortest_paths:
    			shortest_paths[next] = [current, weight]
    			paths[next] = paths[current] + [next]
    		else:
    			currentShortestWeight = shortest_paths[next][1]
    			if currentShortestWeight > weight:
    				shortest_paths[next] = [current, weight]
    	
    	nextDestinat = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
    	
    	current = min(nextDestinat, key=lambda x: nextDestinat[x][1])

    return paths


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    #plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    print(shortest_paths)
#    plot_graph(G)
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
