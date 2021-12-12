import typing
import os


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]):
    clean_data = []
    for line in lines:
        clean_data.append(int(line))

    return clean_data


def increments(numbers: typing.List[int], interval: int):
    inc = 0

    for i in range(len(numbers) - interval):
        if numbers[i + interval] > numbers[i]:
            inc = inc + 1

    return inc


def part1(numbers: typing.List[int]):
    return increments(numbers, 1)


def part2(numbers: typing.List[int]):
    return increments(numbers, 3)


# sample
print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

# actual
print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
