from functools import reduce

import construct_ll1 as ll

def start():
  table, string, prod = main()
  print("Table: \n{}\n\nString: {}\n\nProductions: \n{}".format(ll.print_table(table), 
                                                                string, 
                                                                '\n'.join([ '{} -> {}'.format(p[0], p[1]) for p in prod ]))
  )

example_table = {
  "S": { "(": ("S", "TE"), "a": ("S", "TE") },
  "E": { "+": ("E", "+TE"), ")": ("E", "%"), "$": ("E", "%") },
  "T": { "(": ("T", "FR"), "a": ("T", "FR") },
  "R": { "+": ("R", "%"), "*": ("R", "*FR"), ")": ("R", "%"), "$": ("R", "%") },
  "F": { "(": ("F", "(S)"), "a": ("F", "a") }
}

def main(table=example_table, string="a+a*a"):
  stack = ["$", "S"]
  my_str = string + "$"
  ip = 0
  ans = []

  non_terms = list(table.keys())
  terms = ''.join([ table[x][y][1] for x in table for y in table[x] ])
  terms = list(filter(lambda x: x not in non_terms and x != "$", set(terms))) 

  while stack[-1] != "$":
    X = stack[-1]
    a = my_str[ip]
    if X in terms or X == '$':
      if X == a:
        stack.pop()
        ip += 1
      else:
        print(stack, X, a, ans)
        raise Exception
    elif table[X].get(a) != None:
      stack.pop()
      stack += list(table[X][a][1])[::-1]
      if stack[-1] == "%":
        stack.pop()
      ans.append(table[X][a])
    else:
      print(stack)
      raise Exception

  return table, string, ans

if __name__ == '__main__':
  start()


