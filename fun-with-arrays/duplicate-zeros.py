from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    output_array = [

    ]
    for i in arr:
        if len(arr) == len(output_array):
            break
        elif i == 0:
            output_array.append(0)
            output_array.append(0)
        else:
            output_array.append(i)

    arr = output_array

def main():
    print(duplicateZeros([12, 345, 2, 6, 7896]))


if __name__ == "__main__":
    main()