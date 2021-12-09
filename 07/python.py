import typing
import os

def load_data(file = 'input.txt') -> typing.List[str]:
  dirname = os.path.dirname(__file__)
  input_file = os.path.join(dirname, file)
  fd = open(input_file)
  lines = fd.readlines()
  fd.close()

  return lines

def clean_data(lines: typing.List[str]):
  data = [int(i) for i in lines[0].split(',')]

  return data

def get_median(data: typing.List[int]):
  sorted_data = sorted(data)
  pos = len(sorted_data) / 2
  low = int(pos)
  high = round(pos + 0.00001)

  return sorted_data[low]

def distance_from_2(data, pos):
  steps = []

  for d in data:
    steps.append(abs(d - pos))

  return sum([( n * (n+1) / 2) for n in steps])

def distance_from_1(data, pos):
  steps = []

  for d in data:
    steps.append(abs(d - pos))

  return sum(steps)

def part1(data: typing.List[int]):
  median = get_median(data)

  return distance_from_1(data, median)

def part2(data: typing.List[int]):
  mean = round(sum(data)/len(data))

  print(distance_from_2(data, mean - 2))
  print(distance_from_2(data, mean - 1))

  return distance_from_2(data, mean)


print(part1(clean_data(load_data('sample.txt'))))
print(part2(clean_data(load_data('sample.txt'))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
