from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    '''
        Create a grid that will hold all of the tiles
        for a boggle game
    '''
    
    return {(row, col): choice(ascii_uppercase) for row in range(height)
        for col in range(width)
    }
    
def neighbors_of_position(coords):
    '''
        Get neighbors of a given position
    '''
    
    # This is the starting position (i.e. the "center tile")
    row = coords[0]
    col = coords[1]
    
    # Every center tile has 8 neighbors: its four sides + its four corners
    
    # Top neighbors (i.e. top left/right corners and top side)
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    # Left and right neighbors
    left = (row, col - 1)
    right = (row, col + 1)
    
    # Bottom neighbors (i.e. left/right bottom corners and bottom side)
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    # Now we just return a list of the position's neighbors
    return [
            top_left,
            top_center,
            top_right,
            left,
            right,
            bottom_left,
            bottom_center,
            bottom_right
        ]
    
def all_grid_neighbors(grid):
    '''
        Get all of the possible neighbors for each position in
        the grid
    '''
    neighbors = {}
    for position in grid:
        position_neighbors = neighbors_of_position(position)
        neighbors[position] = [p for p in position_neighbors if p in grid]
        
    return neighbors
    
    
def path_to_word(grid, path):
    '''
        Add all of the letters on the path to a string
    '''
    return ''.join([grid[p] for p in path])