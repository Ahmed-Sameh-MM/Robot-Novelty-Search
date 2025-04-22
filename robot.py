import mesa

class Robot(mesa.Agent):
    """A Robot Agent"""

    def __init__(self, model):
        # Pass the parameters to the parent class.
        super().__init__(model)

        # Create the agent's variable and set the initial values.
        self.wealth = 1

    def move(self):
        # The agent's step will go here.
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        old_pos = self.pos
        self.model.grid.move_agent(self, new_position)

        print(f"Old pos: {old_pos}, New pos: {self.pos}")
