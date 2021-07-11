from typing import List, Tuple

def has_vertical_symentric_line(coordinates: List[Tuple[int, int]]) -> str:
    """ Check if the coordinates contain a verticle symentrical line """
  
    min_x, max_x = min(coordinates)[0], max(coordinates)[0]
    x_middle = (min_x + max_x) / 2   

    left_coordinates_list = []
    right_coordinates_list = []
    symentric_pairs = 0

    for i in coordinates:   
        if i[0] == x_middle:
            continue
        if i[0] < x_middle:
            left_coordinates_list.append(i)
        if i[0] > x_middle:
            right_coordinates_list.append(i)    

    if len(left_coordinates_list) != len(right_coordinates_list):
        return 'No'

    for x, y in zip(left_coordinates_list, right_coordinates_list):
        if y[1] == x[1] and y[0] - x_middle == x_middle - x[0]:
            symentric_pairs += 1    

    return "Yes" if symentric_pairs == len(left_coordinates_list) and symentric_pairs == len(right_coordinates_list) else "No"


# print(has_vertical_symentric_line([(-2, 5), (2, 5), (4, 3), (-4, 3)]))
