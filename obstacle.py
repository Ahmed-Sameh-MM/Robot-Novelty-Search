import mesa

class Obstacle(mesa.Agent):
    """A Hill Obstacle"""
    def __init__(self, model, position, orientation, is_first_cell=True):
        super().__init__(model)
        self.position = position
        self.orientation = orientation  # 'horizontal' or 'vertical'
        self.is_first_cell = is_first_cell  # True for first cell, False for second cell
        self.occupied_cell = self._get_occupied_cell()

    def _get_occupied_cell(self):
        """Get the occupied cell by this obstacle"""
        return [(self.position[0], self.position[1])]

    def get_next_cell(self, climb_direction: str):
        position = self.position

        if climb_direction == 'up':
            if self.orientation == 'horizontal':
                if self.is_first_cell:
                    return [(position[0] + 1, position[1])]
                else:
                    return [(position[0] - 1, position[1])]

            else:  # vertical
                if self.is_first_cell:
                    return [(position[0], position[1] + 1)]
                else:
                    return [(position[0], position[1] - 1)]

        elif climb_direction == 'down':
            if self.orientation == 'horizontal':
                if self.is_first_cell:
                    return [(position[0] - 1, position[1])]
                else:
                    return [(position[0] + 1, position[1])]

            else:  # vertical
                if self.is_first_cell:
                    return [(position[0], position[1] - 1)]
                else:
                    return [(position[0], position[1] + 1)]

    # This agent is static (No movement)
    def move(self):
        pass
