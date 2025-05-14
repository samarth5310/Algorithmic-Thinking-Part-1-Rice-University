"""
Project 1 - Degree distributions for graphs
Daoyuan Wang
"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 4: set([1]),
             5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]),
             5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """
    make a complete directional graph
    return a dictionary representation
    """
    complete_graph = {}
    for node in range(num_nodes):
        base_set = set()
        for node_single in range(num_nodes):
            base_set.add(node_single)
        base_set.remove(node)
        complete_graph[node] = base_set
    return complete_graph


def compute_in_degrees(digraph):
    """
    calculate in-degree of all nodes
    return a dictionary
    """
    in_degree = {}
    for key in digraph:
        in_degree[key] = 0
    for key in digraph:
        for dist in digraph[key]:
            in_degree[dist] += 1
    return in_degree


def in_degree_distribution(digraph):
    """
    calculate in-degree distribution
    return a dictionary
    """
    in_degree = compute_in_degrees(digraph)
    distribution = {}
    for key in in_degree:
        length = in_degree[key]
        if length in distribution:
            distribution[length] += 1
        else:
            distribution[length] = 1
    return distribution
