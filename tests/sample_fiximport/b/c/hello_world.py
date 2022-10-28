"""Environment setup."""
import sys
from os.path import join, dirname, abspath

# Prevents PyCharm from automatically adding these to sys.path.
for path in sys.path:
    if "fiximport" in path and "tests" in path:
        sys.path.remove(path)

# Add `fiximport` to sys.path.
# If `fiximport` is installed with pip, this is not required.
sys.path.insert(0, abspath(join(dirname(__file__), "../../../../src/fiximport")))

"""Application code."""
import fiximport
from sample_fiximport.a.hello_world_utils import print_hello_world

print_hello_world()
