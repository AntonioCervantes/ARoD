import math
def steering_correct(steering_angle):
    max_left = 50
    max_right = 130
    if steering_angle < 0: # Turn Right (Robot is on left side of line)
        steering_angle = 90 + math.fabs(steering_angle)
        if steering_angle > max_right:
            steering_angle = max_right
        else:
            steering_angle = steering_angle
    elif steering_angle > 0: # Turn left (Robot is on right side of line)
        steering_angle = 90 - math.fabs(steering_angle)
        if steering_angle < max_left:
            steering_angle = max_left
        else:
            steering_angle = steering_angle
    return steering_angle    
