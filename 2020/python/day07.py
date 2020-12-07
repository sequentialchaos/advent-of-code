import re

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  count = 0
  bags = lines_to_bags(s)
  for bag_color in bags:
    if contains_shiny_gold(bag_color, bags):
      count += 1    
  return count

def part_2(s):
  bags = lines_to_bags_2(s)
  return count_bags_inside('shiny gold', bags)

#####################################################################

def read_input():
  with open('../inputs/07.txt') as f:
    return [line for line in f.read().split('\n')]

def lines_to_bags(lines):
  all_bags = {}
  for line in lines:
    bags = re.findall('(\w+ \w+) bag', line)
    bag = bags[0]
    bags_inside = bags[1:]
    if bags_inside[0] == 'no other':
      bags_inside = []
    all_bags[bag] = bags_inside
  return all_bags

def lines_to_bags_2(lines):
  bags = {}
  for line in lines:
    bag = re.findall('(\w+ \w+) bag', line)[0]
    inner_bags = re.findall('(\d) (\w+ \w+) bag', line)
    bags[bag] = [(b[1], int(b[0])) for b in inner_bags]
  return bags

def contains_shiny_gold(start, bags):
  stack = [start]
  while stack:
    bag = stack.pop()
    for inner_bag in bags[bag]:
      if inner_bag == 'shiny gold':
        return True
      stack.append(inner_bag)
  return False

def count_bags_inside(start, bags):
  total_bags = 0
  for bag_color, bag_amount in bags[start]:
    total_bags += bag_amount
    total_bags += bag_amount * count_bags_inside(bag_color, bags)
  return total_bags

#####################################################################

if __name__ == "__main__":
  main()
