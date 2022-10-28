"""Environment setup."""
import sys

# Prevents PyCharm from automatically adding these to sys.path.
for path in sys.path:
    if "fiximport" in path and "tests" in path:
        sys.path.remove(path)


"""Application code"""
from sample.a.hello_world_utils import print_hello_world

print_hello_world()
