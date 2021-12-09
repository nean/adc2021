import typing
import os

class BingBoard:
  SIZE = 5
  def __init__(self, numbers: typing.List[str]) -> None:
    self.board = [[0]*self.SIZE for i in range(self.SIZE)]
    self.strikes = [[False]*self.SIZE for i in range(self.SIZE)]
    self.bingo_won = False

    for k, v in enumerate(numbers):
      self.board[int(k/self.SIZE)][k%self.SIZE] = int(v)

  def __repr__(self) -> str:
    text = '\n-------\n'
    for x in range(self.SIZE):
      for y in range(self.SIZE):
        if self.strikes[x][y]:
          text = f'{text}\033[91m{self.board[x][y] : <4}\033[0m'
        else:
          text = f'{text}{self.board[x][y] : <4}'
      text = f'{text}\n'

    return text

  def strike(self, number: int):
    for x in range(self.SIZE):
      for y in range(self.SIZE):
        if self.board[x][y] == number:
          self.strikes[x][y] = True

  def bingo(self) -> bool:
    if self.bingo_won:
      return self.bingo_won

    # horizontal
    for x in self.strikes:
      if x[0] and len(set(x)) == 1:
        self.bingo_won = True
        return True

    # vertical
    for i in range(self.SIZE):
      win_column = True
      for x in self.strikes:
        win_column = win_column and x[i]
      
      if win_column:
        self.bingo_won = True
        return True

    return False

  def unstriked(self) -> typing.List[int]:
    unmarked = []
    for x in range(self.SIZE):
      for y in range(self.SIZE):
        if not self.strikes[x][y]:
          unmarked.append(self.board[x][y])
    
    return unmarked


def load_data(file = 'input.txt') -> typing.List[str]:
  dirname = os.path.dirname(__file__)
  input_file = os.path.join(dirname, file)
  fd = open(input_file)
  lines = fd.readlines()
  fd.close()

  return lines

def clean_data(lines: typing.List[str]):
  draws = [int(i) for i in lines[0].split(',')]

  boards = []
  board_lines = lines[1:]

  buffer = []

  for line in board_lines:
    buffer = buffer + line.split()

    if len(buffer) == 25:
      boards.append(BingBoard(buffer))
      buffer = []

  return draws, boards


def part1(data: typing.Tuple[typing.List[int], typing.List[BingBoard]]):
  draws, boards = data

  bingo_draw = None
  bingo_board = None

  for d in draws:
    #print(d)
    for b in boards:
      b.strike(d)
    
    for b in boards:
      #print(b)
      if b.bingo():
        bingo_draw = d
        bingo_board = b
        break
    if bingo_draw is not None:
      break
  
  assert bingo_board is not None
  assert bingo_draw is not None

  unmarked = bingo_board.unstriked()
  return sum(unmarked) * bingo_draw

def part2(data: typing.Tuple[typing.List[int], typing.List[BingBoard]]):
  draws, boards = data

  board_count = len(boards)
  bingod_board_count = 0

  last_bingo_board = None
  last_bingo_draw = None

  for d in draws:
    for b in boards:
      b.strike(d)
    
    for b in boards:
      if b.bingo_won:
        continue

      if b.bingo():
        last_bingo_board = b
        last_bingo_draw = d
        bingod_board_count = bingod_board_count + 1

    if board_count - bingod_board_count == 0:
      break
  
  unmarked = last_bingo_board.unstriked()
  return sum(unmarked) * last_bingo_draw

print(part1(clean_data(load_data('sample.txt'))))
print(part2(clean_data(load_data('sample.txt'))))

print(part1(clean_data(load_data())))
print(part2(clean_data(load_data())))
