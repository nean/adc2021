import typing
import os

class Tank:
  def __init__(self, data: typing.List[int]) -> None:
    fishes = {i: 0 for i in range(9)}

    for f in data:
      if f not in fishes.keys():
        fishes[f] = 1
      else:
        fishes[f] += 1

    self.fishes = fishes

  def __repr__(self) -> str:
      return repr((repr(self.fish_count), repr(self.fishes)))

  @property
  def fish_count(self):
    count = 0
    for _, v in self.fishes.items():
      count += v

    return count

  def next_day(self):
    prev_fishes = self.fishes.copy()
    next_fishes = {i: 0 for i in range(9)}
    for k, v in prev_fishes.items():
      if k == 0:
        next_fishes[8] += v
        next_fishes[6] += v
      else:
        next_fishes[k - 1] += v

    self.fishes = next_fishes

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

def part1(data: typing.List[int]):
  tank = Tank(data)

  for i in range(80):
    print('day ', i + 1)
    tank.next_day()
    print(tank)

  return tank

def part2(data: typing.List[int]):
  tank = Tank(data)

  for i in range(256):
    tank.next_day()
    print('day ', i + 1, tank)

  return tank

print(part1(clean_data(load_data('sample.txt'))))
print(part2(clean_data(load_data('sample.txt'))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
