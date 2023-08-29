
from collections import defaultdict

class Node:
    def __init__(self, id):
        self.id = id

class Arc:
    def __init__(self, start_node, end_node, cost_vector):
        self.start_node = start_node
        self.end_node = end_node
        self.cost_vector = cost_vector  # A list of costs for multiple objectives

class Graph:
    def __init__(self):
        self.nodes = {}
        self.arcs = defaultdict(list)
    
    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node
    
    def add_arc(self, start_id, end_id, cost_vector):
        start_node = self.nodes[start_id]
        end_node = self.nodes[end_id]
        arc = Arc(start_node, end_node, cost_vector)
        self.arcs[start_id].append(arc)
