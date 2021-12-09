import typing
import os
import enum

#   s1
# s2  s3
#   s4
# s5  s6
#   s7

class Segments(enum.Enum):
  SEGMENT_1 = 's1'
  SEGMENT_2 = 's2'
  SEGMENT_3 = 's3'
  SEGMENT_4 = 's4'
  SEGMENT_5 = 's5'
  SEGMENT_6 = 's6'
  SEGMENT_7 = 's7'

class Signals(enum.Enum):
  A = 'a'
  B = 'b'
  C = 'c'
  D = 'd'
  E = 'e'
  F = 'f'
  G = 'g'

def load_data(file = 'input.txt') -> typing.List[str]:
  dirname = os.path.dirname(__file__)
  input_file = os.path.join(dirname, file)
  fd = open(input_file)
  lines = fd.readlines()
  fd.close()

  return lines

def clean_data(lines: typing.List[str]):
  cleaned_data = []
  for line in lines:
    signals, output = line.split('|')
    signals = signals.split()
    output = output.split()
    cleaned_data.append((signals, output))
  return cleaned_data


def get_numbers(signals: typing.List[str]):
  numbers = {}
  mapping = {}

  # 1, 4, 7, 8
  for s in signals:
    if len(s) == 2:
      numbers[1] = set(s)
    elif len(s) == 3:
      numbers[7] = set(s)
    elif len(s) == 4:
      numbers[4] = set(s)
    elif len(s) == 7:
      numbers[8] = set(s)

  segment1 = numbers[7] - numbers[1]
  mapping[Segments.SEGMENT_1] = segment1.pop()

  # 6, 9, 0
  for s in signals:
    if len(s) != 6:
      continue

    test_6 = set(numbers[1])
    test_6.update(list(s))
    if test_6 != set(s):
      numbers[6] = set(s)
      continue

    test_9 = set(numbers[4])
    test_9.update(list(s))
    if test_9 == set(s):
      numbers[9] = set(s)
      continue

    # only zero
    numbers[0] = set(s)

  # 2, 3, 5
  for s in signals:
    if len(s) != 5:
      continue

    test_3 = set(numbers[7])
    test_3.update(list(s))
    if test_3 == set(s):
      numbers[3] = set(s)
      continue

    # 2, 5
    test_2_5 = set(numbers[1])
    test_2_5.update(list(s))
    if test_2_5 == numbers[9]:
      numbers[5] = set(s)
      continue

    numbers[2] = set(s)

  return dict(sorted(numbers.items()))

def part1(data: typing.List[typing.Tuple[typing.List[str], typing.List[str]]]):
  count = 0

  for display in data:
    signals, output = display

    for d in output:
      if len(d) in [2, 3, 4, 7]:
        count += 1

  return count

def part2(data: typing.List[typing.Tuple[typing.List[str], typing.List[str]]]):
  numbers = []
  for display in data:
    signals, output = display

    mapping = get_numbers(signals)

    number = ''
    for o in output:
      for k, v in mapping.items():
        if set(o) == v:
          number = f'{number}{k}'
    
    numbers.append(int(number))

  return sum(numbers)

print(part1(clean_data(load_data('sample.txt'))))
print(part2(clean_data(load_data('sample.txt'))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
