def find_duplicate(list_of_number: list[int]):

    duplicates = list(set([number for number in list_of_number if list_of_number.count(number) > 1]))

    return duplicates


if __name__ == "__main__":
    print(find_duplicate([1, 2, 3, 2, 4, 5, 4, 6]))
