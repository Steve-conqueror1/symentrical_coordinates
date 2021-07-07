from typing import List, Tuple


def get_max_and_min_value(coordinates: List[Tuple[int, int]], min: int, max: int, index: int):
    """ Get min and max of x or y coordinates"""
    for i in coordinates:
        if i[index] > max:
            max = i[index]
        elif i[index] <= min:
            min = i[index]
    return min, max


def has_vertical_symentric_line(coordinates: List[Tuple[int, int]]) -> str:
    """ Check if the coordinates contain a verticle line """
    min_x, max_x = get_max_and_min_value(
        coordinates, coordinates[0][0], coordinates[0][0], 0)
    x_middle = (min_x+max_x) / 2

    left_coordinates_dict = []
    right_coordinates_dict = []
    symentric_pairs = 0

    for i in coordinates:
        if i[0] == x_middle:
            continue
        if i[0] < x_middle:
            left_coordinates_dict.append(i)
        if i[0] > x_middle:
            right_coordinates_dict.append(i)
    if len(left_coordinates_dict) != len(right_coordinates_dict):
        return 'No'

    for left_point in left_coordinates_dict:
      for right_point in right_coordinates_dict:
        if right_point[1] == left_point[1] and right_point[0] - x_middle == x_middle - left_point[0]:
          symentric_pairs += 1         


    return "Yes" if symentric_pairs == len(left_coordinates_dict) else "No"


# print(has_vertical_symentric_line([(-2, 5), (2, 5), (4, 3), (-4, 3)]))
