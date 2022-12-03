
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

def get_priority(inp: str) -> int:
    if inp in alphabet:
        return ord(inp) - 96
    if inp in alphabet.upper():
        return ord(inp) - 38
    error("oops")



if __name__ == "__main__":
    testinput = """vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw"""

    with open("03/input.txt") as file:
        print(sum(map(get_priority, get_doubled_items(file.read()))))
