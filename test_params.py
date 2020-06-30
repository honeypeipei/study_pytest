# @File  : test_params.py
# @Author: leipei
# @Date  :  2020/06/29

import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5",8),
                                                 ("2-1",1),
                                                 ("7*5",30),
                                                 ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


if __name__ == "__main__":
    pytest.main()