import main
import pytest


def tests():
    assert type(main.make_table([{'a': '1'}, {'b': '2'}])) == type(str())
    assert type(main.list_to_prettystring([[1, 2], [3, 4]])) == type(str())
    assert type(main.list_to_prettystring([[1, 2], [3, '4']])) == type(str())
    assert type(main.get_from_file()) == type(dict())


tests()
