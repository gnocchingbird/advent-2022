
def get_section_ids(inp: str) -> list:
    """Returns a list of 2-element-lists each containing the assignments for the first and the second elf"""
    range_ = lambda start, end: range(start, end + 1)
    return [[set(range_(*map(int, item.split("-")))) for item in line.split(",")] for line in inp.split("\n")]

def count_containments(pairs: list) -> int:
    """Counts the amount of pairs where one half wholly contains the other"""
    return sum((s1.issubset(s2) or s2.issubset(s1) for s1, s2 in pairs))

def count_intersections(pairs: list) -> int:
    """Counts the amount of pairs where the halves intersect at all"""
    return sum((s1.intersection(s2) != set() for s1, s2 in pairs))



if __name__ == "__main__":
    testinput = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    
    with open("04/input.txt") as file:
        pairs = get_section_ids(file.read())
        print("Puzzle 01:", count_containments(pairs))
        print("Puzzle 02:", count_intersections(pairs))
