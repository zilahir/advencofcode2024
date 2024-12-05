from collections import defaultdict, deque


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


def find_correct_update_in_wrong_order(update, graph, in_degree):
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
    incorrect_orders = []

    for update in updates:
        if is_update_in_order(update, graph, in_degree):
            results.append("yo")
            correct_orders.append(update)
        else:
            results.append("notyo")
            incorrect_orders.append(update)

    return results, correct_orders, incorrect_orders


def correct_order(update, graph, in_degree):
    update_set = set(update)
    filtered_graph = defaultdict(list)
    filtered_in_degree = defaultdict(int)

    for page in update_set:
        if page in graph:
            for neighbor in graph[page]:
                if neighbor in update_set:
                    filtered_graph[page].append(neighbor)
                    filtered_in_degree[neighbor] += 1

    for page in update_set:
        if page not in filtered_in_degree:
            filtered_in_degree[page] = 0

    zero_in_degree_queue = deque(
        [page for page in update_set if filtered_in_degree[page] == 0]
    )
    sorted_order = []

    while zero_in_degree_queue:
        page = zero_in_degree_queue.popleft()
        sorted_order.append(page)

        for neighbor in filtered_graph[page]:
            filtered_in_degree[neighbor] -= 1
            if filtered_in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)

    if len(sorted_order) == len(update):
        return sorted_order
    else:
        return update


def main():
    with open("input.txt", "r") as file:
        input = file.read().strip()
        file.close()

    page_ordering_rules, updates = process_file(input)
    # print(page_ordering_rules)
    # print(updates)

    _, correct_orders, incorrect_orders = process_task(page_ordering_rules, updates)

    sum = 0
    sum_incorrect = 0
    for order in correct_orders:
        # get middle number of order
        middle = len(order) // 2
        sum += order[middle]

    for order in incorrect_orders:
        correct = correct_order(order, *build_graph(page_ordering_rules))
        middle = len(correct) // 2
        sum_incorrect += correct[middle]

    print(sum_incorrect)


if __name__ == "__main__":
    main()
