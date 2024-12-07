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


def simulate_guard_with_obstruction(
    grid, guard_pos, guard_dir, directions, obstruction
):
    """Simulates the guard's movement with an added obstruction to detect cycles."""
    x, y = guard_pos
    dx, dy = guard_dir

    # Add the obstruction
    ox, oy = obstruction
    grid[oy][ox] = "#"

    visited_states = set()
    while True:
        state = (x, y, dx, dy)
        if state in visited_states:
            # Cycle detected
            grid[oy][ox] = "."  # Remove obstruction before returning
            return True
        visited_states.add(state)

        # Compute the next position
        next_pos = (x + dx, y + dy)
        if is_within_bounds(next_pos, grid) and grid[next_pos[1]][next_pos[0]] != "#":
            # Move forward
            x, y = next_pos
        else:
            # Turn right
            dx, dy = turn_right((dx, dy), directions)

        # Check if the guard is about to leave the map
        next_x, next_y = x + dx, y + dy
        if not is_within_bounds((next_x, next_y), grid):
            grid[oy][ox] = "."  # Remove obstruction before returning
            return False


def find_valid_obstruction_positions(grid, guard_pos, guard_dir, directions):
    valid_positions = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "." and (x, y) != guard_pos:
                # Test this position as an obstruction
                if simulate_guard_with_obstruction(
                    grid, guard_pos, guard_dir, directions, (x, y)
                ):
                    valid_positions.add((x, y))

    return valid_positions


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

    # visited_positions = simulate_guard(grid, guard_pos, guard_dir, directions)
    valid_obstructions = find_valid_obstruction_positions(
        grid, guard_pos, guard_dir, directions
    )

    # print(len(visited_positions))
    print(len(valid_obstructions))


if __name__ == "__main__":
    main()
