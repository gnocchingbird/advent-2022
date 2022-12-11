
import operator

class Monkey:
    def __init__(self, items: list, operation, test, lcm):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0
        self.lcm = lcm # least common multiple

    def inspect(self) -> int:
        """Determines the worry level for the first item and returns the value (adjusted for relief)."""
        item = self.items[0]
        item = self.operation(item)
        item = item // 3
        self.inspections += 1
        self.items[0] = item
        return item

    def inspect_without_relief(self) -> int:
        """Determines the worry level for the first item and returns the value (not adjusted for relief)."""
        item = self.items[0]
        item = self.operation(item)
        item = item % self.lcm
        self.inspections += 1
        self.items[0] = item
        return item

    def throw(self) -> int:
        """Returns a tuple (target monkey, item value) for the first item and removes it from the list."""
        item = self.items[0]
        self.items = self.items[1:]
        target = self.test(item)
        return (target, item)

def parse_monkey(monke: str):
    """Returns a Monkey object according to the given input."""
    items = []
    operation = None
    test = None

    monke = monke.split("\n")
    
    items = list(map(lambda i: int(i.strip(",")), monke[1].strip().split(" ")[2:]))

    op = monke[2].strip().split(" ")[3:]
    operator = op[1]
    op = op[::2]
    def operate(x: int):
        values = [x if e == "old" else int(e) for e in op]
        if operator == "*":
            return values[0] * values[1]
        else:
            return values[0] + values[1]
    operation = operate

    mod_val = int(monke[3].strip().split(" ")[-1])
    targets = (int(monke[4].strip().split(" ")[-1]), int(monke[5].strip().split(" ")[-1])) # targets[0] if true
    test = lambda x: targets[0] if x % mod_val == 0 else targets[1]
    return Monkey(items, operation, test, mod_val)

def simulate_monkeys(monkeys: list, rounds: int, relief: bool = True) -> int:
    """Returns the level of monkey business after rounds."""
    done = 0
    for r in range(1, rounds + 1):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                if relief:
                    monkey.inspect()
                else:
                    monkey.inspect_without_relief()
                target, item = monkey.throw()
                monkeys[target].items.append(item)
    most_active = sorted(map(lambda m: m.inspections, monkeys))[-2:]
    return operator.mul(*most_active)

def get_monkeys(inp: str) -> list:
    """Returns a list of monkeys from the input."""
    monkeys = []
    for monke in inp.split("\n\n"):
        monkeys.append(parse_monkey(monke))
    return monkeys

def adjust_for_lcm(monkeys: list) -> list:
    """Returns a list of monkeys with the lcm set to the least common multiple of the monkeys' divisors."""
    temp = 1
    for i in map(lambda m: m.lcm, monkeys):
        temp = temp * i
    for monkey in monkeys:
        monkey.lcm = temp
    return monkeys
            
if __name__ == "__main__":
    testinput = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    with open("11/input.txt") as file:
        fileinput = file.read()
        print("Puzzle 01:", simulate_monkeys(get_monkeys(fileinput), 20))
        print("Puzzle 02:", simulate_monkeys(adjust_for_lcm(get_monkeys(fileinput)), 10000, False))
