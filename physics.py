from constants import *


def equations(t, z):
    """
    Defines the differential equations for the motion of the ball.
    z = [x, y, vx, vy] represents position and velocity.
    """
    x, y, vx, vy = z
    ax = 0  # Horizontal acceleration is zero
    ay = -GRAVITY  # Vertical acceleration by default (gravity)

    """
    attempt to make the ball bounce off the plate
    # Check if the ball hits the plate and bounce if necessary
    if (PLATE_X - RADIUS <= x <= PLATE_X + RADIUS) and check_plate_collision([x],[y]) and vy < 0:
        # Reverse and reduce the vertical velocity
        vy = -COEFFICIENT_OF_RESTITUTION * vy
        # Adjust position to prevent continuous collision detection
        y = PLATE_Y + RADIUS + 1e-5

        # Acceleration due to spring force from plate deformation
        ay = -GRAVITY - SPRING_CONSTANT * (y - PLATE_Y) / MASS - DRAG_COEFFICIENT * vy / MASS
    """

    if y > RADIUS:  # Free fall
        ay = -GRAVITY  # Gravitational acceleration (before hitting the plate)

    else:  # Bounce phase (on the ground or after a plate bounce)
        ay = -GRAVITY - SPRING_CONSTANT * (y - RADIUS) / MASS - DRAG_COEFFICIENT * vy / MASS

    return [vx, vy, ax, ay]


def check_plate_collision(x_values, y_values):
    """
    Checks if the ball passes through the plate's hole.
    """
    for x, y in zip(x_values, y_values):
        if PLATE_X - RADIUS <= x <= PLATE_X + RADIUS:
            distance_to_center = abs(y - PLATE_Y)
            if distance_to_center <= PLATE_RADIUS:
                return True  # Ball passes through the hole
    return False


def check_ground_hole_collision(x_values, y_values):
    """
    Checks if the ball lands in the ground's hole.
    """
    for x, y in zip(x_values, y_values):
        # Check if the ball is within the horizontal range of the hole in the ground
        if HOLE_X - HOLE_RADIUS <= x <= HOLE_X + HOLE_RADIUS:
            # Check if the ball touches the ground within the hole range
            if y <= RADIUS:  # Ground is at y = 0, so y <= radius means touching the ground
                return True  # Ball lands in the hole
    return False
