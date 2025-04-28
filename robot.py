import mesa

from obstacle import Obstacle

class Robot(mesa.Agent):
    """A Robot Agent"""

    def __init__(self, model):
        # Pass the parameters to the parent class.
        super().__init__(model)

        # Create the agent's variable and set the initial values.
        self.is_climbing = False
        self.climb_progress = 0
        self.climb_direction = None  # 'up' or 'down'
        self.required_climb_steps = 3  # Steps needed to climb up
        self.required_descend_steps = 1  # Steps needed to climb down
        self.trajectory = [self.pos]  # Record the trajectory

    def _add_trajectory(self):
        # Update trajectory
        self.trajectory.append(self.pos)

    def _is_on_obstacle(self):
        """Check if the robot is on an obstacle"""
        for obstacle in self.model.obstacles:
            if self.pos in obstacle.occupied_cell:
                return obstacle
        return None

    def _get_possible_moves(self):
        """Get possible moves considering obstacles"""
        obstacle = self._is_on_obstacle()
        if obstacle:
            # If on obstacle, can only move along the obstacle's orientation
            return obstacle.get_next_cell(climb_direction=self.climb_direction)

        else:
            # Get all neighboring cells
            neighbors = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)

            return neighbors

    def move(self):
        # The agent's step will go here.
        obstacle = self._is_on_obstacle()

        if obstacle:
            if not self.is_climbing:
                # Start climbing
                self.is_climbing = True
                self.climb_progress = 0
                self.climb_direction = 'up'
                return
            
            if self.is_climbing:
                self.climb_progress += 1
                
                if self.climb_direction == 'up':
                    if self.climb_progress >= self.required_climb_steps:
                        # Move to next cell
                        possible_moves = self._get_possible_moves()
                        new_position = self.random.choice(possible_moves)
                        self.model.grid.move_agent(self, new_position)

                        self._add_trajectory()

                        # Reached top, start descending
                        self.climb_direction = 'down'
                        self.climb_progress = 0
                else:  # descending
                    if self.climb_progress >= self.required_descend_steps:
                        # Finished descending
                        self.is_climbing = False
                        self.climb_progress = 0

                        # Move to next cell
                        possible_moves = self._get_possible_moves()
                        new_position = self.random.choice(possible_moves)
                        self.model.grid.move_agent(self, new_position)

                        self._add_trajectory()

                        self.climb_direction = None

        else:
            # Normal movement
            possible_moves = self._get_possible_moves()
            new_position = self.random.choice(possible_moves)
            self.model.grid.move_agent(self, new_position)

            self._add_trajectory()
