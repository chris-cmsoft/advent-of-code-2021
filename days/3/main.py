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
    aggregate = [int(char) for char in next(get_input(INPUT_FILE))]

    o2_gen = None
    matches = list(get_input(INPUT_FILE))
    for i in range(len(aggregate)):
        most_common = int(sum([int(x[i]) for x in matches]) >= (len(matches) / 2))
        matches = list(filter(lambda x: x[i] == str(most_common), matches))
        if len(matches) == 1:
            o2_gen = matches[0]
            break

    co2_gen = None
    matches = list(get_input(INPUT_FILE))
    for i in range(len(aggregate)):
        most_common = int(sum([int(x[i]) for x in matches]) < (len(matches) / 2))
        matches = list(filter(lambda x: x[i] == str(most_common), matches))
        if len(matches) == 1:
            co2_gen = matches[0]
            break

    print(int(o2_gen, 2) * int(co2_gen, 2))
