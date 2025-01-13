from typing import Union

from Edge import Edge
from Node import Node


class Graph:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(j) for j in range(num_nodes)]

    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, None]:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        return self.nodes[from_node].get_edge(to_node)

    def is_edge(self, from_node: int, to_node: int) -> bool:
        return self.get_edge(from_node, to_node) is not None

    def make_edge_list(self) -> list:
        all_edges: list = []
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)
        return all_edges

    def insert_edge(self, from_node: int, to_node: int, weight: float):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        self.nodes[from_node].add_edge(to_node, weight)
        if self.undirected:
            self.nodes[to_node].add_edge(from_node, weight)

    def remove_edge(self, from_node: int, to_node: int):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        self.nodes[from_node].remove_edge(to_node)
        if self.undirected:
            self.nodes[to_node].remove_edge(from_node)


    def make_copy(self):
        g2: Graph = Graph(self.num_nodes, undirected=self.undirected)
        for node in self.nodes:
            g2.nodes[node.index].label = node.label
            for edge in node.edges.values():
                 g2.insert_edge(edge.from_node, edge.to_node, edge.weight)
        return g2
    def insert_node(self, label=None) -> Node:
        new_node: Node = Node(self.num_nodes, label=label)
        self.nodes.append(new_node)
        self.num_nodes += 1
        return new_node

    def get_in_neighbors(self, target: int) -> set:
        neighbors: set = set()
        for node in self.nodes:
            if target in node.edges:
                neighbors.add(node.index)
        return neighbors

if __name__ == '__main__':
    g: Graph = Graph(5, undirected=False)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 3.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(1, 4, 1.0)
    g.insert_edge(3, 4, 3.0)
    g.insert_edge(4, 2, 3.0)
    g.insert_edge(4, 3, 3.0)
    for node in g.nodes:
        print(node.index, end='\t')
        for edge in node.edges.values():
            print(edge.to_node, end='\t')
        print()

        for edge2 in node.get_sorted_edge_list():
            print(edge2)