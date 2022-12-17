
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
                
def find_starts(inp: str, func):
    """Returns a generator that yields all positions with characters that have func evaluate to True."""
    for y, line in enumerate(inp.split("\n")):
        for x, char in enumerate(line):
            if func(char):
                yield (x, y)

def shortest_path_dijkstra(inp: str, start: tuple, goal: tuple, equalise_a: bool = False) -> int:
    lines = inp.split("\n")
    nodes = collect_nodes(lines)
    current = nodes[f"{start[0]}:{start[1]}"]
    current.cost = 0
    to_visit = list(nodes.values())
    visited = []
    func = weight_ if equalise_a else weight

    while to_visit != [] and current.pos != goal:
        for neighbor in current.neighbors:
            if neighbor not in visited:
                if neighbor.cost > current.cost + func(current, neighbor):
                    neighbor.cost = current.cost + func(current, neighbor)
                    neighbor.parent = current
        visited.append(current)
        to_visit.sort(key = lambda n: n.cost, reverse = True)
        current = to_visit.pop()
        
    return current.cost


def shortest_paths_floyd_warshall(inp: str) -> list:
    """Returns a two-dimensional list dist with the shortest path between nodes being dist[node1][node2] long."""
    lines = inp.split("\n")
    length = len(lines[0])
    nodes = collect_nodes(lines)
    dist = [[float("inf") for _ in range(len(nodes))] for _ in range(len(nodes))]
    
    for i in range(len(nodes)):
        dist[i][i] = 0
        x, y = translate_to_pos(length, i)
        node = nodes[f"{x}:{y}"]
        for neighbor in node.neighbors:
            dist[i][translate_to_int(length, neighbor.pos)] = weight(node, neighbor)

    for k in range(len(nodes)):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def translate_to_pos(length: int, n: int) -> tuple:
    """Returns the tuple (x, y) appropriate to the input n."""
    y = n // length
    x = n % length
    return (x, y)

def translate_to_int(length: int, pos: tuple) -> int:
    """Returns the int belonging to the given position."""
    x, y = pos
    return (y * length) + x

def collect_nodes(lines: list):
    """Returns a dictionary of nodes with their position 'x:y' being the key."""
    nodes = dict()
    convert_start_end = lambda c: "a" if c == "S" else "z"
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            name = char
            if char in ("S", "E"):
                char = convert_start_end(char)
            if f"{x}:{y}" in nodes.keys():
                node = nodes[f"{x}:{y}"]
            else:
                node = Node(name, (x, y), ord(char) - ord("a"))
                nodes[f"{x}:{y}"] = node
    
            if 0 <= x - 1:
                if f"{x - 1}:{y}" in nodes.keys():
                    temp = nodes[f"{x - 1}:{y}"]
                else:
                    temp_char = line[x - 1] if line[x - 1] not in ("S", "E") else convert_start_end(line[x - 1])
                    temp = Node(temp_char, (x - 1, y), ord(temp_char) - ord("a"))
                    nodes[f"{x - 1}:{y}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)
            if x + 1 < len(lines[y]):
                if f"{x + 1}:{y}" in nodes.keys():
                    temp = nodes[f"{x + 1}:{y}"]
                else:
                    temp_char = line[x + 1] if line[x + 1] not in ("S", "E") else convert_start_end(line[x + 1])
                    temp = Node(temp_char, (x + 1, y), ord(temp_char) - ord("a"))
                    nodes[f"{x + 1}:{y}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)
            if 0 <= y - 1:
                if f"{x}:{y - 1}" in nodes.keys():
                    temp = nodes[f"{x}:{y - 1}"]
                else:
                    temp_char = lines[y - 1][x] if lines[y - 1][x] not in ("S", "E") else convert_start_end(lines[y - 1][x])
                    temp = Node(temp_char, (x, y - 1), ord(temp_char) - ord("a"))
                    nodes[f"{x}:{y - 1}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)
            if y + 1 < len(lines):
                if f"{x}:{y + 1}" in nodes.keys():
                    temp = nodes[f"{x}:{y + 1}"]
                else:
                    temp_char = lines[y + 1][x] if lines[y + 1][x] not in ("S", "E") else convert_start_end(lines[y + 1][x])
                    temp = Node(temp_char, (x, y + 1), ord(temp_char) - ord("a"))
                    nodes[f"{x}:{y + 1}"] = temp
                if temp.height <= node.height + 1:
                    node.neighbors.append(temp)

    return nodes

def weight(node1, node2) -> int:
    """Returns the weight of the (directional) edge from node1 to node2."""
    if node2 in node1.neighbors:
        return 1
        #return node1.height + 2 - node2.height
    else:
        return float("inf")

def weight_(node1, node2) -> int:
    """Returns the weight of the (directional) edge from node1 to node2; 0 if both are a."""
    if node2 in node1.neighbors:
        if node1.height == 0 and node2.height == 0:
            return 0
        return 1
    return float("inf")

def find_fields(inp: str, func):
    """Returns the positions (x, y) of all characters that satisfy func."""
    for y, line in enumerate(inp.split("\n")):
        for x, char in enumerate(line):
            if func(char):
                yield (x, y)

def print_distance_from_start(inp: str):
    temp = ""
    dist = shortest_paths_floyd_warshall(inp)
    for y, line in enumerate(inp.split("\n")):
        for x, char in enumerate(line):
            temp += str(dist[translate_to_int(8, (0, 0))][translate_to_int(8, (x, y))])[-1]
        temp += "\n"

    print(temp)
            
def print_costs(inp: str, nodes: dict):
    temp = ""
    for y, line in enumerate(inp.split("\n")):
        for x in range(len(line)):
            temp += str(nodes[f"{x}:{y}"].cost)[-1]
        temp += "\n"
    print(temp)


if __name__ == "__main__":
    testinput = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    with open("12/input.txt") as file:
        fileinput = file.read()
        cleaned_input = fileinput.replace("S", "a").replace("E", "z")
        length = len(fileinput.split("\n")[0])
        start = next(find_fields(fileinput, lambda c: c == "S"))
        #start = translate_to_int(length, next(find_fields(fileinput, lambda c: c == "S")))
        goal = next(find_fields(fileinput, lambda c: c == "E"))
        #goal = translate_to_int(length, next(find_fields(fileinput, lambda c: c == "E")))
        print("Puzzle 01:", shortest_path_dijkstra(fileinput, start, goal, False))
        print("Puzzle 02:", shortest_path_dijkstra(fileinput, start, goal, True))
        #dist = shortest_paths_floyd_warshall(cleaned_input)
        #print("Puzzle 01:", dist[start][goal])
        #print("Puzzle 02:", min(map(lambda st: dist[translate_to_int(length, st)][goal], find_fields(fileinput, lambda c: c in ("a", "S")))))
