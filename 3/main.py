import re


def main():
    with open("input.txt", "r") as file:
        # read input
        input = file.read().strip()
        # close input file
        file.close()

    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize state
    mul_enabled = True
    result = 0

    tokens = re.split(r"(\bdo\(\)|\bdon't\(\))", input)
    for token in tokens:
        token = token.strip()
        if re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False
        else:
            for x, y in re.findall(mul_pattern, token):
                if mul_enabled:
                    x, y = int(x), int(y)
                    print(f"{x} * {y}")
                    result += x * y

    print(f"Total Sum: {result}")


def main_():
    # open input file
    with open("input.txt", "r") as file:
        # read input
        input = file.read().strip()
        # close input file
        file.close()

    # print(input)
    # pattern = r"mul[\(\[\{]?(\d+),(\d+)[\)\]\}]?"
    pattern = r"mul\((\d+),(\d+)\)"

    # example input xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    # find all mul(x,y) and evalute expression
    muls = re.findall(pattern, input)
    # print(muls)

    result = 0
    for mul in muls:
        x = int(mul[0])
        y = int(mul[1])
        print(f"{x} * {y}")
        result += x * y

    print(result)


if __name__ == "__main__":
    main()
