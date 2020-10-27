from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    previous_counter, current_counter, prev_value = (0, 0, 0)
    for i in nums:
        if prev_value == 0 and i == 1:
            current_counter = 1
        elif prev_value == 1:
            if i == 1:
                current_counter += 1
            elif i == 0:
                previous_counter = max(current_counter, previous_counter)
                current_counter = 0

        prev_value = i
    if previous_counter > current_counter:
        current_counter = previous_counter

    return current_counter


def main():
    print(findMaxConsecutiveOnes([1, 0, 1, 1, 0]))


if __name__ == "__main__":
    main()
