from itertools import product


def evaluate_left_to_right(numbers, operators):
    """Evaluate the expression left-to-right given numbers and operators."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result


def solve_line(target, numbers):
    """Check if any combination of operators results in the target value."""
    num_count = len(numbers)
    # Generate all possible operator combinations: '+' or '*'
    for operators in product(["+", "*"], repeat=num_count - 1):
        result = evaluate_left_to_right(numbers, operators)
        if result == target:
            return True  # Found a valid equation
    return False


def main():
    total_sum = 0
    with open("input.txt", "r") as file:
        for line in file:
            # Parse each line
            test_value, number_list = line.strip().split(":")
            target = int(test_value)
            numbers = list(map(int, number_list.split()))

            # Check if any equation works
            if solve_line(target, numbers):
                total_sum += target

    print("Total Calibration Result:", total_sum)


if __name__ == "__main__":
    main()
