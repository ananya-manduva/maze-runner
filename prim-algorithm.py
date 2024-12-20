# Prim's Algorithm
# 1. choose a random cell on the grid to start generating and mark it as the passage way (0)
# 2. The algorithm looks in all 4 directions (4 boxes around it) and if a box hasn't been visited yet (marked by a 1), it becomes a canidate to become part of the maze
# 3. It will pick one of the 4 (less if some were already visited) cells by random and mark that cell with a (0), creating a passageway by removing the wall btwn current cell and new cell
# 4. After marking a new cell as part of the maze, it will once again look at neighboring cells for an unvisited cell; continue until all cells are visited and connected
# 5. The algorithm stops after there are no more unvisited cells left to connect

import random
import pygame
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 100, 100       # change to increase/decrease number of squares
CELL_SIZE = min(WIDTH // COLS, HEIGHT // ROWS)
GENERATION_DELAY = 0.05  # Delay between steps in seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)     # For highlighting frontier cells
GREEN = (0, 255, 0)   # For highlighting current cell

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prim's Maze")

def draw_grid(grid, current=None, frontier=None):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if grid[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, 
                           (col * CELL_SIZE, row * CELL_SIZE, 
                            CELL_SIZE, CELL_SIZE))
    
    # Highlight frontier cells
    if frontier:
        for y, x in frontier:
            pygame.draw.rect(screen, RED,
                           (x * CELL_SIZE, y * CELL_SIZE,
                            CELL_SIZE, CELL_SIZE))
    
    # Highlight current cell
    if current:
        y, x = current
        pygame.draw.rect(screen, GREEN,
                        (x * CELL_SIZE, y * CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()

def generate_maze_step_by_step():
    # Initialize grid with walls
    grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]
    
    # Start from a random cell
    start_y, start_x = random.randint(0, ROWS-1), random.randint(0, COLS-1)
    grid[start_y][start_x] = 0
    
    # Initialize frontier cells
    frontier = []
    add_frontier_cells(grid, start_y, start_x, frontier)
    
    # Draw initial state
    draw_grid(grid, (start_y, start_x), frontier)
    time.sleep(GENERATION_DELAY)
    
    while frontier:
        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
        
        # Pick a random frontier cell
        current = random.choice(frontier)
        frontier.remove(current)
        y, x = current
        
        # Find neighbors that are paths
        neighbors = []
        for dy, dx in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < ROWS and 0 <= nx < COLS and grid[ny][nx] == 0:
                neighbors.append((ny, nx))
        
        if neighbors:
            # Connect to a random neighbor
            ny, nx = random.choice(neighbors)
            # Mark the cell and the wall between as path
            grid[y][x] = 0
            grid[y + (ny - y) // 2][x + (nx - x) // 2] = 0
            # Add new frontier cells
            add_frontier_cells(grid, y, x, frontier)
        
        # Update display
        draw_grid(grid, (y, x), frontier)
        time.sleep(GENERATION_DELAY)
    
    return grid

def add_frontier_cells(grid, y, x, frontier):
    # Check in all four directions
    for dy, dx in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
        ny, nx = y + dy, x + dx
        if (0 <= ny < ROWS and 0 <= nx < COLS and 
            grid[ny][nx] == 1 and 
            (ny, nx) not in frontier):
            frontier.append((ny, nx))

def main():
    clock = pygame.time.Clock()
    grid = None
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid = generate_maze_step_by_step()
        
        # Generate initial maze if none exists
        if grid is None:
            grid = generate_maze_step_by_step()
        
        # Draw the final maze state
        if grid:
            draw_grid(grid)
        
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()