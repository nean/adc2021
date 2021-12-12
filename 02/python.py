import typing
import os
import enum


class Direction(enum.Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


class Instruction:
    def __init__(self, direction: Direction, units: int) -> None:
        self.direction = direction
        self.units = units

    def __repr__(self) -> str:
        return f"{self.direction.value} {self.units}"


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
        direction, units = line.split(" ")
        clean_data.append(Instruction(Direction(direction), int(units)))

    return clean_data


def part1(instructions: typing.List[Instruction]):
    vertical_pos = 0
    horizontal_pos = 0

    for i in instructions:
        if i.direction is Direction.FORWARD:
            horizontal_pos = horizontal_pos + i.units
            continue
        if i.direction is Direction.UP:
            vertical_pos = vertical_pos - i.units
            continue
        if i.direction is Direction.DOWN:
            vertical_pos = vertical_pos + i.units
            continue

    return horizontal_pos * vertical_pos


def part2(instructions: typing.List[Instruction]):
    vertical_pos = 0
    horizontal_pos = 0
    aim = 0

    for i in instructions:
        if i.direction is Direction.FORWARD:
            horizontal_pos = horizontal_pos + i.units
            vertical_pos = vertical_pos + aim * i.units
            continue

        if i.direction is Direction.UP:
            aim = aim - i.units
            continue

        if i.direction is Direction.DOWN:
            aim = aim + i.units
            continue

    return horizontal_pos * vertical_pos


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
