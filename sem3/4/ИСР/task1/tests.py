import main


print(main.list_to_prettystring([[], []]))


try:
    assert type(main.make_table([{'a': '1'}, {'b': '2'}])) == type(str())
except:
    print('It`s not a list of dicts')
try:
    assert type(main.list_to_prettystring([[1, 2], [3, 4]])) == type(str())
except:
    print('It`s not list of lists')
try:
    assert type(main.list_to_prettystring([[1, 2], [3, '4']])) == type(str())
except:
    print('It`s not list of lists')
try:
    assert type(main.get_from_file()) == type(dict())
except:
    print('Vals from file imported not as a dict')
