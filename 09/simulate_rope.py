
def simulate_rope(inp: str) -> list:
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

def simulate_longer_rope(inp: str) -> list:
    """Returns a list of the positions the last knot has passed."""
    knot_pos = [(0, 0) for _ in range(10)]
    visited = {knot_pos[9]}

    for line in inp.split("\n"):
        direction, distance = line.split(" ")
        if direction == "R":
            for _ in range(int(distance)):
                knot_pos[0] = (knot_pos[0][0] + 1, knot_pos[0][1])
                for i in range(1, len(knot_pos)):
                    head_pos, tail_pos = knot_pos[i - 1:i + 1]
                    tail_pos = gen_pos(head_pos, tail_pos)
                    knot_pos[i - 1] = head_pos
                    knot_pos[i] = tail_pos
                visited.add(knot_pos[-1])
        elif direction == "L":
            for _ in range(int(distance)):
                knot_pos[0] = (knot_pos[0][0] - 1, knot_pos[0][1])
                for i in range(1, len(knot_pos)):
                    head_pos, tail_pos = knot_pos[i - 1:i + 1]
                    tail_pos = gen_pos(head_pos, tail_pos)
                    knot_pos[i - 1] = head_pos
                    knot_pos[i] = tail_pos
                visited.add(knot_pos[-1])
        elif direction == "U":
            for _ in range(int(distance)):
                knot_pos[0] = (knot_pos[0][0], knot_pos[0][1] - 1)
                for i in range(1, len(knot_pos)):
                    head_pos, tail_pos = knot_pos[i - 1:i + 1]
                    tail_pos = gen_pos(head_pos, tail_pos)
                    knot_pos[i - 1] = head_pos
                    knot_pos[i] = tail_pos
                visited.add(knot_pos[-1])
        elif direction == "D":
            for _ in range(int(distance)):
                knot_pos[0] = (knot_pos[0][0], knot_pos[0][1] + 1)
                for i in range(1, len(knot_pos)):
                    head_pos, tail_pos = knot_pos[i - 1:i + 1]
                    tail_pos = gen_pos(head_pos, tail_pos)
                    knot_pos[i - 1] = head_pos
                    knot_pos[i] = tail_pos
                visited.add(knot_pos[-1])
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
    testinput1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    testinput2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    with open("09/input.txt") as file:
        moves = file.read()
        print("Puzzle 01:", simulate_rope(moves))
        print("Puzzle 02:", simulate_longer_rope(moves))
