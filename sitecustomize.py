"""Install Pyblish into the current environment

Usage:
    Insert the parent directory of this file to your PYTHONPATH
    and make sure it's inserted FIRST. Python only automatically
    runs a single sitecustomize so this module manually imports
    any previously existing (if any).

Note:
    Use of `self` is due to the last portion of the file, where
    apparently Python clears locals() and globals() during import
    of another sitecustomize, making cwd unavailble afterwards.

"""

import os
import sys

self = sys.modules[__name__]
self.cwd = os.path.dirname(__file__)

# Install default packages
moduledir = os.path.join(self.cwd, "lib", "pyblish-x", "modules")
for module in os.listdir(moduledir):
    abspath = os.path.join(moduledir, module)
    sys.path.insert(0, abspath)

# Install dependencies
sys.path.insert(0, os.path.join(self.cwd, "lib", "python-qt5"))
os.environ["PATH"] = "blabla"

# Run existing sitecustomize, if any
sys.path.remove(self.cwd)
del sys.modules["sitecustomize"]

try:
    __import__("sitecustomize")

except ImportError:
    pass

finally:
    import sys
    sys.path.insert(0, self.cwd)
