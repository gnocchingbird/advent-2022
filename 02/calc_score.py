
values = {
    "A": 1,
    "X": 0,
    "B": 2,
    "Y": 1,
    "C": 3,
    "Z": 2}

letters = {value: key for key, value in values.items()}

def calculate_score1(inp: str) -> int:
    score = 0
    for line in inp.split("\n"):
        p1, p2 = line.split(" ")
        p1val = values[p1]
        p2val = values[p2] + 1

        score += p2val
    
        if p1val == p2val:
            score = score + 3
            continue
        if (1 + (p1val + 1) % 3) == p2val:
            continue
        if (1 + (p2val + 1) % 3) == p1val:
            score = score + 6
    return score

def calculate_score2(inp: str) -> int:
    score = 0
    for line in inp.split("\n"):
        p1, result = line.split(" ")
        p1val = values[p1]
        score = score + (3 * values[result])
        print(3 * values[result])
        
        if result == "X":
            if p1val == 1:
                score = score + 3
                print(f"p1 won with {p1val} against {3}!")
            else:
                score = score + (p1val - 1)
                print(f"p1 won with {p1val} against {p1val - 1}!")
            #score = score + (1 + p1val % 3)
        if result == "Y":
            score = score + p1val
            print(f"it's a draw with {p1val} on both sides!")
        if result == "Z":
            score = score + ((p1val + 1) % 3)
            print(f"p2 won with {(p1val + 1) % 3} against {p1val}!")
            #if p1val == 1:
            #    score = score + 3
            #    print(f"p2 won with {3} against {p1val}!")
            #else:
            #    score = score + (p1val - 1)
            #    print(f"p2 won with {p1val - 1} against {p1val}!")
    return score
        

if __name__ == "__main__":
    testinput = """A Y
B X
C Z"""
    with open("02/input.txt") as file:
        print(calculate_score2(file.read()))
