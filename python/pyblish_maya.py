import os
import sys


python_dir = os.path.dirname(__file__)
repository_dir = os.path.dirname(python_dir)

library_dir = os.path.join(
    repository_dir,
    "lib",
    "pyblish-suite",
    "pyblish-maya")

if not library_dir in sys.path:
    sys.path.insert(0, library_dir)

import pyblish_maya
sys.modules[__name__] = pyblish_maya
reload(pyblish_maya)