def get_text(filename):
    with open(filename, 'r') as fl:
        data = fl.readlines()
    return data

def count_words(str_lst):
    total_words = 0
    for i in range(len(str_lst)):
        str_lst[i] = str_lst[i].split(' ')
    for each in str_lst:
        total_words+=len(each)
    total_array = [i for sublist in str_lst for i in sublist]
    yield total_words
    for i in total_array:
        yield len(i)


a = count_words(get_text('text.txt'))
for each in a:
    print(each)