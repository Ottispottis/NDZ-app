from droneinfo import x_coordinate, y_coordinate
from math import sqrt


def calculate_position():

    origin = 250000
    coordinate_list = []
    x = x_coordinate()
    y = y_coordinate()

    for i in range(len(x)):
        try:
            coordinate = sqrt((float(x[i])-origin)**2 + (float(y[i])-origin)**2)
            coordinate_list.append(coordinate)
        except IndexError:
            return None

    return coordinate_list

