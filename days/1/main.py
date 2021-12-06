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
    increased_depth_count = 0
    previous = []
    for depth in get_input(INPUT_FILE):
        previous.append(int(depth))
        if len(previous) < 4:
            continue
        previous_window = previous[:3]
        new_window = previous[1:]
        if sum(new_window) > sum(previous_window):
            increased_depth_count += 1
        previous = new_window
    print(increased_depth_count)
