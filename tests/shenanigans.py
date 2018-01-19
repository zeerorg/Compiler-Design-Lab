import contextlib

# Create a modified mock.patch so that everytime function is called a 
# new value is returned, convert a generator to mock.patch side_effect function

class GenFunc:

    def __init__(self, gen: 'generator'):
        self.gen = gen()
        self.gen

    def __call__(self):
        return next(self.gen)

@contextlib.contextmanager
def patch_with_generator(to_patch: str, gen: 'generator'):
    to_import = to_patch.split(".")
    lib = __import__('.'.join(to_import[:-1]), globals(), locals(), [to_import[-1]], 0)
    old_module_func = lib.__getattribute__(to_import[-1])
    setattr(lib, to_import[-1], GenFunc(gen))
    yield
    setattr(lib, to_import[-1], old_module_func)
    pass
