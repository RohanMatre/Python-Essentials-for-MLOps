from utils import str_to_int


def test_str_to_int_fails():
    result = str_to_int("14,44")
    assert result == 14


def test_str_to_int_decimals():
    result = str_to_int("14.44")
    assert result == 14


def test_str_to_int_with_integers():
    result = str_to_int(10)
    assert result == 10


# (base) rohanmatre@192 LESSON3 % pytest test_failure_output.py 
# ===================================================================== test session starts ======================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3
# plugins: anyio-3.5.0
# collected 3 items                                                                                                                                              

# test_failure_output.py F..                                                                                                                               [100%]

# =========================================================================== FAILURES ===========================================================================
# ____________________________________________________________________ test_str_to_int_fails _____________________________________________________________________

# string = '14, 44'

#     def str_to_int(string):
#         """
#         Parses a string number into an integer, optionally converting to a float
#         and rounding down.
#         You can pass "1.1" which returns 1
#         ["1"] -> raises RuntimeError
#         """
#         error_msg = "Unable to convert to integer: '%s'" % str(string)
#         try:
# >           integer = float(string.replace(',', '.'))
# E           ValueError: could not convert string to float: '14. 44'

# utils.py:11: ValueError

# During handling of the above exception, another exception occurred:

#     def test_str_to_int_fails():
# >       result = str_to_int("14, 44")

# test_failure_output.py:5: 
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# string = '14, 44'

#     def str_to_int(string):
#         """
#         Parses a string number into an integer, optionally converting to a float
#         and rounding down.
#         You can pass "1.1" which returns 1
#         ["1"] -> raises RuntimeError
#         """
#         error_msg = "Unable to convert to integer: '%s'" % str(string)
#         try:
#             integer = float(string.replace(',', '.'))
#         except AttributeError:
#             # this might be a integer already, so try to use it, otherwise raise
#             # the original exception
#             if isinstance(string, (int, float)):
#                 integer = string
#             else:
#                 raise RuntimeError(error_msg)
#         except (TypeError, ValueError):
# >           raise RuntimeError(error_msg)
# E           RuntimeError: Unable to convert to integer: '14, 44'

# utils.py:20: RuntimeError
# =================================================================== short test summary info ====================================================================
# FAILED test_failure_output.py::test_str_to_int_fails - RuntimeError: Unable to convert to integer: '14, 44'
# ================================================================= 1 failed, 2 passed in 0.08s ==================================================================
# (base) rohanmatre@192 LESSON3 % pytest -v test_failure_output.py
# ===================================================================== test session starts ======================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0 -- /Users/rohanmatre/anaconda3/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3
# plugins: anyio-3.5.0
# collected 3 items                                                                                                                                              

# test_failure_output.py::test_str_to_int_fails FAILED                                                                                                     [ 33%]
# test_failure_output.py::test_str_to_int_decimals PASSED                                                                                                  [ 66%]
# test_failure_output.py::test_str_to_int_with_integers PASSED                                                                                             [100%]

# =========================================================================== FAILURES ===========================================================================
# ____________________________________________________________________ test_str_to_int_fails _____________________________________________________________________

# string = '14, 44'

#     def str_to_int(string):
#         """
#         Parses a string number into an integer, optionally converting to a float
#         and rounding down.
#         You can pass "1.1" which returns 1
#         ["1"] -> raises RuntimeError
#         """
#         error_msg = "Unable to convert to integer: '%s'" % str(string)
#         try:
# >           integer = float(string.replace(',', '.'))
# E           ValueError: could not convert string to float: '14. 44'

# utils.py:11: ValueError

# During handling of the above exception, another exception occurred:

#     def test_str_to_int_fails():
# >       result = str_to_int("14, 44")

# test_failure_output.py:5: 
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# string = '14, 44'

#     def str_to_int(string):
#         """
#         Parses a string number into an integer, optionally converting to a float
#         and rounding down.
#         You can pass "1.1" which returns 1
#         ["1"] -> raises RuntimeError
#         """
#         error_msg = "Unable to convert to integer: '%s'" % str(string)
#         try:
#             integer = float(string.replace(',', '.'))
#         except AttributeError:
#             # this might be a integer already, so try to use it, otherwise raise
#             # the original exception
#             if isinstance(string, (int, float)):
#                 integer = string
#             else:
#                 raise RuntimeError(error_msg)
#         except (TypeError, ValueError):
# >           raise RuntimeError(error_msg)
# E           RuntimeError: Unable to convert to integer: '14, 44'

# utils.py:20: RuntimeError
# =================================================================== short test summary info ====================================================================
# FAILED test_failure_output.py::test_str_to_int_fails - RuntimeError: Unable to convert to integer: '14, 44'
# ================================================================= 1 failed, 2 passed in 0.09s ==================================================================