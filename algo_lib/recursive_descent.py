def advance(word, string, ptr):
	if string[ptr] == word:
		return ptr + 1
	else:
		raise Exception('Cannot parse')

def E(string, ptr):
    """
    >>> string = 'i+i$'
    >>> ptr = 0
    >>> E()

    """
    ptr = T(string, ptr)
    ptr = E_(string, ptr)
    return ptr

def E_(string, ptr):
    if string[ptr] == '+':
        ptr = advance('+', string, ptr)
        ptr = T(string, ptr)
        ptr = E_(string, ptr)
    return ptr

def T(string, ptr):
    ptr = F(string, ptr)
    ptr = T_(string, ptr)
    return ptr

def T_(string, ptr):
    if string[ptr] == '*':
        ptr = advance('*')
        ptr = F(string, ptr)
        ptr = T_(string, ptr)
    return ptr

def F(string, ptr):
    if string[ptr] == 'i':
        ptr = advance('i', string, ptr)
    elif string[ptr] == '(':
        ptr = advance('(', string, ptr)
        ptr = E(string, ptr)
        ptr = advance(')', string, ptr)
    else:
        raise Exception('Cannot parse')
    return ptr

def main(string, ptr):
    try:
        ptr = E(string, ptr)
        if string[ptr] == '$':
            return True
        else:
            raise Exception('Cannot parse')
    except Exception as Err:
        return False


if __name__ == '__main__':
    print(main('i+i$', 0))
    print(main('i+$', 0))