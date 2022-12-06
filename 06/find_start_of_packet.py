
def find_position(inp: str, n: int) -> int:
    """Returns the number of characters read until n consecutive characters differ"""
    most_recent = list(inp[:n])
    for i in range(n, len(inp)):
        if len(set(most_recent)) == n:
            return i
        most_recent[i % n] = inp[i]

if __name__ == "__main__":
    teststring = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    with open("06/input.txt") as file:
        fileinput = file.read()
        print("Puzzle 01:", find_position(fileinput, 4))
