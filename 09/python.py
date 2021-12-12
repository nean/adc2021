import typing
import os

InputDataType = typing.List[typing.List[int]]


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]) -> InputDataType:
    cleaned_data = []
    for line in lines:
        row = [int(i) for i in list(line.removesuffix("\n"))]
        cleaned_data.append(row)
    return cleaned_data


def check_low(rk, ck, v, data: InputDataType):
    top = (rk - 1, ck) if rk - 1 >= 0 else None
    down = (rk + 1, ck) if rk + 1 < len(data) else None
    left = (rk, ck - 1) if ck - 1 >= 0 else None
    right = (rk, ck + 1) if ck + 1 < len(data[0]) else None

    low = True

    if top is not None:
        low = low and data[top[0]][top[1]] > v

    if down is not None:
        low = low and data[down[0]][down[1]] > v

    if left is not None:
        low = low and data[left[0]][left[1]] > v

    if right is not None:
        low = low and data[right[0]][right[1]] > v

    return low


def get_surrounding(rk, ck, data):
    top = (rk - 1, ck) if rk - 1 >= 0 else None
    down = (rk + 1, ck) if rk + 1 < len(data) else None
    left = (rk, ck - 1) if ck - 1 >= 0 else None
    right = (rk, ck + 1) if ck + 1 < len(data[0]) else None

    returned = []

    if top is not None:
        if data[top[0]][top[1]] < 9:
            returned.append(top)

    if down is not None:
        if data[down[0]][down[1]] < 9:
            returned.append(down)

    if left is not None:
        if data[left[0]][left[1]] < 9:
            returned.append(left)

    if right is not None:
        if data[right[0]][right[1]] < 9:
            returned.append(right)

    return returned


def find_basin(rk, ck, data: InputDataType, basin_points=[], checked={}):
    old_size = len(basin_points)
    for p in basin_points:
        if p in checked.keys():
            continue

        new_points = get_surrounding(p[0], p[1], data)

        for q in new_points:
            if q not in basin_points:
                basin_points.append(q)

        checked[p] = True

    if len(basin_points) == old_size:
        return basin_points

    return find_basin(rk, ck, data, basin_points, checked)


def part1(data: InputDataType):
    risk = []

    for rk, r in enumerate(data):
        for ck, c in enumerate(r):
            if check_low(rk, ck, c, data):
                risk.append(c + 1)

    return sum(risk)


def part2(data: InputDataType):
    basins = []

    for rk, r in enumerate(data):
        for ck, c in enumerate(r):
            if check_low(rk, ck, c, data):
                basins.append(len(find_basin(rk, ck, data, basin_points=[(rk, ck)])))

    top_three = sorted(basins)

    return top_three[-1] * top_three[-2] * top_three[-3]


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
