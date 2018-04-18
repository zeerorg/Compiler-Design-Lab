from functools import reduce

import first_and_follow as fnf

def start():
  prod, table = main()
  print("Productions: \n{}\n\nTable: \n{}".format(fnf.print_prod(prod), print_table(table)))

def print_table(table):
  non_terms = list(table.keys())
  terms = []
  #for _, sents in prod.items():
  #  terms += ''.join(sents)

  terms = ''.join([ table[x][y][1] for x in table for y in table[x] if table[x].get(y) != None])
  terms = list(filter(lambda x: x not in non_terms and x != "$" and x != "%", set(terms)))
  
  # terms = list(filter(lambda x: x not in non_terms and x != "%", terms)) + ["$"]

  ans = []
  for x in non_terms:
    row_st = '{}: \t'.format(x)
    ans += [ row_st + '\t\t'.join([ '{}|{}'.format(y, get_pp(table[x][y]) if table[x].get(y) != None else '\t') for y in terms ]) ]

  return '\n'.join(ans)

def get_pp(tup):
  return "{} -> {}".format(tup[0], tup[1])

def main(prod=[("S", "TE"), ("E", "+TE"), ("E", "%"), ("T", "FR"), ("R", "*FR"), ("R", "%"), ("F", "(S)"), ("F", "a")]):
  prod_d = {}
  for nonT, sent in prod:
    prod_d[nonT] = prod_d.get(nonT, []) + [sent]
  
  non_terms = list(prod_d.keys())
  terms = filter(lambda x: x not in non_terms and x != "%", ''.join([x[1] for x in prod]))
  terms = list(set(terms))

  table = { nT: { term: None for term in terms + ["$"] } for nT in non_terms }
  
  for nont, sent in prod:
    sent_fir = fnf.first_nont(prod_d, sent)
    sent_terms = set(sent_fir).intersection(set(terms))
    table[nont].update({ st: (nont, sent) for st in sent_terms })

    if "%" in sent_fir:
      nont_fol = fnf.follow_nont(nont, prod_d)
      nont_fol_terms = set(nont_fol).intersection(set(terms))
      table[nont].update({ ft: (nont, sent) for ft in nont_fol_terms })
      if "$" in nont_fol:
        table[nont]["$"] = (nont, sent)

  return prod_d, table
  

if __name__ == '__main__':
  start()
