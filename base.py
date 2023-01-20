import random


def swap(first_element,second_element)->int:
    first_element,second_element = second_element,first_element
    return first_element,second_element

def test_arrays() -> list:
    lst = []
    ran = range(10)
    for i in range(10):
        j = random.randint(0,ran[len(ran)-1])
        lst.append(j)
    return lst