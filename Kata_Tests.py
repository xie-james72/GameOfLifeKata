import unittest
import numpy
import Game_Of_Life_Kata


class Kata_Tests(unittest.TestCase):
    def given_2_rows_and_2_columns_generate_a_grid_array(self):
        grid = Game_Of_Life_Kata.generate_array(2,2)
        self.assertEqual(grid, [[0,0],[0,0]])

    def given_n_rows_and_m_columns_generate_a_grid_array(self):
        n = 10
        m = 12
        grid = Game_Of_Life_Kata.generate_array(n, m)
        self.assertEqual(grid, np.zeros((n, m)))

    def test_if_index_is_out_of_bounds(self):
        grid = [[0,0],[0,0]]
        step_too_far_left = (-1,0)
        step_too_far_up = (0,-1)

        result = Game_Of_Life_Kata.check_valid(grid,index)

        self.assertEqual(result, False)

    def count_number_of_neighbors_around_a_zero_grid_cell(self):
        grid = [0]
        index = (0,0)
        number_of_neighbors = Game_Of_Life_Kata.neighbors(grid, index)
        self.assertEqual(number_of_neighbors, 0)

    def count_number_of_neighbors_around_a_corner_cell(self):
        grid = [[0,0],[0,0]]
        index = (0,0)
        number_of_neighbors = Game_Of_Life_Kata.neighbors(grid, index)
        self.assertEqual(number_of_neighbors, 3)

    #........

    def check_if_cell_is_dead(self):
        cell = Game_Of_Life_Kata.cell():
        self.assertEqual(cell.state, 0)

    def make_dead_cell_live(self):
        cell = Game_Of_Life_Kata.cell():
        cell.toggle_state
        self.assertEqual(cell.state, 1)



if __name__ == '__main__':
    unittest.main()
