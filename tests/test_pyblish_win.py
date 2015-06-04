import os
import tempfile
import shutil

from nose.tools import (
    assert_equals
)

import pyblish_win.util
pyblish_win.util.augment_pythonpath()

original_path = os.environ["PATH"]
temp_dir = None


def setup():
    global temp_dir
    temp_dir = tempfile.mkdtemp()


def teardown():
    os.environ["PATH"] = original_path
    shutil.rmtree(temp_dir)


def test_where():
    """where() works fine"""

    # Create fixture with executables
    for fname in ("myfile.exe", "notexec.bin", "test.bat"):
        with open(os.path.join(temp_dir, fname), "w") as f:
            f.write("")

    os.environ["PATH"] = temp_dir + ";"

    myfile = pyblish_win.util.where("myfile")
    assert_equals(os.path.basename(myfile).lower(), "myfile.exe")

    notexec = pyblish_win.util.where("notexec")
    assert_equals(notexec, None)
