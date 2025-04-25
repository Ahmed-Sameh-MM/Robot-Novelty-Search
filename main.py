from mesa.visualization import SolaraViz, make_plot_component, make_space_component

# import seaborn as sns
import numpy as np
import pandas as pd

from model import RobotModel
from robot import Robot
from obstacle import Obstacle
from constants import *

def agent_portrayal(agent):
    if isinstance(agent, Robot):
        color = "green"
    elif isinstance(agent, Obstacle):
        if agent.orientation == "horizontal":
            color = "blue"
        else:
            color = "yellow"
    else:
        color = "red"

    return {
        "color": color,
        "size": 50,
    }

model_params = {
    "width": GRID_WIDTH,
    "length": GRID_LENGTH
}

# Create initial model instance
robot_model = RobotModel(
    width=GRID_WIDTH,
    length=GRID_LENGTH,
) #keyword arguments

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
