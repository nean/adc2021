import typing
import os

InputDataType = typing.List[typing.List[int]]


class OctoMap:
    def __init__(self, data: InputDataType) -> None:
        self.points = data
        self.step_count = 0
        self.xlen = len(data[0])
        self.ylen = len(data)
        self.flash_count = 0

    def step(self):
        old_flash_count = self.flash_count
        self.step_count += 1
        flash_points = []

        # increase all by 1
        for y in range(self.ylen):
            for x in range(self.xlen):
                self.points[y][x] += 1

                if self.points[y][x] > 9:
                    flash_points.append((x, y))

        # flash till nothing to flash
        while len(flash_points) > 0:
            # print('re-flash', self.step_count)
            flash_points = self.reflash(flash_points)

        # return flashed in this turn
        return self.flash_count - old_flash_count

    def reflash(self, points: typing.List[typing.Tuple[int, int]]):
        re_flash_points = []

        for x, y in points:
            to_be_flashed_ = self.flash(x, y)
            for i in to_be_flashed_:
                re_flash_points.append(i)

        return re_flash_points

    def flash(self, x, y):
        if self.points[y][x] == 0:
            return []

        # print('flashed ', x, y, self.points[y][x])

        self.points[y][x] = 0

        self.flash_count += 1

        adjecent_points = [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]

        to_be_flashed = []

        for x, y in adjecent_points:
            if (
                (x >= 0 and x < self.xlen)
                and (y >= 0 and y < self.ylen)
                and self.points[y][x] != 0
            ):
                self.points[y][x] += 1
                if self.points[y][x] > 9:
                    to_be_flashed.append((x, y))

        return to_be_flashed

    def __repr__(self) -> str:
        ret = ""
        for y in self.points:
            ret = f'{ret}{"".join([str(i) for i in y])}\n'

        return ret


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
        cleaned_data.append([int(i) for i in list(line.removesuffix("\n"))])
    return cleaned_data


def part1(data: InputDataType):
    om = OctoMap(data)

    while om.step_count < 100:
        dif = om.step()
        # print(om, dif)

    return om.flash_count


def part2(data: InputDataType):
    om = OctoMap(data)

    dif = 0

    while dif != (om.xlen * om.ylen):
        dif = om.step()
        # print(om, dif)

    return om.step_count, om.flash_count


print(part1(clean_data(load_data("test.txt"))))
print(part2(clean_data(load_data("test.txt"))))

print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
