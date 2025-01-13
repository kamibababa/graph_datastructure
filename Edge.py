class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight
    def __str__(self):
        return f"{self.from_node}-->{self.to_node}"


if __name__ == '__main__':
    edge = Edge(1,2,3)
