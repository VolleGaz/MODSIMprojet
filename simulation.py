import numpy as np
import scipy.integrate as spi
from physics import *


def run_simulation(initial_conditions):
    """
    Runs the simulation for the ball using the provided initial conditions.
    """
    solution = spi.solve_ivp(equations, [0, TIME_MAX], initial_conditions, t_eval=np.linspace(0, TIME_MAX, 1000))
    x_values = solution.y[0]
    y_values = solution.y[1]
    return solution, x_values, y_values

def get_multiple_trajectories():
    """
    Generates multiple trajectories with different horizontal velocities.
    """
    trajectories = []
    for vx0 in np.linspace(-5, 5, 10):  # Different initial horizontal velocities
        vy0 = 0  # Fixed initial vertical velocity
        initial_conditions = [X0, Y0, vx0, vy0]
        solution, x_values, y_values = run_simulation(initial_conditions)

        # Check if the trajectory passes through the plate hole and lands in the ground hole
        if check_plate_collision(x_values, y_values) and check_ground_hole_collision(x_values, y_values):
            color = 'green'  # Trajectory passes through the hole
        else:
            color = 'red'  # Trajectory fails

        trajectories.append((x_values, y_values, color))

    return trajectories
