import typing
import os
import collections

InputDataType = typing.List[typing.Tuple[str, str]]


class CaveGraph:
    def __init__(self, paths: InputDataType, small_cave_visits: int = 1) -> None:
        self.graph = collections.defaultdict(list)
        self.mini_cave_visits = small_cave_visits

        for s, e in paths:
            self.add_node(s, e)
            self.add_node(e, s)

        # this is here just so i can debug the paths as listed by adc
        # for k, v in self.graph.items():
        #     self.graph[k] = sorted(v)

        self.reset()

    def reset(self):
        self.visited = {i: 0 for i in self.graph.keys()}
        self.current_path = []
        self.paths = []
        self.path_count = 0

    def add_node(self, f, t):
        if t != "start":
            self.graph[f].append(t)

    def enter_node(self, n):
        # increment visit_count for the current node and store in current_path
        self.visited[n] += 1
        self.current_path.append(n)

    def exit_node(self, n):
        # decrement the visit_count for the current node and pop it from the current_path
        self.visited[n] -= 1
        self.current_path.pop()

    def add_current_path(self):
        self.path_count += 1
        self.paths.append(self.current_path.copy())

    def get_paths_recursive(self, s: str, e: str):
        self.enter_node(s)

        # if current node is same as destination, then add it to paths
        if s == e:
            self.add_current_path()
        else:
            # get all visitable nodes from the current node
            # given the visit_counts
            for i in self.get_visitable_nodes(s):
                # print(s, e, i, visited, all_nodes)
                # recursively
                self.get_paths_recursive(i, e)

        self.exit_node(s)

    def get_paths(self, start: str = "start", end: str = "end"):
        self.reset()

        self.get_paths_recursive(start, end)

        return self.paths

    def get_visitable_nodes(self, node: str):
        # add a flag to check if a small cave is already visited twice
        small_cave_twice_visit = False
        if 2 in [v for k, v in self.visited.items() if k.upper() != k]:
            small_cave_twice_visit = True

        for i in self.graph[node]:
            # unvisited node add it to possible_nodes
            if self.visited[i] == 0:
                yield i
                continue

            # big cave
            if i.upper() == i:
                yield i
                continue

            # already visited a small cave once so skip
            if small_cave_twice_visit:
                continue

            # mini cave
            if self.visited[i] < self.mini_cave_visits:
                yield i
                continue


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]) -> InputDataType:
    cleaned_data = []
    for line in lines:
        i = line.removesuffix("\n").split("-")
        cleaned_data.append((i[0], i[1]))
    return cleaned_data


def part1(data: InputDataType):
    om = CaveGraph(data, 1)

    om.get_paths()

    return om.path_count


def part2(data: InputDataType):
    om = CaveGraph(data, 2)

    om.get_paths()

    return om.path_count


print(part1(clean_data(load_data("test1.txt"))))
print(part2(clean_data(load_data("test1.txt"))))

print(part1(clean_data(load_data("test2.txt"))))
print(part2(clean_data(load_data("test2.txt"))))

print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
