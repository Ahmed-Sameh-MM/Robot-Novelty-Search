import mesa

class Obstacle(mesa.Agent):
    """A Hill Obstacle"""
    def __init__(self, model, pos, orientation, is_first_cell=True):
        super().__init__(model)
        self.pos = pos
        self.orientation = orientation  # 'horizontal' or 'vertical'
        self.is_first_cell = is_first_cell  # True for first cell, False for second cell
        self.height = 2  # Takes 2 cells
        self.occupied_cells = self._get_occupied_cells()

    def _get_occupied_cells(self):
        """Get all cells occupied by this obstacle"""
        if self.orientation == 'horizontal':
            if self.is_first_cell:
                return [(self.pos[0], self.pos[1])]
            else:
                return [(self.pos[0] + 1, self.pos[1])]
        else:  # vertical
            if self.is_first_cell:
                return [(self.pos[0], self.pos[1])]
            else:
                return [(self.pos[0], self.pos[1] + 1)]

    # This agent is static (No movement)
    def move(self):
        pass
