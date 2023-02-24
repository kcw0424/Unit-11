from contextlib import contextmanager

@contextmanager
def open3(path):
    print("opining file...")
    file = open(path)
    try:
        print("yielding file...")
        yield file
    finally:
        print("closing file...")
        file.close()

with open3("text.txt") as file:
    s = file.read()
    print(s)
