# Ball parameters
MASS = 0.2  # Mass of the ball in kg
RADIUS = 0.05  # Radius of the ball in meters
GRAVITY = 9.81  # Gravitational acceleration in m/s²
DRAG_COEFFICIENT = 5  # Air drag coefficient
SPRING_CONSTANT = 5000  # Spring constant for vertical motion
COEFFICIENT_OF_RESTITUTION = 0.8 # Coefficient of restitution for elasticity

# Initial conditions
X0 = 10  # Initial x position (m)
Y0 = 10  # Initial y position (m)
VX0 = 3  # Initial horizontal velocity (m/s)
VY0 = 0  # Initial vertical velocity (m/s)
TIME_MAX = 10  # Maximum time for the simulation (seconds)

# Obstacle parameters
PLATE_X = 5  # x-position of the plate
PLATE_Y = 1.5  # y-position of the center of the hole in the plate
PLATE_RADIUS = 1  # Radius of the hole in the plate
HOLE_X = 4  # x-position of the hole in the ground
HOLE_RADIUS = 1  # Radius of the hole in the ground