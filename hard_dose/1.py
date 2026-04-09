import collections

def solve_rover_arena():
    # 1. Setup the Arena (11x11 matrix) [cite: 189]
    # 1 = Safe position, 0 = Obstacle 
    size = 11
    arena = [[1 for _ in range(size)] for _ in range(size)]
    
    # 2. Add Obstacles based on the sample.txt format [cite: 179-183]
    # In the task, columns represent North, East, South, West distances [cite: 171-178]
    # We'll mark specific coordinates as obstacles (0)
    obstacles = [
        (2, 3), (5, 1), (3, 0), (3, 4) 
    ]
    
    for r, c in obstacles:
        if 0 <= r < size and 0 <= c < size:
            arena[r][c] = 0

    # 3. Print the matrix to the console 
    print("--- Arena Map ---")
    for row in arena:
        print(" ".join(map(str, row)))

    # 4. Pathfinding (BFS for shortest path) 
    start = (0, 0)
    goal = (10, 10)
    
    queue = collections.deque([(start, [start])])
    visited = {start}
    
    found_path = None
    
    while queue:
        (curr_r, curr_c), path = queue.popleft()
        
        if (curr_r, curr_c) == goal:
            found_path = path
            break
            
        # Movement: King style (North, South, East, West) but NO diagonals [cite: 186-187]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr_r + dr, curr_c + dc
            
            # Stay inside grid, hit safe spots only, and don't backtrack
            if 0 <= nr < size and 0 <= nc < size:
                if arena[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    # 5. Show Results
    print("\n--- Mission Result ---")
    if found_path:
        print(f"Shortest path to {goal} found!")
        print("Steps:", " -> ".join(map(str, found_path)))
        print(f"Total distance: {len(found_path) - 1} meters")
    else:
        print("No path found! Rover is blocked by obstacles.")

if __name__ == "__main__":
    solve_rover_arena()