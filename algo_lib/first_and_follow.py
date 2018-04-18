import string

from functools import reduce


def start():
  prod, fir, fol = main()
  print("Productions: \n{}\nFirst: \n{}\nFollow: \n{}".format(print_prod(prod), print_dict(fir), print_dict(fol)))

def print_prod(prod):
  ans = []
  for nont in prod:
    ans += ["{} -> {}".format(nont, "|".join(prod[nont]))]
  return "\n".join(ans)

def print_dict(d):
  return "\n".join(["{} -> {}".format(x, d[x]) for x in d])

def main(prod=[("S", "TE"), ("E", "+TE"), ("E", "%"), ("T", "FR"), ("R", "*FR"), ("R", "%"), ("F", "(S)"), ("F", "a")]):
  prod_d = {}
  for nont, sent in prod:
    prod_d[nont] = prod_d.get(nont, []) + [sent]
  
  return prod_d, first(prod_d), follow(prod_d)

def first(prod):
  ans = {}
  for nonT in prod:
    ans[nonT] = list(set(first_nont(prod, nonT)))
  return ans

def first_nont(prod, nont):
  if nont == '' or nont == "%":  # if it is empty string or "epsilon"
    return ["%"]

  if nont in list(string.ascii_lowercase) + list("+()*"): # if it is a terminal
    return [nont]

  if nont.__len__() > 1:  # it is a sentence then
    first_of_first_sym = first_nont(prod, nont[0])
    if "%" in first_of_first_sym:
      return first_of_first_sym + first_nont(prod, nont[1:])
    else:
      return first_of_first_sym

  return reduce(lambda acc, first: acc + first, map(lambda sent: first_nont(prod, sent), prod[nont]), [])  # if it is a non Terminal

def follow(prod):
  ans = {}
  for nonT in prod:
    ans[nonT] = list(set(follow_nont(nonT, prod)).difference(set(["%"])))
  return ans

def follow_nont(nont, prod):
  ans = []
  if nont == "S":
    ans += ["$"]
  for every_nont in prod:
    for every_sent in prod[every_nont]:
      if nont in every_sent:
        ind = every_sent.index(nont)
        # print(nont, every_sent, ind)
        to_add = first_nont(prod, every_sent[ind+1:])
        ans += to_add.copy()
        if "%" in ans and every_nont != nont:
          ans.remove("%")
          ans += follow_nont(every_nont, prod)

  return ans

if __name__ == '__main__':
  start()
