# picture-grid.py
# By Ben Bicakci
# Source: Automate the Boring Stuff with Python by Al Sweigart

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotate_grid_90(grid_input):

#Takes grid as input and rotate 90 degrees to right

        for col in range(len(grid_input[0])):
                for row in range(len(grid_input)):
                        new_index = grid_input[row][col]
                        print(new_index, end = ' ')
                print()


rotate_grid_90(grid)