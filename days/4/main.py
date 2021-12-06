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
    bingo_numbers = []
    bingo_boards = []

    input_stream = get_input(INPUT_FILE)
    bingo_numbers = list(map(lambda x: int(x), next(input_stream).split(",")))
    # Fake the next call to get to the numbers
    next(input_stream)

    boards = {}
    current_board = 0
    for board_row in input_stream:
        if not board_row.strip():
            current_board += 1
            continue
        numbers = list(map(lambda x: int(x), board_row.replace("  ", " ").split(" ")))
        if current_board not in boards:
            boards[current_board] = []
        boards[current_board].append(numbers)

    winning_boards = {}
    for bingo_pull in bingo_numbers:
        print(bingo_pull)
        for board_id, board in boards.items():
            for row_id, row in enumerate(board):
                boards[board_id][row_id] = list(map(lambda x: -1 if x == bingo_pull else x, row))
            for row_id, row in enumerate(board):
                if boards[board_id][row_id] == [-1] * 5 \
                        or [-1]*5 in [[item[i] for item in boards[board_id]] for i in range(0, 5)]:
                    if board_id not in winning_boards:
                        print("Bingo", board_id)
                        print(sum([0 if item == -1 else item for row in boards[board_id] for item in row]) * bingo_pull)
                    winning_boards[board_id] = True
                    # print("#########################", board_id)
                    # if board_id not in winning_boards and len(winning_boards.keys()) == len(boards) - 1:
                    # print(sum([0 if item == -1 else item for row in boards[board_id] for item in row]))
                        # print(sum([0 if item == -1 else item for row in boards[list(boards.keys())[0]] for item in
                        #            row]) * bingo_pull)
                        # exit()
                    # else:
                    #     winning_boards[board_id] = True
                    # Found horizontal match
                    # Board matches

