import os

INPUT_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")


def get_input(path):
    with open(path, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line.strip()


if __name__ == '__main__':
    days = 256
    lantern_fish = list(map(lambda x: int(x), next(get_input(INPUT_FILE)).split(",")))

    lantern_fish_ages = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in lantern_fish:
        lantern_fish_ages[fish] += 1
    for i in range(days):
        for age, count in lantern_fish_ages.copy().items():
            lantern_fish_ages[age - 1] = count
        lantern_fish_ages[8] = lantern_fish_ages[-1]
        lantern_fish_ages[6] = lantern_fish_ages[6] + lantern_fish_ages[-1]
        del lantern_fish_ages[-1]

    print(sum([count for count in lantern_fish_ages.values()]))
