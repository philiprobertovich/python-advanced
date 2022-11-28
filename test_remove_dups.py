import pytest
from faker import Faker
from python_advanced import remove_dups


@pytest.mark.parametrize("color_lst, return_value", [
  (["green", "green", "green", "blue", "blue", "blue", "red"], ["green","blue","red"]),
  ([], []),
  ("blue", "blue")
])

def test_remove_dups(color_lst, return_value):
  assert remove_dups(color_lst) == return_value