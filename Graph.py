from typing import Dict, List, Callable
import networkx as nx

from EdgeType import *
from Edge import *
from Vertex import *
from queue import Queue

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data, len(self.adjacencies))
        list_of_adjacencies = []
        self.adjacencies[new_vertex] = list_of_adjacencies
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_edge)

    def add_undirected_edge(self,  source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_edge)
        self.adjacencies[destination].append(new_edge)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        queue = Queue()
        first = None
        for vertex in self.adjacencies.keys():
            if vertex.index == 'v0':
                first = vertex
        visited = [first]
        queue.enqueue(first)
        while queue:
            v = queue.dequeue()
            visit(v)
            for edge in self.adjacencies[v]:
                neighbour = edge.destination
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.enqueue(neighbour)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        v = None
        visited = []
        for vertex in self.adjacencies.keys():
            if vertex.index == 'v0':
                v = vertex

        def dfs(graph, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
            visit(v)
            visited.append(v)
            for edge in graph.adjacencies[v]:
                neighbour = edge.destination
                if neighbour not in visited:
                    dfs(graph, neighbour, visited, visit)

        dfs(self, v, visited, visit)

    def show(self):
        viusal_graph = nx.Graph()
        for key in self.adjacencies.keys():
            viusal_graph.add_node(key)
            for edge in self.adjacencies[key]:
                viusal_graph.add_edge(edge.source, edge.destination)

        for key in self.adjacencies.keys():
            list_of_edges = []
            for edge in viusal_graph.edges:
                if edge[0].data == key.data:
                    list_of_edges.append(f'{edge[1].data}: v{edge[1].index}')
                elif edge[1].data == key.data:
                    list_of_edges.append(f'{edge[0].data}: v{edge[0].index}')

            print(f'- {key.data}: v{key.index} ----> {list_of_edges}')