from mesa.visualization import SolaraViz, make_plot_component, make_space_component

# import seaborn as sns
import numpy as np
import pandas as pd

from model import RobotModel
from constants import *

def agent_portrayal(agent):
    return {
        "color": "tab:blue",
        "size": 50,
    }

model_params = {
    # "width": {
    #     "type": "SliderInt",
    #     "value": GRID_WIDTH,
    #     "label": "Grid Width:",
    #     "min": 5,
    #     "max": 100,
    #     "step": 1,
    # },
    # "length": {
    #     "type": "SliderInt",
    #     "value": GRID_LENGTH,
    #     "label": "Grid Length:",
    #     "min": 5,
    #     "max": 100,
    #     "step": 1,
    # },
    "width": GRID_WIDTH,
    "length": GRID_LENGTH
}

# Create initial model instance
robot_model = RobotModel(
    width=GRID_WIDTH,
    length=GRID_LENGTH,
) #keyword arguments

# for _ in range(NUM_STEPS):
#     robot_model.step()
#
# agent_wealth = robot_model.datacollector.get_agent_vars_dataframe()
# print(agent_wealth.head())

SpaceGraph = make_space_component(agent_portrayal)
# GiniPlot = make_plot_component("Gini")

page = SolaraViz(
    robot_model,
    components=[SpaceGraph],
    model_params=model_params,
    name="Robot Model",
)
