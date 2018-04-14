"""

Left recursive to right recursive
1.  Input productions as a list, non T are Upper case letters while others are terminals
2.  loop over all productions and collect all productions of a non terminal, create a dictionary (maybe)
3.  for every production in the dict:
    3.1 determine if there is left recursion
    3.2 if there is LR, create two lists, one with all LR grammer and one without
    3.3 Create a new production
    3.4 In list with LR grammar cut the first character
    3.5 add new production to the end of all non recursive productions, put this list as the non T's productions
    3.6 In the new production add "epsilon", take list from step 3.5 and add new Production at the end
    3.7 the productions in 3.5 and 3.6 are productions of the new non T

"""

from functools import reduce

def start():
  main()
  pass

def main(prod=[("E", "E+T"), ("E", "T"), ("T", "a")]):
  prod_d = {}
  print(prod)
  for pro in prod:
    if prod_d.get(pro[0]) is None:
      prod_d[pro[0]] = []
    prod_d[pro[0]].append(pro[1])

  new_prod = {}
  for NonT in prod_d:
    is_prod = reduce(lambda acc, new: new[0] == NonT or acc, prod_d[NonT], False)
    if is_prod:
      LR = list(filter(lambda new: new[0] == NonT, prod_d[NonT]))
      nonLR = list(filter(lambda new: new[0] != NonT, prod_d[NonT]))
      newP = "{}_".format(NonT)
      new_prod[newP] = ["$"]
      LR = list(map(lambda new: "{}{}".format(new[1:], newP), LR))
      print(LR)
      nonLR = list(map(lambda new: "{}{}".format(new, newP), nonLR))
      prod_d[NonT] = nonLR
      new_prod[newP].extend(LR)

  prod_d.update(new_prod)

  print("Productions are")
  for p in prod_d.items():
    print("{} -> {}".format(p[0], p[1]))

  pass

start()
