import pytest
from utils import str_to_bool

# def test_yes_is_true():
#     result = str_to_bool('yes')
#     assert result is True


# def test_y_is_true():
#     result = str_to_bool('y')
#     assert result is True


@pytest.mark.parametrize('value', ['n', 'no'])
# this above value is injected down 
def test_is_false(value):
    result = str_to_bool(value)
    assert result is False

# pytest Parameterizing Tests
# @pytest.mark.parametrize('value', ['N','y', 'yes', ''])
@pytest.mark.parametrize('value', ['y', 'yes', ''])
# this above value is injected down 
def test_is_true(value):
    result = str_to_bool(value)
    assert result is True


#Solution: vscode
# (base) rohanmatre@192 parametrize % pytest -v
# ====================================================================================== test session starts ======================================================================================
# platform darwin -- Python 3.10.12, pytest-7.1.2, pluggy-1.0.0 -- /Users/rohanmatre/anaconda3/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/rohanmatre/Documents/MLOP's/Course1/Week3/LESSON2/parametrize
# plugins: anyio-3.5.0
# collected 5 items                                                                                                                                                                               

# test_utils.py::test_is_false[n] PASSED                                                                                                                                                    [ 20%]
# test_utils.py::test_is_false[no] PASSED                                                                                                                                                   [ 40%]
# test_utils.py::test_is_true[y] PASSED                                                                                                                                                     [ 60%]
# test_utils.py::test_is_true[yes] PASSED                                                                                                                                                   [ 80%]
# test_utils.py::test_is_true[] PASSED                                                                                                                                                      [100%]

# ======================================================================================= 5 passed in 0.01s =======================================================================================