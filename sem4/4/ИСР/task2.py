from random import randint



def split_lists(list):
    list1 = []
    list2 = []
    for each in list:
        if each % 2 == 0:
            list1.append(each)
        else:
            list2.append(each)
    return list1, list2    

def main():
    n = 20
    arr = [randint(1,31) for i in range(n)]    
    print(arr)
    l1, l2 = split_lists(arr)
    print(l1, l2)

main()