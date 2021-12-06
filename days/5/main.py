import collections
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
    coordinate = collections.namedtuple("coordinate", "x y")
    line_map = {}
    for row in get_input(INPUT_FILE):
        coord1, coord2 = [list(map(lambda x: int(x), coordinate.split(","))) for coordinate in row.split(" -> ")]
        print('#')
        print(coord1)
        print(coord2)
        coords = [
            coordinate(coord1[0], coord1[1]),
            coordinate(coord2[0], coord2[1])
        ]

        if coords[0].x == coords[1].x:
            x = coords[0].x
            for y in range(coords[0].y, coords[1].y + 1) if coords[0].y < coords[1].y else range(coords[1].y, coords[0].y + 1):
                key = "{}:{}".format(x, y)
                if key not in line_map:
                    line_map[key] = 0
                line_map[key] += 1
            continue


        if coords[0].y == coords[1].y:
            y = coords[0].y
            for x in range(coords[0].x, coords[1].x + 1) if coords[0].x < coords[1].x else range(coords[1].x, coords[0].x + 1):
                key = "{}:{}".format(x, y)
                if key not in line_map:
                    line_map[key] = 0
                line_map[key] += 1
            continue

        if coords[1].x > coords[0].x:
            coords = [
                coords[1],
                coords[0]
            ]
        x = coords[1].x
        print(x)
        y_range = reversed(range(coords[0].y, coords[1].y + 1)) if coords[0].y < coords[1].y else range(coords[1].y, coords[0].y + 1)
        for y in y_range:
            key = "{}:{}".format(x, y)
            if key not in line_map:
                line_map[key] = 0
            line_map[key] += 1
            x += 1

        # for x in range(coord1[0], coord2[0]):
        #     print(x)
    print(line_map)
    counter = 0
    for coordinate_count in line_map.values():
        if coordinate_count >= 2:
            counter += 1

    print(counter)
    # A = y2-y1
    # B = x1-x2
    # C = Ax1+By1
    #
    # Regardless of how the lines are specified, you should be able to generate two different points along the line, and then generate A, B and C. Now,
    # lets say
    # that you have lines, given by the equations:
    #
    # A1x + B1y = C1
