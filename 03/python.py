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
        clean_data.append(line.removesuffix("\n"))

    return clean_data


def get_rates(data: typing.List[str]):
    data_length = len(data)
    bits = [0 for k in range(len(data[0]))]

    for d in data:
        for k, v in enumerate(d):
            bits[k] = bits[k] + int(v)

    bit_rates = [b / data_length for b in bits]

    gamma_rates = [str(round(b + 0.000000001)) for b in bit_rates]
    epsilon_rates = [str(abs(int(b) - 1)) for b in gamma_rates]

    return gamma_rates, epsilon_rates


def filter_bits(
    data: typing.List[str],
    bits: typing.List[str],
    rate: str = "gamma",
    position: int = 0,
):
    filtered = []
    for d in data:
        if d[position] == bits[position]:
            filtered.append(d)

    if len(filtered) == 1:
        return filtered[0]

    g, e = get_rates(filtered)

    if rate == "gamma":
        bits = g
    else:
        bits = e

    return filter_bits(filtered, bits, rate, position + 1)


def part1(data: typing.List[str]):
    g_rates, e_rates = get_rates(data)

    g_rate = int("".join(g_rates), 2)
    e_rate = int("".join(e_rates), 2)

    print(g_rate, e_rate)

    return g_rate * e_rate


def part2(data: typing.List[str]):
    g_rates, e_rates = get_rates(data)

    o2_rating = filter_bits(data, g_rates)
    co2_rating = filter_bits(data, e_rates, "epsilon")

    o2_rating = int(o2_rating, 2)
    co2_rating = int(co2_rating, 2)

    return co2_rating * o2_rating


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
