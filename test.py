list1 = []

def big(list2):

    while len(list2) < 4:
        list2.append('a')
        big(list2)

big(list1)

list3 = list1

memo = [[(-1, []) for _ in range(10)] for _ in range(10)]

print(memo[1][1][1])