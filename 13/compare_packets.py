
class Node:
    def __init__(self, parent):
        self.list = []
        self.parent = parent

    def __repr__(self):
        return "[" + ", ".join(map(lambda n: n.__repr__(), self.list)) + "]"

    def append(self, element):
        self.list.append(element)

    def collapse(self):
        return list(map(lambda n: n.collapse() if type(n) != int else n, self.list))

def parse_packets(inp: str) -> list:
    """Returns a list of tuples of lists, representing the packets."""
    temp = []

    for pair in inp.split("\n\n"):
        print(pair.split("\n"))
        left, right = pair.split("\n")
        temp.append((parse_list(left), parse_list(right)))
    return temp

def parse_list(inp: str) -> list:
    """Parses a single packet and returns the list representing that packet."""
    temp = inp[1:]
    root = Node(None)
    node = Node(root)
    root.append(node)
    read = ""
    close = False
    
    while temp != "" and node != root:
        c = temp[0]
        #print(c, root)
        if c == "[":
            if read != "":
                node.append(int(read))
            read = ""
            child = Node(node)
            node.append(child)
            node = child
        elif c == "]":
            if read != "":
                node.append(int(read))
            read = ""
            node = node.parent
        elif c == ",":
            if read != "":
                node.append(int(read))
            read = ""
        else:
            read += c
        temp = temp[1:]

    return root.list[0].collapse()

root = Node(None)
root.list = [1, 2, 3]
child = Node(root)
root.append(child)
child.append(4)
#print(root)



testinput = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

print(parse_packets(testinput))
