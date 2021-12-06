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
    horizontal = 0
    depth = 0
    aim = 0
    for line in get_input(INPUT_FILE):
        command, amount = line.split(" ")
        amount = int(amount)
        if command == "forward":
            horizontal += amount
            depth = depth + (aim * amount)
        if command == "up":
            aim -= amount
        if command == "down":
            aim += amount
    print(depth * horizontal)
