import pytest
from radix_string.radix_string import radix_string
from random import randint

TEST_COUNT = 500


@pytest.mark.parametrize(
    "number,radix",
    [
        (randint(-1_000_000_000, 1_000_000_000), randint(2, 26))
        for _ in range(TEST_COUNT)
    ],
)
def test_radix_convert(number, radix):
    string = radix_string(number, radix)
    assert int(string, radix) == number
