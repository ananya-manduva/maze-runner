# Maze Generation with Prim's Algorithm in Pygame

This project demonstrates how to generate mazes using Prim's Algorithm in Pygame. The maze is created cell-by-cell with a visual representation of the algorithm’s steps. You can run the program to see how the maze is progressively built and interact with it by generating new mazes.

## Features
- Maze generation using Prim's Algorithm.
- Visualizes maze generation step-by-step.
- Pygame-based interface for an interactive experience.
- Random start point and frontier cells for dynamic maze generation.

## Prerequisites
- Python 3.x
- Pygame library (`pygame`)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/ananya-manduva/maze-runner.git
   cd maze-runner
   ```

2. Install the required Python library:
   ```bash
   pip install pygame
   ```

3. Run the maze generator:
   ```bash
   python prim-algorithm.py
   ```


## Description
This project uses Prim's Algorithm to generate mazes. Starting from a random cell, it creates passages to neighboring cells, marking them as part of the maze. The process continues until all cells are visited and connected. The algorithm's steps are visualized with cells being highlighted as the maze grows.

## Code Overview
- `main.py`: Main script to run the maze generator and visualizer.
- `prims_algorithm.py`: Implementation of Prim's Algorithm.
- `README.md`: This file.

## Maze Image

![image](https://github.com/user-attachments/assets/6c3ca082-e0ea-4757-a16e-1b4a7e1bbf10)





