import math


def add_it_up(first: int, second: int):
    return first + second


def find_distance(point1, point2):
    delta_x = point1[0]-point2[0]
    delta_y = point1[1]-point2[1]
    result = math.sqrt(delta_x*delta_x+delta_y*delta_y)
    return result