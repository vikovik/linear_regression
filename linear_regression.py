# Creating three lists: `possible_ms`, `possible_bs`, and `datapoints`.
possible_ms = [m * 0.1 for m in range(-10, 11)]
possible_bs = [b * 0.1 for b in range(-20, 21)]
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

"""
    The function calculates the value of y given the slope (m), y-intercept (b), and x-coordinate.
    
    :param m: The slope of the line. It represents how steep the line is
    :param b: The parameter "b" represents the y-intercept of a linear equation. It is the value of y
    when x is equal to 0
    :param x: The x parameter represents the input value for which we want to calculate the
    corresponding y value
    :return: the value of y, which is calculated using the formula y = m * x + b.
"""
def get_y(m, b, x):
    if not isinstance(m, (int, float)) or not isinstance(b, (int, float)) or not isinstance(x, (int, float)):
        raise ValueError("Parameters m, b, and x must be numbers.")
    
    y = m * x + b
    return y

"""
    The function calculates the difference between the predicted y-value and the actual y-value for a
    given point on a line.
    
    :param m: The slope of the line
    :param b: The parameter "b" represents the y-intercept of a linear equation
    :param point: A tuple containing the x and y coordinates of a point on a graph
    :return: the difference between the predicted y-value (calculated using the given slope (m),
    y-intercept (b), and x-value (x_point)) and the actual y-value (y_point).
"""
def calculate_error(m, b, point):
    if not isinstance(m, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Parameters m and b must be numbers")
    
    if not isinstance(point, tuple) or len(point) != 2:
        raise ValueError("Parameter point should be a tuple with two values (x, y)")
    
    x_point, y_point = point
    y = get_y(m, b, x_point)
    difference = abs(y - y_point)

    return difference

"""
    The function calculates the total error for a given set of points using a linear equation defined by
    the slope (m) and y-intercept (b).
    
    :param m: The slope of the line in the equation y = mx + b
    :param b: The parameter "b" represents the y-intercept of a linear equation
    :param points: A list of points, where each point is represented as a tuple (x, y)
    :return: the total error, which is the sum of the errors calculated for each point in the given list
    of points.
"""
def calculate_all_error(m, b, points):
    if not isinstance(m, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Parameters m and b must be numbers")
    
    if not isinstance(points, list):
        raise ValueError("Parameter points should be a list of tuples")
    
    total_error = 0

    for point in points:

        if not isinstance(point, tuple) or len(point) != 2:
            raise ValueError("Each point in the list should be a tuple with two values (x, y)")
        
        total_error += calculate_error(m, b, point)

    return int(total_error)

"""
    The function `find_smallest_error` finds the values of `m` and `b` that minimize the error when
    fitting a line to a set of datapoints.
    
    :param possible_ms: A list of possible values for the slope (m) of the linear equation
    :param possible_bs: The parameter `possible_bs` is a list of possible values for the variable `b`.
    It represents the different intercept values that will be tested in order to find the best fit line
    for the given data points
    :param datapoints: The `datapoints` parameter is a list of tuples, where each tuple represents a
    data point. Each tuple contains two values: the x-coordinate and the y-coordinate of the data point
    :param custom_ms: A list of custom values for the slope (m) of the linear equation
    :param custom_bs: A list of custom values for the y-intercept (b) of the linear equation
    :return: a tuple containing the slope and y-intercept that minimize the error for the given set of data points
"""

def find_smallest_error(possible_ms, possible_bs, datapoints, custom_ms=None, custom_bs=None):
    if not all(isinstance(param, list) for param in [possible_ms, possible_bs, datapoints, custom_ms, custom_bs]) and custom_ms is not None and custom_bs is not None:
        raise ValueError("All parameters should be lists")
    
    custom_ms = custom_ms or possible_ms
    custom_bs = custom_bs or possible_bs

    valid_custom_ms = all(isinstance(m, (int, float)) for m in custom_ms)
    valid_custom_bs = all(isinstance(b, (int, float)) for b in custom_bs)

    if not (valid_custom_ms and valid_custom_bs):
        raise ValueError("Custom slope and intercept values should be numbers")

    smallest_error = float("inf")
    best_m, best_b = 0, 0

    for m in custom_ms:
        for b in custom_bs:
            error = calculate_all_error(m, b, datapoints)

            if error < smallest_error:
                best_m, best_b, smallest_error = m, b, error

    return best_m, best_b, smallest_error

