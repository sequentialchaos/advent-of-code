
def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return sum(is_passport_valid_1(passport) for passport in s)

def part_2(s):
  return sum(is_passport_valid_2(passport) for passport in s)

#####################################################################

def read_input():
  def parse_passport(s):
    return {
      field.split(':')[0]:field.split(':')[1]
      for field in s.split()
    }
  with open('../inputs/04.txt') as f:
    return [parse_passport(s) for s in f.read().split('\n\n')]

def is_passport_valid_1(passport):
  required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  return all(field in passport for field in required)

def is_passport_valid_2(passport):
  required = {
    'byr': lambda s: 1920 <= int(s) <= 2002, 
    'iyr': lambda s: 2010 <= int(s) <= 2020, 
    'eyr': lambda s: 2020 <= int(s) <= 2030, 
    'hgt': lambda s: s[-2:] in ['in', 'cm'] and 
                      (59 <= int(s[:-2]) <= 76 if s[-2:] == 'in' 
                      else 150 <= int(s[:-2]) <= 193),
    'hcl': lambda s: len(s) == 7 and s[0] == '#' and 
                      all(c in '0123456789abcdef' for c in s[1:7]), 
    'ecl': lambda s: s in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda s: len(s) == 9 and all(c in '0123456789' for c in s),
    'cid': lambda s: True
  }
  has_all_fields = all(field in passport for field in required if field != 'cid')
  each_field_valid = all(required[field](value) for field,value in passport.items())
  return has_all_fields and each_field_valid
  
#####################################################################

if __name__ == "__main__":
  main()
