from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph
from queue import PriorityQueue as PQ


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set(start_node)  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    rest_set.remove(start_node)
    
    mst_edges = set()  # set of edges constituting MST
    
    pq = PQ()
    current = start_node
    while rest_set:
    	for neighbor in G.neighbors(current):
    		if neighbor in rest_set:
    			pq.put([G[current][neighbor]['weight'], current, neighbor])
    
    	nodeFirstDone, nodeSecDone = None, current
    	while (current == nodeSecDone):
    		firstNode, secNode = pq.get()[1:]
    		if (secNode in rest_set):
    			nodeFirstDone = firstNode
    			nodeSecDone = secNode
    	
    	mst_edges.add((nodeFirstDone, nodeSecDone))
    	current = nodeSecDone
    	
    	rest_set.remove(nodeSecDone)

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    #plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
