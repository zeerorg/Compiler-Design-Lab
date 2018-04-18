"""
1.  Input productions as a list of tuples
2.  Create a dictionary from those from {nonT : [ "prod1", "prod2" ]}

Left_factor(dictionary)
3.  FOr every nonterminal in the dictionary do:
        matches = []
    3.1 FOr every production of the nonT do:
        3.1.1 Loop over all other productions and determine which have common prefix (by checking every other's first character)
        3.1.2 If found break
    3.2 if the above found array is not empty
        3.2.1 Find the common prefix from matches (using predefined function)
        3.2.2 Calculate new production equal to matches minus the prefix
        3.2.3 current production becomes everything except matches and a "perfix.new nonT"
        3.2.4 flag = True
        3.2.5 break
    3.3 if flag: return Left_factor(new_dictionary)
    3.4 return dictionary
        

Keep repeating till new dictionary is empty
"""

from functools import reduce

def start():
  print("Start: {}\nLeft Factored: {}".format(*main()))
  pass


def main(prod=[("A", "abc"), ("A", "abp"), ("A", "abq")]):
  
  prod_d = {}
  for x in prod:
    prod_d[x[0]] = [x[1]] + prod_d.get(x[0], [])

  return prod_d.copy(), left_factor(prod_d)

def left_factor(prod):
  new_d = {}
  flag = False
  for nont in prod:
    matches = []
    for sent in prod[nont]:
      matches = list(filter(lambda x: x[0] == sent[0], prod[nont]))
      if matches.__len__() > 1:
        break
    if matches.__len__() > 1:
      prefix = get_common_prefix(matches)
      new_d["{}_".format(nont)] = list(map(lambda x: x[len(prefix):], matches))
      new_d[nont] = list(filter(lambda x: x not in matches, prod[nont])) + ["{}{}_".format(prefix, nont)]
      flag = True
      break
  if flag:
    for x in new_d:
      prod[x] = new_d[x]
    return left_factor(prod)
  return prod

def common_perf(string1, string2):
  ans = []
  for x in zip(string1, string2):
    if x[0] == x[1]:
      ans.append(x[0])
    else:
      return ''.join(ans)
  return ''.join(ans)

def get_common_prefix(strings):
  return reduce(lambda prefix, x: common_perf(prefix, x), strings[1:], strings[0])

if __name__ == '__main__':
  start()
