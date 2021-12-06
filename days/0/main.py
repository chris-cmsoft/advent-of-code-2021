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
    for row in get_input(INPUT_FILE):
        print(row)
