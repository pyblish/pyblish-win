import os
import sys


python_dir = os.path.dirname(__file__)
repository_dir = os.path.dirname(python_dir)

library_dir = os.path.join(
    repository_dir,
    "lib",
    "pyblish-suite",
    "pyblish-nuke")

if not library_dir in sys.path:
    sys.path.insert(0, library_dir)

import pyblish_nuke
sys.modules[__name__] = pyblish_nuke
reload(pyblish_nuke)