
def get_instruction_by_tick(inp: str):
    """Returns a generator yielding the executed command at the respective tick (shift ticks by 1 pls)."""
    for line in inp.split("\n"):
        if line.split(" ")[0] == "addx":
            yield "noop"
        yield line

def get_signal_strenghths(inp: str) -> int:
    """Returns the sum of products val(x) * cycle for each cycle with (cycle - 20) % 40 == 0."""
    x = 1
    signal_sum = 0

    for cycle, inst in enumerate(get_instruction_by_tick(inp), 1):
        if (cycle - 20) % 40 == 0:
            signal_sum += (x * cycle)
        inst = inst.split(" ")
        if inst[0] == "addx":
            x = x + int(inst[1])

    return signal_sum

def parse_crt_signal(inp: str):
    """Returns a list of the rendered lines (strings)."""
    x = 1
    rendered = []

    for cycle, inst in enumerate(get_instruction_by_tick(inp), 1):
        if cycle % 40 == 1:
            rendered.append([])
        rendered[-1].append("#" if is_visible(cycle, x) else '.')
        inst = inst.split(" ")
        if inst[0] == "addx":
            x = x + int(inst[1])
    return rendered

def is_visible(cycle: int, xpos: int) -> bool: # somewhat redundant
    """Returns True if the sprite is visible."""
    beam_pos = (cycle - 1) % 40 # adjust for beam position being [0, 39]
    return xpos - 1 == beam_pos or xpos == beam_pos or xpos + 1 == beam_pos

def render_crt_signal(parsed: list) -> str:
    """Makes the parsed signal readable."""
    return "\n".join(map(lambda l: "".join(l), parsed))


if __name__ == "__main__":
    testinput = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    with open("10/input.txt") as file:
        fileinput = file.read()
        print("Puzzle 01:", get_signal_strenghths(fileinput))
        print("Puzzle 02:", "\n" + render_crt_signal(parse_crt_signal(fileinput)))
