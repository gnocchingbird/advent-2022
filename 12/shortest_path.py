
class Node:
    def __init__(self, name: str, pos: tuple[int, int], height: int):
        self.parent = None
        self.cost = float("inf")
        self.name = name
        self.pos = pos
        self.height = height

    def __repr__(self):
        return f"Node {self.name} at {self.pos}"

    def __eq__(self, other):
        return False if other == None else self.pos == other.pos

def shortest_path_dijkstra(inp: str) -> int:
    """Returns the length of the shortest path leading from S to E."""
    to_visit = []
    visited = []
    length = 0
    start = None

    for y, line in enumerate(inp.split("\n")):
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
                print(start)
                break

    current = Node("S", start, ord("a"))
    current.cost = 0

    to_visit.extend(find_neighbors(inp, current))
    while current.name != "E":
        print(current.pos)
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
        current = to_visit[0]
        to_visit = to_visit[1:]
        visited.append(current)

    while current.name != "S":
        length += 1
        current = current.parent

    return length
                
                

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



if __name__ == "__main__":
    testinput = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    with open("12/input.txt") as file:
        print("Puzzle 01:", shortest_path_dijkstra(file.read())) # 8s to solve puzzle 01, what??
