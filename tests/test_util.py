import pytest
from util import return_first_arg


####################
@pytest.mark.parametrize(
    "arg1, arg2, solution",
    [(1, 2, 1), (0, 0, 0)],
)
def test_return_first_arg(arg1, arg2, solution):
    my_sol = return_first_arg(arg1, arg2)
    assert solution == my_sol
