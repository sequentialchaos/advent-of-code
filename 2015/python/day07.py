import re
import math
from operator import lshift, rshift, sub, and_, or_

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(instructions):
  wires = connect_wires(instructions)
  return wires['a']

def part_2(instructions):
  wires = connect_wires(instructions)
  tmp = wires['a']
  wires = {'b':tmp}
  wires = connect_wires(instructions, wires)
  return(wires['a'])

#####################################################################

def read_input():
  parse_signals = lambda line: [int(n) for n in re.findall('(\d+)', line)]
  parse_operator = lambda line: re.findall('([A-Z]+)', line)
  parse_wires = lambda line: re.findall('([a-z]+)', line)
  parse = lambda line: parse_operator(line) + parse_wires(line) + parse_signals(line)
  with open('../inputs/07.txt') as f:
    return [parse(line) for line in f.readlines()]

def perform(instruction, wires):
  if len(instruction) == 2:
    if isinstance(instruction[1], int):
      wire, signal = instruction
      wires[wire] = signal
    else: 
      wire_1, wire_2 = instruction
      wires[wire_2] = wires[wire_1]
  elif len(instruction) == 3:
    operator, wire_1, wire_2 = instruction
    wires[wire_2] = not_(wires[wire_1])
  elif len(instruction) == 4:
    if 'LSHIFT' in instruction or 'RSHIFT' in instruction:
      operator, wire_1, wire_2, amount = instruction
      if operator == 'LSHIFT':
        wires[wire_2] = lshift(wires[wire_1], amount)
      elif operator == 'RSHIFT':
        wires[wire_2] = rshift(wires[wire_1], amount)
    elif 'OR' or 'AND' in instruction:
      if any(isinstance(w, int) for w in instruction):
        operator, wire_1, wire_2, signal = instruction
        if operator == 'OR':
          value = or_(wires[wire_1], signal)
          wires[wire_2] = value
        elif operator == 'AND':
          value = and_(wires[wire_1], signal)
          wires[wire_2] = value
      else:
        operator, wire_1, wire_2, wire_3 = instruction
        if operator == 'OR':
          wires[wire_3] = or_(wires[wire_1], wires[wire_2])
        elif operator == 'AND':
          wires[wire_3] = and_(wires[wire_1], wires[wire_2])
  return wires

def not_(n):
  if n == 0: return 65535
  pow_2 = int(math.log2(n)) + 1
  return sub(2**pow_2 - 1, n)

def get_wires(instruction):
  raw_instruction = ' '.join([str(x) for x in instruction])
  instruction_wires = re.findall('([a-z]+)', raw_instruction)
  return instruction_wires

def has_inputs(instruction, wires):
  raw_instruction = ' '.join([str(x) for x in instruction])
  input_wires = re.findall('([a-z]+)', raw_instruction)[:-1]
  return all(wire in wires for wire in input_wires)

def connect_wires(instructions, wires={}):
  deque = instructions*1
  while len(deque) > 0:
    instruction = deque.pop()
    if instruction[0] == 'b' and instruction[0] in wires:
      continue
    elif has_inputs(instruction, wires):
      wires = perform(instruction, wires)
    else:
      deque.insert(0, instruction)
  return wires
#####################################################################

if __name__ == "__main__":
  main()
