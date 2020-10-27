from typing import List


def findNumbers(nums: List[int]) -> int:
    counter = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            counter += 1

    return counter


def main():
    print(findNumbers([12, 345, 2, 6, 7896]))


if __name__ == "__main__":
    main()
