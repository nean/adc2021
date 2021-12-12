from posixpath import islink
import typing
import os

COORDS = typing.Tuple[int, int]


class Board:
    def __init__(self, size: int) -> None:
        self.board = [[0] * size for i in range(size)]
        self.size = size

    def draw(self, start_coords: COORDS, end_coords: COORDS, diag: bool = False):
        x1 = start_coords[0]
        y1 = start_coords[1]

        x2 = end_coords[0]
        y2 = end_coords[1]

        if x1 == x2:
            print("  x line ", start_coords, end_coords)
            for i in range(min(y1, y2), max(y1, y2) + 1):
                self.board[i][x1] += 1
            return

        if y1 == y2:
            print("  y line ", start_coords, end_coords)
            for i in range(min(x1, x2), max(x1, x2) + 1):
                self.board[y2][i] += 1
            return

        if not diag:
            return

        slope = (y2 - y1) / (x2 - x1)

        if slope == 1:
            print("+ve slope", start_coords, end_coords)
            minx = min(x1, x2)
            maxx = max(x1, x2)
            maxy = max(y1, y2)
            miny = min(y1, y2)

            i = minx
            j = miny
            while True:
                # print(i, j)
                self.board[j][i] += 1
                i += 1
                j += 1

                if i > maxx:
                    break

            return

        if slope == -1:
            print("-ve slope", start_coords, end_coords)
            minx = min(x1, x2)
            maxx = max(x1, x2)
            maxy = max(y1, y2)

            i = minx
            j = maxy
            while True:
                # print(i, j)
                self.board[j][i] += 1
                i += 1
                j -= 1

                if i > maxx:
                    break
            return

        print("nope", slope, start_coords, end_coords)

    def points(self):
        count = 0

        for i in self.board:
            for j in i:
                if j > 1:
                    count += 1

        return count

    def __repr__(self) -> str:
        text = "\n"
        for x in range(self.size):
            for y in range(self.size):
                text = f"{text}{self.board[x][y] : <1}"
            text = f"{text}\n"

        return text


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]):
    clean_data = []

    board_size = 0

    for line in lines:
        coords = line.split(" -> ")
        start_coords = [int(c) for c in coords[0].split(",")]
        end_coords = [int(c) for c in coords[1].split(",")]

        board_size = max(start_coords + end_coords + [board_size])
        clean_data.append(
            ((start_coords[0], start_coords[1]), (end_coords[0], end_coords[1]))
        )

    return board_size, clean_data


def part1(data: typing.Tuple[int, typing.List[typing.Tuple[COORDS, COORDS]]]):
    size, lines = data
    board = Board(size + 1)

    for l in lines:
        s, e = l
        board.draw(s, e)

    # print(board)

    return board.points()


def part2(data: typing.Tuple[int, typing.List[typing.Tuple[COORDS, COORDS]]]):
    size, lines = data
    board = Board(size + 1)

    for l in lines:
        s, e = l
        board.draw(s, e, True)

    # print(board)

    return board.points()


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
