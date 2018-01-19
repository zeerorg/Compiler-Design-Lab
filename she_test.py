from tests import shenanigans

def new_gen():
    print("YOLO")
    yield "YOLO"
    print("2nd Time")
    yield "2nd Time"

with shenanigans.patch_with_generator('builtins.input', new_gen):
    input()
    input()

