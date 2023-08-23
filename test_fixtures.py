import os
from utils import str_to_bool


def write_integer(string, path):
    with open(path, "w") as _f:
        try:
            _f.write(str(str_to_bool(string)))
        except RuntimeError:
            _f.write(0)


class TestWriteBooleans:

    def setup(self):
        if os.path.exists("/tmp/test_value"):
            os.remove("/tmp/test_value")

    def test_write_Yes(self):
        write_integer("Yes", "/tmp/test_value")
        with open("/tmp/test_value", "r") as _f:
            value = _f.read()

        assert value == "True"

    def test_write_n(self):
        write_integer("n", "/tmp/test_value")
        with open("/tmp/test_value", "r") as _f:
            value = _f.read()

        assert value == "False"


class TestFixtures:

    def test_write_Yes(self, tmpdir):
        path = str(tmpdir.join("test_value"))
        # print("The path from tmpdir fixture is: ", path)
        # assert False                      
        write_integer("Yes", path)
        with open(path, "r") as _f:
            value = _f.read()

        assert value == "True"

# (base) rohanmatre@192 LESSON3 % pytest -v test_fixtures.py
# ====================================================================================== test session starts ======================================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0 -- /Users/rohanmatre/anaconda3/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3
# plugins: anyio-3.5.0
# collected 3 items                                                                                                                                                                               

# test_fixtures.py::TestWriteBooleans::test_write_Yes PASSED                                                                                                                                [ 33%]
# test_fixtures.py::TestWriteBooleans::test_write_n PASSED                                                                                                                                  [ 66%]
# test_fixtures.py::TestFixtures::test_write_Yes FAILED                                                                                                                                     [100%]

# =========================================================================================== FAILURES ============================================================================================
# __________________________________________________________________________________ TestFixtures.test_write_Yes __________________________________________________________________________________

# self = <test_fixtures.TestFixtures object at 0x10667f640>, tmpdir = local('/private/var/folders/p5/n7j5q_px2cd9h403j_hqqldc0000gn/T/pytest-of-rohanmatre/pytest-1/test_write_Yes0')

#     def test_write_Yes(self, tmpdir):
#         path = str(tmpdir.join("test_value"))
#         print("The path from tmpdir fixture is: ", path)
# >       assert False
# E       assert False

# test_fixtures.py:39: AssertionError
# ------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------
# The path from tmpdir fixture is:  /private/var/folders/p5/n7j5q_px2cd9h403j_hqqldc0000gn/T/pytest-of-rohanmatre/pytest-1/test_write_Yes0/test_value
# ==================================================================================== short test summary info ====================================================================================
# FAILED test_fixtures.py::TestFixtures::test_write_Yes - assert False