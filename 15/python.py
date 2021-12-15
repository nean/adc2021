import typing
import os
import collections
import heapq

InputDataType = typing.List[typing.List[int]]


class CaveGraph:
    def __init__(self, risk_matrix: InputDataType) -> None:
        self.graph = collections.defaultdict(list)
        self.risk_matrix = risk_matrix

    def add_node(self, fro, to):
        self.graph[fro].append(to)

    def get_edges(self, node):
        return self.graph[node]

    def get_risk(self, node):
        return self.risk_matrix[node[0]][node[1]]


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]) -> InputDataType:
    cleaned_lines = []

    for line in lines:
        cleaned_lines.append([int(i) for i in list(line.removesuffix("\n"))])

    return cleaned_lines


def dijkstra(graph: CaveGraph, start_node, end_node):
    node_queue = []
    heapq.heappush(node_queue, (0, start_node))
    risk_values = {}
    risk_values[start_node] = 0
    visited = {}

    while node_queue:
        current_min_node = heapq.heappop(node_queue)[1]

        if current_min_node == end_node:
            return risk_values[end_node]

        for neighbor in graph.get_edges(current_min_node):
            if neighbor in visited:
                continue

            tentative_risk = risk_values[current_min_node] + graph.get_risk(neighbor)
            if neighbor not in risk_values or tentative_risk < risk_values[neighbor]:
                risk_values[neighbor] = tentative_risk
                heapq.heappush(node_queue, (0, neighbor))


def build_graph(g, data):
    for j, row in enumerate(data):
        for i, risk in enumerate(row):
            if i + 1 < len(row):
                g.add_node((i, j), (i + 1, j))

            if j + 1 < len(data):
                g.add_node((i, j), (i, j + 1))

            if j - 1 > 0:
                g.add_node((i, j), (i, j - 1))

            if i - 1 > 0:
                g.add_node((i, j), (i - 1, j))


def part1(data: InputDataType):
    g = CaveGraph(data)

    build_graph(g, data)

    shortest_paths = dijkstra(g, (0, 0), (len(data) - 1, len(data) - 1))

    return shortest_paths


def part2(data: InputDataType):
    data_length = len(data)

    new_data = [[] for i in range(data_length * 5)]

    for y in range(data_length * 5):
        y_add = int(y / data_length)
        for x in range(data_length * 5):
            x_add = int(x / data_length)
            new_data[y].append(
                (data[y % data_length][x % data_length] + y_add + x_add - 1) % 9 + 1
            )

    g = CaveGraph(new_data)

    build_graph(g, new_data)

    shortest_paths = dijkstra(g, (0, 0), (data_length * 5 - 1, data_length * 5 - 1))

    return shortest_paths


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
