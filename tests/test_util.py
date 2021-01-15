import pytest
from util import my_util_function

####################
@pytest.mark.parametrize(
    "arg1, arg2, solution",
    [(1, 2, 1), (0, 0, 0)],
)
def test_my_util_function(arg1, arg2, solution):
    my_sol = my_util_function(arg1, arg2)
    assert solution == my_sol