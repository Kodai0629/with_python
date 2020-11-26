from typing import List
import random


def generate_10_numbers_from_0_until_100() -> List[int]:
    List=random.sample(range(0,100),k=10)
    return List


def print_list(numbers: List[int]):
    for i in numbers:
        print(i)



def sort_in_ascending_order(numbers: List[int]) -> List[int]:
    i=sorted(numbers)
    return i


def remove_content_which_number_is_under_50(numbers: List[int]) -> List[int]:
    i=[e for e in numbers if e>50]
    return i


if __name__ == '__main__':
    List=generate_10_numbers_from_0_until_100()
    print_list(List)
    print('----')
    print_list(sort_in_ascending_order(List))
    print('----')
    print_list(remove_content_which_number_is_under_50(List))


