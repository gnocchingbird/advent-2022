def find_calories_per_elf(inp:str) -> list:
    """Returns a list of the calories each elf is holding."""
    calories = [[int(item) for item in elf.split("\n")] for elf in inp.split("\n\n")]
    return list(map(sum, calories))

def find_top_elf(calories: list) -> int:
    """Returns the total number of calories held by the elf with the most calories."""
    return max(calories)

def find_top_three_elves(calories: list) -> int:
    """Returns the sum of the total calories held by the top three elves."""
    return sum(sorted(calories)[-3:])

if __name__ == "__main__":
    with open("01/input.txt") as file:
        calories = find_calories_per_elf(file.read())
        print(f"Calories held by top elf: {find_top_elf(calories)}")
        print(f"Calories held by top three elves: {find_top_three_elves(calories)}")