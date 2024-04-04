import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

class GameOfLife(object):  
    '''
        The GameOfLife class implements the famous "Conway's Game of Life".
    
        The game is a zero-player game, meaning that its evolution is determined by its initial state,
        requiring no further input. One interacts with the Game of Life by creating an initial 
        configuration and observing how it evolves.
    '''
    def __init__(self, x_dim, y_dim):
        '''
        Initializes a new instance of the GameOfLife class with a grid of given dimensions.
        
        Parameters:
        x_dim: The number of rows in the grid.
        y_dim: The number of columns in the grid.
        '''
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.life_grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]
   
        
    
    def get_grid(self):
        '''
        Gets the current state of the life grid.

        Returns:
        The current state of the life grid.
        '''
        return self.life_grid

    def print_grid(self):
        '''
        Prints the current state of the life grid in a readable format.
        '''
        # Implement a method to print out your grid in a human-readable format.
        for i in range(len(self.life_grid)):
            for j in range(len(self.life_grid[i])):
                
                print(self.life_grid[i][j],end=' | ')    
                
            print()
            print('_ '*(len(self.life_grid[i]) * 2))
               
            

    def populate_grid(self, coord):
        '''
        Populates the game grid with live cells at the specified coordinates.
    
        Parameters:
        coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.

        Returns:
        The updated life_grid with the new live cells.
    '''
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for x, y in coord:
                self.life_grid[x][y] = 1

                

    
    
    # No need to return self.life_grid here
    def make_step(self):
        '''
        Advances the game by one step according to the rules of the Game of Life.
        
        Returns:
        The updated life_grid after one step.
        '''
    # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        sum_grid = [[0 for _ in range(len(self.life_grid[0]))] for _ in range(len(self.life_grid))]

    # Create a new grid to store the next state
        new_life_grid = [[0 for _ in range(len(self.life_grid[0]))] for _ in range(len(self.life_grid))]

    # Loop through each cell
        for i in range(len(self.life_grid)):
            for j in range(len(self.life_grid[i])):
                sum_neighbors = 0
            # Loop through its neighbors
                for a in range(max(0, i - 1), min(len(self.life_grid), i + 2)):
                    for b in range(max(0, j - 1), min(len(self.life_grid[0]), j + 2)):
                        if a == i and b == j:
                            continue  # Skip the current cell
                    # Calculate the sum
                        sum_neighbors += self.life_grid[a][b]

            # Store the sum in the corresponding cell in sum_grid
                sum_grid[i][j] = sum_neighbors

            # Update the new grid based on the Game of Life rules
                if self.life_grid[i][j] == 1:
                    if sum_grid[i][j] < 2 or sum_grid[i][j] > 3:
                        new_life_grid[i][j] = 0
                    else:
                        new_life_grid[i][j] = 1
                else:
                    if sum_grid[i][j] == 3:
                        new_life_grid[i][j] = 1

    # Update the current life_grid with the new state
        self.life_grid = new_life_grid

        return self.life_grid

    def make_n_steps(self, n):
        '''
        Advances the game by a specified number of steps.

        Parameters:
        n: The number of steps to advance the game by.

        Returns:
        The updated life_grid after n steps.
        '''
        # Implement a method that applies the make_step method n times.
        for i in range(n):
             self.make_step()
        return self.life_grid

    #def draw_grid(self):
        # Draw the current state of the grid.
        x = [] 
        y = []
        for i in range(len(self.life_grid)):
            for j in range(len(self.life_grid[i])):
                x.append(i)
                y.append(j)

        fig, ax = plt.subplots(figsize=(20/2.54, 20/2.54))
        plt.scatter(x, y)
        custom_cmap = ListedColormap(['m', 'y'])

        ax.scatter(x, y, c=[self.life_grid[i][j] for j in range(len(self.life_grid[0])) for i in range(len(self.life_grid))], cmap=custom_cmap, s=1000)
        ax.set_xlim([-0.5, len(self.life_grid)-0.5])
        ax.set_ylim([-0.5, len(self.life_grid[0])-0.5])
        ax.invert_yaxis()
    
        # Remove axis labels
        ax.axis('off')
    
        # Show the plot
        plt.show()
        
    def draw_grid(self):
        '''
        Visualizes the current state of the game grid using a scatter plot.

        This method generates x and y coordinates for each cell in the grid and 
        creates a scatter plot using matplotlib. Each cell is represented as a point
        in the plot. The color of the point indicates the state of the cell
        (alive or dead). The grid is displayed with inverted y-axis to match the 
        console output of the game.

        Returns:
        None
        '''
        # Draw the current state of the grid.
        fig, ax = plt.subplots(figsize=(20/2.54, 20/2.54))
        custom_cmap = ListedColormap(['m', 'y'])

        for i in range(len(self.life_grid)):
            for j in range(len(self.life_grid[i])):
                color = 'm' if self.life_grid[i][j] == 0 else 'y'
                rect = Rectangle((i-0.5, j-0.5), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
                ax.add_patch(rect)

        ax.set_xlim([-0.5, len(self.life_grid)-0.5])
        ax.set_ylim([-0.5, len(self.life_grid[0])-0.5])
        ax.invert_yaxis()

        # Remove axis labels
        ax.axis('off')

        # Show the plot
        plt.show()



