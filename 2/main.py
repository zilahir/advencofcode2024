import numpy as np


def is_valid(numbers):
    arr = np.array(numbers, dtype=int)
    is_increasing = np.all(np.diff(arr) > 0)
    is_decreasing = np.all(np.diff(arr) < 0)
    return (is_increasing or is_decreasing) and (np.max(np.abs(np.diff(arr))) <= 3)


def main():
    result_indexes = []
    with open("input.txt", "r") as file:
        # for line in file:
        lines = file.readlines()
        for lidx in range(len(lines)):
            line = lines[lidx]
            numbers = line.split()
            valiid = False

            for i in range(len(numbers)):
                # check if strictly increasing or strictly decreasing
                arr = np.array(numbers, dtype=int)
                temp_numbers = np.concatenate((arr[:i], arr[i + 1 :]))
                if is_valid(temp_numbers):
                    valiid = True
                    break
            if is_valid(numbers):
                valiid = True
            if valiid:
                result_indexes.append(lidx)

    print(f"Total number of valid lines: {len(result_indexes)}\n")
    # print(f"index of valid lines: {result_indexes}")


if __name__ == "__main__":
    main()
