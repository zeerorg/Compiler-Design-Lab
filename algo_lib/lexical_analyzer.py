# create a lexical analyzer
# how to do:
"""
  1. Write the worst code in your entire life. 
"""
import string
def main(program: str) -> list:
  get_literal = literal_closure()
  get_keyword = keyword_closure()
  get_operator = operator_closure()
  get_identifier = identifier_closure()
  ans = []
  
  for letter in program:
    literal = get_literal(letter)
    keyword = get_keyword(letter)
    operator = get_operator(letter)
    identifier = get_identifier(letter)
    if literal:
      ans.append((literal, 'literal'))
    elif keyword:
      ans.append((keyword, 'keyword'))
    elif operator:
      ans.append((operator, 'operator'))
    elif identifier:
      ans.append((identifier, 'identifier'))

  return ans

def operator_closure():
  word = []
  start = False
  def get_operator(letter):
    nonlocal word, start
    if start == False and letter in ' \n':
      start = True
    elif start and letter in '+-*/<>=!' and word.__len__() == 0:
      word.append(letter)
    elif start and letter in '=' and word.__len__() == 1:
      word.append(letter)
    elif start and letter in ' \n':
      start = True
      op = ''.join(word)
      word = []
      return op
    else:
      start = False
      word = []
    return False
  return get_operator

def identifier_closure():
  word = []
  in_string = False
  start = False
  def get_identifier(letter):
    nonlocal word, start, in_string
    if not start and not in_string and letter in ' \n':
      start = True
    elif start and not in_string and word.__len__() == 0 and letter in string.ascii_letters:
      word.append(letter)
    elif start and not in_string and letter in string.ascii_letters + string.digits and word.__len__() > 0:
      word.append(letter)
    elif start and not in_string and word.__len__() > 0 and letter in ' \n':
      start = True
      ans = ''.join(word)
      word = []
      return ans
    elif start and not in_string and letter not in string.ascii_letters + string.digits:
      word = []
      start = False
    elif not in_string and letter == "\"":
      start = False
      word = []
    return False
  return get_identifier

def keyword_closure():
  get_identifier = identifier_closure()
  def get_keyword(letter):
    nonlocal get_identifier
    keyword = get_identifier(letter)
    if keyword in ['if', 'then', 'endif']:
      return keyword
    return False
  return get_keyword

def literal_closure():
  start = False
  in_string = False
  num = False
  word = []
  def get_literal(letter):
    nonlocal start, in_string, num, word
    if start and not in_string and letter == "\"":
      in_string = True
      num = False
      word.append(letter)
    elif start and in_string and letter == "\"":
      in_string = False
      start = False
      word.append(letter)
      ans = ''.join(word)
      word = []
      return ans
    elif start and in_string:
      word.append(letter)
    elif not start and not num and not in_string and letter in " \n":
      start = True
      num = True
    elif start and num and letter in string.digits:
      word.append(letter)
    elif start and num and letter in " \n" and word.__len__() > 0:
      ans = ''.join(word)
      start = True
      word = []
      return ans
    elif start and num and letter not in string.digits:
      start = False
      num = False
      word = []
    return False

  return get_literal
  

if __name__ == '__main__':
  test_programs = [
    ' start = 2 + 4 ',
    ' "hello" ',
    ' x = 523\ny = 3 + x\nz = x * y '
  ]
  for program in test_programs:
    tokens = main(program)
    print(tokens)


