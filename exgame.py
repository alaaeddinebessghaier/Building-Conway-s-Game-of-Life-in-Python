from game import GameOfLife
game = GameOfLife(30,30)

# Check dimensions of life_grid
assert len(game.life_grid) == 30  # Check number of rows
assert all(len(row) == 30 for row in game.life_grid)  # Check number of columns in each row

# Check that life_grid is filled with zeros
assert all(cell == 0 for row in game.life_grid for cell in row)

#game.print_grid()
game.populate_grid([(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)])
#help(game.populate_grid)
game.make_step()
game.make_n_steps(2)
game.draw_grid()

help(game.populate_grid)
help(game.make_step)
help(game.make_n_steps)
help(game.draw_grid)
help(game.get_grid)
help(game.print_grid)



