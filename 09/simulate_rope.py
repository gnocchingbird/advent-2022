
def parse_input(inp: str) -> list:
    """Returns a list of the positions the tail has passed."""
    head_pos = (0, 0)
    tail_pos = (0, 0)
    visited = {tail_pos}

    for line in inp.split("\n"):
        direction, distance = line.split(" ")
        if direction == "R":
            for _ in range(int(distance)):
                head_pos = (head_pos[0] + 1, head_pos[1])
                tail_pos = gen_pos(head_pos, tail_pos)
                visited.add(tail_pos)
        elif direction == "L":
            for _ in range(int(distance)):
                head_pos = (head_pos[0] - 1, head_pos[1])
                tail_pos = gen_pos(head_pos, tail_pos)
                visited.add(tail_pos)
        elif direction == "U":
            for _ in range(int(distance)):
                head_pos = (head_pos[0], head_pos[1] - 1)
                tail_pos = gen_pos(head_pos, tail_pos)
                visited.add(tail_pos)
        elif direction == "D":
            for _ in range(int(distance)):
                head_pos = (head_pos[0], head_pos[1] + 1)
                tail_pos = gen_pos(head_pos, tail_pos)
                visited.add(tail_pos)
    return len(visited)
        

def gen_pos(head: tuple, tail: tuple) -> tuple:
    """Returns the new appropriate position of the tail."""
    if is_adjacent(head, tail):
        return tail

    head_x, head_y = head
    tail_x, tail_y = tail

    if head_x > tail_x:
        tail_x += 1
    elif head_x < tail_x:
        tail_x -= 1
    if head_y > tail_y:
        tail_y += 1
    elif head_y < tail_y:
        tail_y -= 1
    return (tail_x, tail_y)

def is_adjacent(tup1: tuple, tup2: tuple) -> bool:
    """Returns true if inputs are adjacent."""
    x1, y1 = tup1
    return any([(x1 + x_, y1 + y_) == tup2 for x_, y_ in [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]])



if __name__ == "__main__":
    testinput = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    with open("09/input.txt") as file:
        print("Puzzle 01:", parse_input(file.read()))
