
alphabet = "abcdefghijklmnopqrstuvwxyz"

def get_doubled_items(inp: str) -> list:
    doubled = []
    for line in inp.split("\n"):
        fst_half = line[:int(len(line) / 2)] # len(line) is guaranteed to be even
        snd_half = line[int(len(line) / 2):]
        for c in fst_half:
            if c in snd_half:
                doubled.append(c)
                break
    return doubled

def get_badges(inp: str) -> list:
    badges = []
    lines = inp.split("\n")
    for i in range(0, len(lines), 3): # len(lines) is guaranteed to be wholly divisible by 3
        found = False # pinnacle of inelegance
        for c1 in lines[i]:
            if found:
                break
            for c2 in lines[i + 1]:
                if found:
                    break
                if c1 == c2:
                    for c3 in lines[i + 2]:
                        if c1 == c3:
                            found = True
                            badges.append(c1)
                            break
    return badges

def get_priority(inp: str) -> int:
    if inp in alphabet:
        return ord(inp) - 96
    if inp in alphabet.upper():
        return ord(inp) - 38
    print("hwaet? {inp}")



if __name__ == "__main__":
    testinput = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    with open("03/input.txt") as file:
        print(sum(map(get_priority, get_badges(file.read()))))
