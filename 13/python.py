import typing
import os

TCoord = typing.Tuple[int, int]
TCoords = typing.List[TCoord]
TFolds = typing.List[typing.Tuple[str, int]]
InputDataType = typing.Tuple[TCoords, TFolds]


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]) -> InputDataType:
    coords: typing.List[typing.Tuple[int, int]] = []
    folds: typing.List[typing.Tuple[str, int]] = []

    for line in lines:
        if line == "\n":
            continue

        if line.startswith("fold along "):
            i = line.removeprefix("fold along ").split("=")
            folds.append((i[0], int(i[1])))
            continue

        i = line.split(",")
        coords.append((int(i[0]), int(i[1])))

    return coords, folds


def foldx(input_coords: TCoords, fold_by: int) -> TCoords:
    out_coords: TCoords = []
    for x, y in input_coords:
        if x < fold_by:
            out_coords.append((x, y))
            continue

        if x > fold_by:
            out_coords.append((2 * fold_by - x, y))
            continue

    return list(set(out_coords))


def foldy(input_coords: TCoords, fold_by: int) -> TCoords:
    out_coords: TCoords = []
    for x, y in input_coords:
        if y < fold_by:
            out_coords.append((x, y))
            continue

        if y > fold_by:
            out_coords.append((x, 2 * fold_by - y))
            continue

    return list(set(out_coords))


def print_code(input_coords: TCoords):
    max_x = max([x for x, y in input_coords]) + 1
    max_y = max([y for x, y in input_coords]) + 1

    print("size", max_x, max_y)

    out = [[" " for _ in range(max_x)] for _ in range(max_y)]

    for x, y in input_coords:
        out[y][x] = "█"

    out_str = "\n"
    for y in out:
        for x in y:
            out_str += x
        out_str += "\n"

    return out_str


def part1(data: InputDataType):
    coords, folds = data

    axis, fold_by = folds[0]
    if axis == "x":
        coords = foldx(coords, fold_by)

    if axis == "y":
        coords = foldy(coords, fold_by)

    print("folded", axis, fold_by, len(coords))

    return len(coords)


def part2(data: InputDataType):
    coords, folds = data

    for axis, fold_by in folds:
        if axis == "x":
            coords = foldx(coords, fold_by)
        if axis == "y":
            coords = foldy(coords, fold_by)
        print("folded", axis, fold_by, len(coords))

    return print_code(coords)


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
