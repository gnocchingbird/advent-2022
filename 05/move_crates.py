
def parse_input(inp: str) -> tuple:
    """Returns a tuple (stacks, instructions)."""
    crates = []
    n_stacks = 0
    inp, instructions = inp.split("\n\n")
    instructions = [instruction.replace("move ", "").replace(" from ", ":").replace(" to ", ":") for instruction in instructions.split("\n")] # parse natural language instructions to represent "amount:start:goal"
    instructions = (map(int, instruction.split(":")) for instruction in instructions)

    for line in inp.split("\n"):
        if "[" in line:
            crates.append(line)
        else:
            i = 1
            while str(i) in line:
                n_stacks += 1
                i += 1
    
    stacks = [[] for _ in range(n_stacks)]

    for level in crates[::-1]:
        for i in range(n_stacks):
            content = level[4 * i + 1]
            if content != " ":
                stacks[i].append(content)

    return (stacks, list(instructions))

def apply_instructions_9000(stacks: list, instructions: list) -> list:
    """Returns a list of stacks after the instructions have been applied using the CrateMover 9000."""
    for amount, start, goal in instructions:
        while amount != 0:
            temp = stacks[start - 1].pop()
            stacks[goal - 1].append(temp)
            amount -= 1
    return stacks

def apply_instructions_9001(stacks: list, instructions) -> list:
    """Returns a list of stacks after the instructions have been applied using the CrateMover 9001."""
    for amount, start, goal in instructions:
        temp = stacks[start - 1][-amount:]
        stacks[start - 1] = stacks[start - 1][:-amount]
        stacks[goal - 1].extend(temp)
    return stacks


if __name__ == "__main__":
    testinput = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    with open("05/input.txt") as file:
        get_top_crates = lambda s: "".join(map(lambda s_: s_.pop(), s))
        fileinput = file.read()
        stacks, instructions = parse_input(fileinput)
        print("Puzzle 01:", get_top_crates(apply_instructions_9000(stacks, instructions)))
        stacks, instructions = parse_input(fileinput)
        print("Puzzle 02:", get_top_crates(apply_instructions_9001(stacks, instructions)))