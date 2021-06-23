import unittest
import main


class TestTableMethods(unittest.TestCase):

    def test_maketable_is_str(self):
        self.assertEqual(type(main.make_table([{'a': '1'}, {'b': '2'}])), type(str()))

    def test_lst_to_str(self):
        self.assertEqual(type(main.list_to_prettystring([[1, 2], [3, 4]])), type(str()))
        self.assertEqual(type(main.list_to_prettystring([[1, 2], [3, '4']])), type(str()))

    def test_file_extr(self):
        self.assertEqual(type(main.get_from_file()), type(dict()))


TestTableMethods()
