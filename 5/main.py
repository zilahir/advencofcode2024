from collections import defaultdict


def process_file(input_text):
    part1, part2 = input_text.strip().split("\n\n")
    part1_2d_array = [
        [int(x), int(y)] for x, y in (line.split("|") for line in part1.splitlines())
    ]

    part2_2d_array = [
        [int(num) for num in line.split(",")] for line in part2.splitlines()
    ]

    return part1_2d_array, part2_2d_array


def build_graph(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for rule in rules:
        x, y = rule
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0

    return graph, in_degree


def is_update_in_order(update, graph, in_degree):
    # Create a mapping from page number to its position in the update
    position = {page: idx for idx, page in enumerate(update)}

    # Check the ordering constraints
    for u in update:
        for v in graph[u]:
            if v in position and position[u] > position[v]:
                return False
    return True


def process_task(rules, updates):
    graph, in_degree = build_graph(rules)
    results = []
    correct_orders = []

    for update in updates:
        if is_update_in_order(update, graph, in_degree):
            results.append("yo")
            correct_orders.append(update)
        else:
            results.append("notyo")

    return results, correct_orders


def main():
    with open("input.txt", "r") as file:
        # read input
        input = file.read().strip()
        # close input file
        file.close()

    page_ordering_rules, updates = process_file(input)
    # print(page_ordering_rules)
    # print(updates)

    results, correct_orders = process_task(page_ordering_rules, updates)
    print("\n".join(results))
    print("\n".join([",".join(map(str, order)) for order in correct_orders]))

    sum = 0
    for order in correct_orders:
        # get middle number of order
        middle = len(order) // 2
        sum += order[middle]

    print(sum)


if __name__ == "__main__":
    main()
