def parse_map(input_map):
    grid = [list(row) for row in input_map.strip().split("\n")]
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    guard_pos = None
    guard_dir = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                guard_pos = (x, y)
                guard_dir = directions[cell]
                grid[y][x] = "."  # Clear the guard's position
                break
        if guard_pos:
            break

    return grid, guard_pos, guard_dir, directions


def turn_right(direction, directions):
    order = list(directions.values())
    new_index = (order.index(direction) + 1) % len(order)
    return order[new_index]


def is_within_bounds(pos, grid):
    x, y = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def simulate_guard(grid, guard_pos, guard_dir, directions):
    visited = set()
    x, y = guard_pos
    visited.add((x, y))

    while True:
        dx, dy = guard_dir
        next_pos = (x + dx, y + dy)

        if is_within_bounds(next_pos, grid) and grid[next_pos[1]][next_pos[0]] != "#":
            x, y = next_pos
            visited.add((x, y))
        else:
            guard_dir = turn_right(guard_dir, directions)

        next_x, next_y = x + guard_dir[0], y + guard_dir[1]
        if not is_within_bounds((next_x, next_y), grid):
            break

    return visited


def mark_visited_positions(grid, visited):
    """Marks visited positions on the map."""
    for x, y in visited:
        if grid[y][x] == ".":
            grid[y][x] = "X"
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))


def main():
    with open("input.txt") as file:
        input_map = file.read().strip()

    grid, guard_pos, guard_dir, directions = parse_map(input_map)

    visited_positions = simulate_guard(grid, guard_pos, guard_dir, directions)

    # Output results
    print("Distinct positions visited:", len(visited_positions))
    print("\nFinal map with visited positions marked:")
    # print_grid(marked_grid)
    print(len(visited_positions))


if __name__ == "__main__":
    main()
