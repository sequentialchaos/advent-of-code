import re

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return sum(
    evaluate_full_expression(line, evaluate_simple_expression_1) 
    for line in s
  )

def part_2(s):
  return sum(
    evaluate_full_expression(line, evaluate_simple_expression_2) 
    for line in s
  )

#####################################################################
def read_input():
  parse = lambda line: re.findall(r'([\(\)\+\*]|\d+)', line)
  with open('../inputs/18.txt') as f:
    return [parse(line) for line in f.readlines()]

def evaluate_full_expression(tokens, simple_expression_function):
  while len(tokens) > 1:
    next_tokens = []
    i = 0
    p = [t for t in find_inner_parentheses(tokens)]
    if len(p) > 0:
      for t in p:
        a, b = t
        for token in tokens[i:a]:
          next_tokens.append(token)
        next_tokens.append(str(simple_expression_function(tokens[a+1:b])))
        i = b+1
      for token in tokens[i:]:
        next_tokens.append(token)
      tokens = next_tokens
    else:
      tokens = [simple_expression_function(tokens)]
  return tokens[0]

def evaluate_simple_expression_1(tokens):
  result = int(tokens[0])
  for i in range(1, len(tokens), 2):
    operation = tokens[i]
    value = int(tokens[i+1])
    if operation == '+':
      result += value
    elif operation == '*':
      result *= value
  return result

def evaluate_simple_expression_2(tokens):
  while '+' in tokens:
    i = 1
    next_tokens = []
    while i < len(tokens) - 1:
      if tokens[i] == '+':
        value = int(tokens[i-1]) + int(tokens[i+1])
        next_tokens.append(str(value))
        for j in range(i+2, len(tokens)):
          next_tokens.append(tokens[j])
        break
      else:
        next_tokens.append(tokens[i-1])
        next_tokens.append(tokens[i])
      i += 2
    tokens = next_tokens
  return evaluate_simple_expression_1(tokens)

def find_inner_parentheses(tokens):
  prev = False
  for j,token in enumerate(tokens):
    if token == '(':
      i = j
      prev = True
    elif token == ')':
      if prev: 
        yield(i, j)
        prev = False

#####################################################################

if __name__ == "__main__":
  main()
