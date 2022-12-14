
class Node:
    def __init__(self, name: str, pos: tuple[int, int], height: int):
        self.parent = None
        self.cost = float("inf")
        self.name = name
        self.pos = pos
        self.height = height
        self.neighbors = []

    def __repr__(self):
        return f"Node {self.name} at {self.pos}"

    def __eq__(self, other):
        return False if other == None else self.pos == other.pos
    
    def hash(self):
        return ":".join(map(str, [self.pos[0], self.pos[1]]))

def shortest_path_dijkstra(inp: str, start: tuple) -> int:
    """Returns the length of the shortest path leading from start to E."""
    to_visit = []
    visited = []
    length = 0

    current = Node("S", start, ord("a"))
    current.cost = 0

    to_visit.extend(find_neighbors(inp, current))
    while current.name != "E":
        for neighbor in find_neighbors(inp, current):
            if neighbor not in visited:
                if neighbor in to_visit:
                    for node in to_visit:
                        if node == neighbor:
                            neighbor = node
                else:
                    to_visit.append(neighbor)
                if current.cost + (current.height + 2) - neighbor.height < neighbor.cost:
                    neighbor.cost = current.cost + (current.height + 2) - neighbor.height
                    neighbor.parent = current
        to_visit.sort(key = lambda n: n.cost)
        if to_visit == []:
            return float("inf")
        current = to_visit[0]
        to_visit = to_visit[1:]
        visited.append(current)

    while current.name != "S":
        length += 1
        current = current.parent

    return length
                
def find_starts(inp: str, func):
    """Returns a generator that yields all positions with characters that have func evaluate to True."""
    for y, line in enumerate(inp.split("\n")):
        for x, char in enumerate(line):
            if func(char):
                yield (x, y)

def find_neighbors(inp: str, node) -> list:
    """Returns the neighbor nodes of node."""
    neighbors = []
    inp = inp.split("\n")
    node_x, node_y = node.pos
    for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        x_ = node_x + x
        y_ = node_y + y
        if 0 <= x_ and x_ < len(inp[0]) and 0 <= y_ and y_ < len(inp):
            char = inp[y_][x_]
            height = ord(char) if char != "E" else ord("z")
            if node.height + 1 >= height:
                neighbors.append(Node(char, (x_, y_), height))
    return neighbors

def shortest_paths_floyd_warshall(inp: str):
    pass

def parse_graph(inp: str) -> dict:
    """Returns a graph as a dictionary with the nodes as keys and their neighbors (list) as the values."""
    nodes = dict()

def collect_nodes(lines: list, nodes: dict):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if f"{x}:{y}" in nodes.keys():
                return nodes[f"{x}:{y}"]
    
            node = Node(char, (x, y), ord(char) - ord("a"))
            nodes[f"{x}:{y}"] = node
    
            if 0 <= x - 1:
                if f"{x - 1}:{y}" in nodes.keys():
                    temp = nodes[f"{x - 1}:{y}"]
                else:
                    temp_char = line[x - 1]
                    temp = Node(temp_char, (x - 1, y), ord(temp_char) - ord("a"))
                    nodes[f"{x - 1}:{y}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)
            if x + 1 < len(lines[y]):
                if f"{x + 1}:{y}" in nodes.keys():
                    temp = nodes[f"{x + 1}:{y}"]
                else:
                    temp_char = line[x + 1]
                    temp = Node(temp_char, (x + 1, y), ord(temp_char) - ord("a"))
                    nodes[f"{x + 1}:{y}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)
            if 0 <= y - 1:
                if f"{x}:{y - 1}" in nodes.keys():
                    temp = nodes[f"{x}:{y - 1}"]
                else:
                    temp_char = lines[y - 1][x]
                    temp = Node(temp_char, (x, y - 1), ord(temp_char) - ord("a"))
                    nodes[f"{x}:{y - 1}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)
            if y + 1 < len(lines):
                if f"{x}:{y + 1}" in nodes.keys():
                    temp = nodes[f"{x}:{y + 1}"]
                else:
                    temp_char = line[y + 1]
                    temp = Node(temp_char, (x, y + 1), ord(temp_char) - ord("a"))
                    nodes[f"{x}:{y + 1}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)

    print("test")
    print(type(nodes))
    return nodes



if __name__ == "__main__":
    testinput = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    with open("12/input.txt") as file:
        fileinput = file.read()
        #print("Puzzle 01:", shortest_path_dijkstra(fileinput, next(find_starts(fileinput, lambda c: c == "S")))) # 8s to solve puzzle 01, what??
        #print("Puzzle 02:", min(map(lambda start: shortest_path_dijkstra(fileinput, start), find_starts(fileinput, lambda c: c in ("a", "S"))))) # consider using floyd-warshall or bellman-ford starting from E next time, doofus
    print(collect_nodes(testinput.split("\n"), dict()))
