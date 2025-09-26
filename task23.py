def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    num_dict: dict[int, list[int]] = {}

    for index, value in enumerate(numbers, start=0):
        if value not in num_dict:
            num_dict[value] = []
        num_dict[value].append(index)

    return num_dict


def main():
    nums = [1, 2, 1, 3, 2, 1, 3]
    result = group_indices(nums)
    print(result)  # {1: [0, 2, 5], 2: [1, 4], 3: [3, 6]}


main()
