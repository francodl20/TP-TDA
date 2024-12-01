list1 = []

def big(list2):

    while len(list2) < 4:
        list2.append('a')
        big(list2)

big(list1)

list3 = list1