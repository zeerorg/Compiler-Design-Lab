from algo_lib import recursive_descent

def main():
  strings = ['i+i$', 'i+$', 'i*i$', 'i+i+(i*i+i)$']
  for string in strings:
    if recursive_descent.main(string, 0):
      print("{} : is parsed".format(string))
    else:
      print("{} : has error parsing".format(string))

if __name__ == '__main__':
  main()
