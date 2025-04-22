import mesa

from constants import NUM_STEPS
from robot import Robot

class RobotModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, width, length, seed=1024):
        super().__init__(seed=seed)
        self.num_agents = 1
        self.grid = mesa.space.SingleGrid(width, length, False)
        self.datacollector = mesa.DataCollector(
            # model_reporters={"Gini": self._compute_gini},
            agent_reporters={"Position": "pos"}
        )
        self.running = True
        self.step_count = 0

        # Create agents
        agents = Robot.create_agents(model=self, n=self.num_agents)

        self.robot = agents[0]

        self.grid.place_agent(self.robot, (0, 0))

    def step(self):
        """Advance the model by one step."""

        # This function psuedo-randomly reorders the list of agent objects and
        # then iterates through calling the function passed in as the parameter
        self.step_count += 1
        if self.step_count > NUM_STEPS:
            self.running = False

        self.datacollector.collect(self)
        self.agents.shuffle_do("move")
