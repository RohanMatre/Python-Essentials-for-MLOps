
def str_to_int(string):
    """
    Parses a string number into an integer, optionally converting to a float
    and rounding down.
    You can pass "1.1" which returns 1
    ["1"] -> raises RuntimeError
    """
    import pdb;
    pdb.set_trace()

    error_msg = "Unable to convert to integer: '%s'" % str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        # this might be a integer already, so try to use it, otherwise raise
        # the original exception
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
        raise RuntimeError(error_msg)

    return int(integer)


def str_to_bool(val):
    """
    Convert a string representation of truth to True or False
    True values are 'y', 'yes', or ''; case-insensitive
    False values are 'n', or 'no'; case-insensitive
    Raises ValueError if 'val' is anything else.
    """
    true_vals = ['yes', 'y', '']
    false_vals = ['no', 'n']
    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError("Invalid input value: %s" % val)


# base) rohanmatre@192 LESSON3 % pytest -v test_failure_output.py
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

# (base) rohanmatre@192 LESSON3 % pytest --pdb test_failure_output.py 
# ====================================================================================== test session starts ======================================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3
# plugins: anyio-3.5.0
# collected 3 items                                                                                                                                                                               

# test_failure_output.py F
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3/utils.py(20)str_to_int()
# -> raise RuntimeError(error_msg)
# (Pdb) h

# Documented commands (type help <topic>):
# ========================================
# EOF    cl         down      j         next     return  tbreak     w     
# a      clear      enable    jump      p        retval  u          whatis
# alias  commands   exit      l         pp       run     unalias    where 
# args   condition  h         list      q        rv      undisplay
# b      d          help      ll        quit     s       unt      
# break  disable    ignore    longlist  r        source  until    
# bt     display    interact  n         restart  step    up       

# Miscellaneous help topics:
# ==========================
# exec  pdb

# Undocumented commands:
# ======================
# c  cont  continue  debug

# (Pdb) l
#  15             if isinstance(string, (int, float)):
#  16                 integer = string
#  17             else:
#  18                 raise RuntimeError(error_msg)
#  19         except (TypeError, ValueError):
#  20  ->         raise RuntimeError(error_msg)
#  21  
#  22         return int(integer)
#  23  
#  24  
#  25     def str_to_bool(val):
# (Pdb) integer
# *** NameError: name 'integer' is not defined
# (Pdb) string
# '14, 44'
# (Pdb) l 10
#   5         and rounding down.
#   6         You can pass "1.1" which returns 1
#   7         ["1"] -> raises RuntimeError
#   8         """
#   9         error_msg = "Unable to convert to integer: '%s'" % str(string)
#  10         try:
#  11             integer = float(string.replace(',', '.'))
#  12         except AttributeError:
#  13             # this might be a integer already, so try to use it, otherwise raise
# (base) rohanmatre@192 LESSON3 % pytest -s test_failure_output.py
# ====================================================================================== test session starts ======================================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3
# plugins: anyio-3.5.0
# collected 3 items                                                                                                                                                                               

# test_failure_output.py 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3/utils.py(12)str_to_int()
# -> error_msg = "Unable to convert to integer: '%s'" % str(string)
# (Pdb) c

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB continue >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# F
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3/utils.py(12)str_to_int()
# -> error_msg = "Unable to convert to integer: '%s'" % str(string)
# (Pdb) c

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB continue >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# .
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3/utils.py(12)str_to_int()
# -> error_msg = "Unable to convert to integer: '%s'" % str(string)
# (Pdb) c

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB continue >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# .

# =========================================================================================== FAILURES ============================================================================================
# _____________________________________________________________________________________ test_str_to_int_fails _____________________________________________________________________________________

# string = '14, 44'

#     def str_to_int(string):
#         """
#         Parses a string number into an integer, optionally converting to a float
#         and rounding down.
#         You can pass "1.1" which returns 1
#         ["1"] -> raises RuntimeError
#         """
#         import pdb;
#         pdb.set_trace()
    
#         error_msg = "Unable to convert to integer: '%s'" % str(string)
#         try:
# >           integer = float(string.replace(',', '.'))
# E           ValueError: could not convert string to float: '14. 44'

# utils.py:14: ValueError

# During handling of the above exception, another exception occurred:

#     def test_str_to_int_fails():
# >       result = str_to_int("14, 44")

# test_failure_output.py:5: 
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# string = '14, 44'

#     def str_to_int(string):
#         """
#         Parses a string number into an integer, optionally converting to a float
#         and rounding down.
#         You can pass "1.1" which returns 1
#         ["1"] -> raises RuntimeError
#         """
#         import pdb;
#         pdb.set_trace()
    
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

# utils.py:23: RuntimeError
# ==================================================================================== short test summary info ====================================================================================
# FAILED test_failure_output.py::test_str_to_int_fails - RuntimeError: Unable to convert to integer: '14, 44'
# ================================================================================= 1 failed, 2 passed in 16.50s ==================================================================================
# (base) rohanmatre@192 LESSON3 % pytest -s test_failure_output.py
# ====================================================================================== test session starts ======================================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3
# plugins: anyio-3.5.0
# collected 3 items                                                                                                                                                                               

# test_failure_output.py 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON3/utils.py(12)str_to_int()
# -> error_msg = "Unable to convert to integer: '%s'" % str(string)
# (Pdb) l
#   7         ["1"] -> raises RuntimeError
#   8         """
#   9         import pdb;
#  10         pdb.set_trace()
#  11  
#  12  ->     error_msg = "Unable to convert to integer: '%s'" % str(string)
#  13         try:
#  14             integer = float(string.replace(',', '.'))
#  15         except AttributeError:
#  16             # this might be a integer already, so try to use it, otherwise raise
#  17             # the original exception
# (Pdb) string
# '14, 44'
# (Pdb) q


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! _pytest.outcomes.Exit: Quitting debugger !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ==================================================================================== no tests ran in 45.84s =====================================================================================
