from typing import List
def rocket(list_:List[int]) -> bool:

    list_ = sorted(list_)

    for i in range(3):
        if list_[i][1] > list_[i +1][0]:
            return False
    return True

if __name__ == '__main__':
    orders = [(1, 5), (6, 7), (22, 24), (7, 13), (15, 20)]
    orders2 = [(13, 15), (15, 20),(18, 23)]
    print(rocket(orders))
    print(rocket(orders2))