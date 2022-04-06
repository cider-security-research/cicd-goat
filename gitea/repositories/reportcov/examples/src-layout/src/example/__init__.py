import platform

# test merging multiple tox runs with a platform
# based branch
if platform.python_implementation() == "PyPy":
    def add(a, b):
        return a + b

else:
    def add(a, b):
        return a + b
