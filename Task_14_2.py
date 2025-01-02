my_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def rec(x):
    if my_list == []:
        return print("конец списка")
    else:
        print(my_list[0])
        my_list.pop(0)
        rec(my_list)

rec(my_list)
