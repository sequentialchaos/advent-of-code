import re

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  _, ranges, tickets = s
  max_ticket_value = max(n for ticket in tickets for n in ticket)
  in_range = join_ranges(ranges, max_ticket_value)
  return sum(
    value 
    for ticket in tickets 
    for value in invalid_values(ticket, in_range)
  )

def part_2(s):
  fields, ranges, tickets = s
  max_ticket_value = max(n for ticket in tickets for n in ticket)
  in_range = join_ranges(ranges, max_ticket_value)
  not_found = [True] * len(ranges)
  positions = [-1 for _ in range(len(fields))]
  while any(not_found):
    d = {}
    for ticket_set in valid_tickets(tickets, in_range):
      for i,ticket in enumerate(ticket_set):
        d.setdefault(i, [])
        b = [
          in_either_range(ticket, t) 
          for t in ranges
        ]
        d[i].append(b)
    for i in range(len(ranges)):
      a = [value for value in not_found]
      for b in d[i]:
        a = intersection(a, b)
      if a.count(True) == 1:
        positions[i] = a.index(True)
        not_found = intersection(not_found, [not value for value in a])
  product = 1
  my_ticket = tickets[0]
  for i,position in enumerate(positions):
    if 'departure' in fields[position]:
      product *= my_ticket[i]
  return product

#####################################################################
def parse(lines):
  fields = re.findall('(.*):.*', lines)
  ranges = [
    [int(n) for n in t]
    for t in re.findall('.*: (\d+)-(\d+) or (\d+)-(\d+)', lines)
  ]
  tickets = [
    [int(n) for n in line.split(',')]
    for line in lines.split('\n')
    if line.count(',') > 0
  ]
  return fields, ranges, tickets

def read_input():
  with open('../inputs/16.txt') as f:
    return parse(f.read())

def in_either_range(value, ranges):
  a, b, c, d = ranges
  return a <= value <= b or c <= value <= d

def join_ranges(ranges, max_ticket_value):
  max_range_value = max(n for t in ranges for n in t)
  max_value = max(max_ticket_value, max_range_value)
  in_range = [0 for n in range(max_value+1)]
  for t in ranges:
    a, b = t[:2]
    c, d = t[2:]
    for value in range(a,b+1):
      in_range[value] = 1
    for value in range(c,d+1):
      in_range[value] = 1
  return in_range

def invalid_values(ticket, in_range):
  for n in ticket:
    if not in_range[n]:
      yield n

def is_valid(ticket, in_range):
  for n in ticket:
    if not in_range[n]:
      return False
  return True

def valid_tickets(tickets, in_range):
  return (ticket for ticket in tickets if is_valid(ticket, in_range))

def intersection(a, b):
  return [a[i] and b[i] for i in range(len(a))]

#####################################################################
if __name__ == "__main__":
  main()
