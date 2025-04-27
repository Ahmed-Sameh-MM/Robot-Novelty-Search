import mesa
import random

from constants import *
from robot import Robot
from obstacle import Obstacle

class RobotModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, width, length, seed=1024):
        super().__init__(seed=seed)
        self.num_agents = 1
        self.grid = mesa.space.MultiGrid(width, length, False)
        self.datacollector = mesa.DataCollector(
            # model_reporters={"Gini": self._compute_gini},
            agent_reporters={"Position": "pos"}
        )
        self.running = True
        self.step_count = 0

        # Create and place obstacles
        self.obstacles = []
        self._place_obstacles()

        # Create agents
        agents = Robot.create_agents(model=self, n=self.num_agents)
        self.robot = agents[0]
        self.grid.place_agent(self.robot, (0, 0))

    def _place_obstacles(self):
        """Place obstacles in the grid"""
        # Place obstacles
        for _ in range(NUM_OBSTACLES):
            # Randomly choose orientation
            orientation = random.choice(['horizontal', 'vertical'])
            
            # Find a valid position for the obstacle
            while True:
                if orientation == 'horizontal':
                    x = random.randint(1, self.grid.width - 3)
                    y = random.randint(0, self.grid.height - 1)
                else:
                    x = random.randint(0, self.grid.width - 1)
                    y = random.randint(1, self.grid.height - 3)
                
                # Check if the position and adjacent cell are empty
                pos = (x, y)
                if orientation == 'horizontal':
                    next_pos = (x + 1, y)
                else:
                    next_pos = (x, y + 1)
                
                if (self.grid.is_cell_empty(pos) and 
                    self.grid.is_cell_empty(next_pos) and
                    pos != (0, 0) and next_pos != (0, 0)):  # Don't block start
                    break

            # Create and place both obstacle agents
            obstacle1 = Obstacle(self, pos, orientation, is_first_cell=True)
            obstacle2 = Obstacle(self, next_pos, orientation, is_first_cell=False)
            self.obstacles.extend([obstacle1, obstacle2])

            # Place both obstacle agents
            self.grid.place_agent(obstacle1, pos)
            self.grid.place_agent(obstacle2, next_pos)

    def step(self):
        """Advance the model by one step."""

        # This function psuedo-randomly reorders the list of agent objects and
        # then iterates through calling the function passed in as the parameter
        self.step_count += 1
        if self.step_count > NUM_STEPS:
            self.running = False
            return

        self.datacollector.collect(self)
        self.agents.shuffle_do("move")
