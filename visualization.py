import matplotlib.pyplot as plt
from simulation import *

def plot_simulation_results():
    """
    Plots the results of the ball's motion over time and its trajectory.
    """
    initial_conditions = [X0, Y0, VX0, VY0]  # Example of initial velocity
    solution, x_values, y_values = run_simulation(initial_conditions)

    # Create a 2x2 grid of subplots
    plt.figure(figsize=(12, 10))

    # Position vs Time (x)
    plt.subplot(2, 2, 1)
    plt.plot(solution.t, solution.y[0], label='x(t)', color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Position x (m)')
    plt.title('Position x vs Time')
    plt.legend()
    plt.grid()

    # Position vs Time (y)
    plt.subplot(2, 2, 2)
    plt.plot(solution.t, solution.y[1], label='y(t)', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Position y (m)')
    plt.title('Position y vs Time')
    plt.legend()
    plt.grid()

    # Trajectory (y vs x)
    plt.subplot(2, 2, 3)
    plt.plot(solution.y[0], solution.y[1], label='y(x)', color='purple')
    plt.xlabel('Position x (m)')
    plt.ylabel('Position y (m)')
    plt.title('Trajectory y vs x')
    plt.legend()
    plt.grid()

    # Velocity vs Time (vx and vy)
    plt.subplot(2, 2, 4)
    plt.plot(solution.t, solution.y[2], label="v_x(t)", linestyle='--', color='green')
    plt.plot(solution.t, solution.y[3], label="v_y(t)", linestyle='--', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocities vs Time')
    plt.legend()
    plt.grid()

    # Multiple trajectories with obstacles
    plt.figure(figsize=(8, 6))

    # Draw the vertical plate line excluding the hole
    plate_top = PLATE_Y + PLATE_RADIUS
    plate_bottom = PLATE_Y - PLATE_RADIUS
    plt.plot([PLATE_X, PLATE_X], [0, plate_bottom], color="black", linewidth=2, label="Plate (No Hole)")  # Bottom part
    plt.plot([PLATE_X, PLATE_X], [plate_top, Y0 + 2], color="black", linewidth=2)  # Top part

    # Draw the horizontal ground line excluding the hole
    ground_left = HOLE_X - HOLE_RADIUS
    ground_right = HOLE_X + HOLE_RADIUS
    plt.plot([0, ground_left], [0, 0], color="black", linewidth=2, label="Ground (No Hole)")  # Left part
    plt.plot([ground_right, X0 + 2], [0, 0], color="black", linewidth=2)  # Right part

    

    # Plot multiple trajectories
    trajectories = get_multiple_trajectories()
    for x_values, y_values, color in trajectories:
        plt.plot(x_values, y_values, color=color, alpha=0.6)

    plt.xlabel("Position x (m)")
    plt.ylabel("Position y (m)")
    plt.title("Multiple Trajectories with Obstacles")
    plt.legend()
    plt.grid()
    plt.xlim(0, X0 + 2)
    plt.ylim(-1, Y0 + 2)
    plt.gca().set_aspect('equal', adjustable='box')

    # Show the plots
    plt.tight_layout()
    plt.show()
