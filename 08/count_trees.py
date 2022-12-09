
def count_trees(inp: str) -> int:
    trees = 0
    lines = inp.split("\n")
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if all(map(lambda c: c < char, line[:x])):
                trees += 1
            elif all(map(lambda c: c < char, line[x + 1:])):
                trees += 1
            elif all(map(lambda c: c < char, [l[x] for l in lines[:y]])):
                trees += 1
            elif all(map(lambda c: c < char, [l[x] for l in lines[y + 1:]])): # possible out of bounds?
                trees += 1
    return trees

def best_view(inp: str) -> int:
    lines = inp.split("\n")
    best_score = 0
    best_tree = (0, 0)
    for y, line in enumerate(lines[1:-1], 1):
        for x, char in enumerate(line[1:-1], 1):
            score = 1
            temp = 0
            x_ = x - 1
            while x_ != -1 and line[x_] < char:
                temp += 1
                x_ -= 1
            temp += 1 if x_ != -1 else 0
            score = score * temp
            temp = 0
            x_ = x + 1
            while x_ != len(line) and line[x_] < char:
                temp += 1
                x_ += 1
            temp += 1 if x_ != len(line) else 0
            score = score * temp
            temp = 0
            y_ = y - 1
            while y_ != -1 and lines[y_][x] < char:
                temp += 1
                y_ -= 1
            temp += 1 if y_ != -1 else 0
            score = score * temp
            temp = 0
            y_ = y + 1
            while y_ != len(lines) and lines[y_][x] < char:
                temp += 1
                y_ += 1
            temp += 1 if y_ != len(lines) else 0
            score = score * temp
            best_score = max(score, best_score)
    return best_score


if __name__ == "__main__":
    testinput = """30373
25512
65332
33549
35390"""
    with open("08/input.txt") as file:
        fileinput = file.read()
        print("Puzzle 01:", count_trees(fileinput))
        print("Puzzle 02:", best_view(fileinput))
