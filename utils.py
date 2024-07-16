def debugg_drawer_of_pipe_system(grid):
    """
      This function prints a visual representation of the pipe system on the console for debugging.

      Args:
          grid (list): List of dicts representing the pipe system data (object, x, y, is_visited).
      """

    # Get grid dimensions
    max_x = max(cell.x for cell in grid) + 1
    max_y = max(cell.y for cell in grid) + 1

    # Print top border
    print("+" + "-" * (max_x) + "+")

    # Print each row
    for y in range(max_y-1, -1, -1):
        # Print left border
        print("|", end="")
        for x in range(max_x):
            # Find object at current cell
            cell = next((cell for cell in grid if cell.x == x and cell.y == y), None)
            if cell:
                # Print symbol based on object
                print(cell.sym, end="")
            else:
                # Print empty space for empty cell
                print(" ", end="")
        # Print right border
        print("|")

    # Print bottom border
    print("+" + "-" * (max_x) + "+")