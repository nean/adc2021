import typing
import os
import collections

TInsertions = typing.Dict[typing.Tuple[str, str], str]
InputDataType = typing.Tuple[str, TInsertions]

# setup lookup dict
data_lookup: typing.Dict[
    typing.Tuple[str, str, int], typing.Counter
] = collections.defaultdict(collections.Counter)
# data_hits = collections.Counter()


def load_data(file="input.txt") -> typing.List[str]:
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, file)
    fd = open(input_file)
    lines = fd.readlines()
    fd.close()

    return lines


def clean_data(lines: typing.List[str]) -> InputDataType:
    insertions: typing.Dict[typing.Tuple[str, str], str] = {}
    seed = lines[0].removesuffix("\n")

    for line in lines[1:]:
        if line == "\n":
            continue

        split = line.removesuffix("\n").split(" -> ")
        insertions[(split[0][0], split[0][1])] = split[1]

    return seed, insertions


def chain(
    start, end, insertions: TInsertions, end_round: int, current_round: int = 0
) -> typing.Counter:
    if current_round == end_round:
        return collections.Counter()

    # return if found in lookup table
    if data_lookup[(start, end, end_round - current_round)]:
        # for stats
        # data_hits[(start, end, end_round - current_round)] += 1
        # data_hits['all'] += 1
        return data_lookup[(start, end, end_round - current_round)]

    insertion = insertions[(start, end)]
    counter_left = chain(start, insertion, insertions, end_round, current_round + 1)
    counter_right = chain(insertion, end, insertions, end_round, current_round + 1)

    current_counter = counter_left + counter_right
    current_counter[insertion] += 1

    # store for lookup
    data_lookup[(start, end, end_round - current_round)] = current_counter

    return current_counter


# BRUTE FORCE !!!
def polymerize(seed: str, insertions: TInsertions):
    out_list = seed[0]

    for i in range(0, len(seed) - 1):
        inserted = insertions[(seed[i], seed[i + 1])]
        out_list += inserted + seed[i + 1]

    return out_list


def part1(data: InputDataType):
    seed, insertions = data

    for i in range(10):
        seed = polymerize(seed, insertions)

    counter = collections.Counter(seed)

    sorted_counts = counter.most_common()

    return sorted_counts[0][1] - sorted_counts[-1][1]


def part2(data: InputDataType):
    seed, insertions = data

    counter = collections.Counter(seed)

    for i in range(0, len(seed) - 1):
        p_counter = chain(seed[i], seed[i + 1], insertions, 40)
        counter.update(p_counter)

    # print('lookups', data_hits['all'])

    sorted_counts = counter.most_common()

    return sorted_counts[0][1] - sorted_counts[-1][1]


print(part1(clean_data(load_data("sample.txt"))))
print(part2(clean_data(load_data("sample.txt"))))

# reset the lookup dict
data_lookup: typing.Dict[
    typing.Tuple[str, str, int], typing.Counter
] = collections.defaultdict(collections.Counter)
# data_hits = collections.Counter()

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
