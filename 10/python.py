import typing
import os

InputDataType = typing.List[str]

TAGS = {'(':')', '[':']' , '{':'}', '<':'>'}

POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}

ADDS = {')': 1, ']': 2, '}': 3, '>': 4}

def load_data(file = 'input.txt') -> typing.List[str]:
  dirname = os.path.dirname(__file__)
  input_file = os.path.join(dirname, file)
  fd = open(input_file)
  lines = fd.readlines()
  fd.close()

  return lines

def clean_data(lines: typing.List[str]) -> InputDataType:
  cleaned_data = []
  for line in lines:
    cleaned_data.append(line.removesuffix('\n'))
  return cleaned_data


def part1(data: InputDataType):
  errors = []
  for line in data:
    stack = []
    skip = False
    for i in list(line):
      if skip:
        continue

      if i in TAGS.keys():
        stack.append(i)

      if i in TAGS.values():
        expected_open_tag = stack[-1]
        if i == TAGS[expected_open_tag]:
          stack.pop()
        else:
          skip = True
          errors.append(i)

  print(errors)

  return sum([POINTS[i] for i in errors])


def part2(data: InputDataType):
  valid_lines = []

  errors = []
  for line in data:
    stack = []
    skip = False
    for i in list(line):
      if skip:
        continue

      if i in TAGS.keys():
        stack.append(i)

      if i in TAGS.values():
        expected_open_tag = stack[-1]
        if i == TAGS[expected_open_tag]:
          stack.pop()
        else:
          skip = True
          errors.append(i)

    if not skip:
      valid_lines.append(stack)

  scores = []
  for stack in valid_lines:
    score = 0
    while len(stack) > 0:
      score = score * 5 + ADDS[TAGS[stack.pop()]]

    scores.append(score)

  scores = sorted(scores)
  return scores[int(len(scores)/2)]

print(part1(clean_data(load_data('sample.txt'))))
print(part2(clean_data(load_data('sample.txt'))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
