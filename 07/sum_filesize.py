
class Node:
    def __init__(self, name: str, parent, nodetype: bool, size: int = 0):
        self.name = name
        self.size = size
        self.type = nodetype # 0 means directory, 1 means file
        self.parent = parent
        self.children = []
        self.visited = False

    def calculate_sizes(self) -> int:
        if self.size != 0:
            return self.size
        size = 0
        for child in self.children:
            size += child.calculate_sizes()
        
        self.size = size
        return self.size

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_child(self, name: str):
        for child in self.children:
            if child.name == name:
                return child

    def __repr__(self):
        return self.name + "\n" + "\n".join(map(lambda s: "  " + "\n".join(map(lambda t: "  " + t, s.__repr__().split("\n"))), self.children))

def parse_input(inp: str):
    """Constructs the file tree according to the input"""
    root = Node("/", False, False)
    current = root
    read = []
    for line in inp.split("\n"):
        temp = line.split(" ")
        if temp[0] == "$":
            if temp[1] == "ls":
                read = []
            if temp[1] == "cd":
                if temp[2] == "/":
                    current = root
                elif temp[2] == "..":
                    current = current.parent
                else:
                    current = current.get_child(temp[2])
        else: # not a command -> file
            if temp[0] == "dir":
                current.add_child(Node(temp[1], current, False))
            else:
                current.add_child(Node(temp[1], current, True, int(temp[0])))
    return root

def sum_directory_sizes(root) -> int:
    """Returns the sum of sizes of directories that have a size less than 100000."""
    root.calculate_sizes()
    size = 0
    current = root
    to_eval = [root]
    
    while to_eval != []:
        current = to_eval.pop()
        to_eval.extend(current.children)
        if current.type == False:
            if current.size <= 100000:
                size += current.size
    return size

def find_smallest_dir_to_delete(root) -> int:
    """Returns the size of the smallest directory that frees enough space when deleted"""
    size_needed = root.calculate_sizes() - 40000000
    smallest_sufficient = root.size
    current = root
    to_eval = [root]

    while to_eval != []:
        current = to_eval.pop()
        to_eval.extend(current.children)
        if current.type == False:
            if current.size >= size_needed and current.size < smallest_sufficient:
                smallest_sufficient = current.size
    return smallest_sufficient


if __name__ == "__main__":
    testinput = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    with open("07/input.txt") as file:
        root = parse_input(file.read())
        print("Puzzle 01:", sum_directory_sizes(root))
        print("Puzzle 02:", find_smallest_dir_to_delete(root))








