from typing import Optional
from data import cumulative_label, price_label
from models import Coordinates, Lines


def get_point_by_row(row, translation_1: Optional[float] = 0.0, translation_2: Optional[float] = 0.0) -> Coordinates:
    return [row[cumulative_label] + translation_1, row[price_label] + translation_2] # (x,y) coordinates

def get_line_equation(point_1: Coordinates, point_2: Coordinates) -> Lines:
    diff = point_1[0] - point_2[0] 
    if diff == 0:
        return [point_1[0], 0, 0]
    slope = (point_1[1] - point_2[1]) / diff
    return [-1 * slope, 1, slope * point_1[0] - point_1[1]] # (a,b,c)(x, y, 1) => ax + by + c = 0

def get_determinant(line_1: Coordinates, line_2: Coordinates) -> float:
    return line_1[0] * line_2[1] - line_2[0] * line_1[1] 

def get_pairs(array: Coordinates, position_1: Optional[int] = 0, position_2: Optional[int] = 1, scale_1: Optional[float] = 1.0, scale_2: Optional[float] = 1.0) -> Coordinates:
    return [scale_1 * array[position_1], scale_2 * array[position_2]]

def get_intersection_lines(line_1: Lines, line_2: Lines) -> Coordinates:
    determinant = get_determinant(get_pairs(line_1), get_pairs(line_2))
    if determinant == 0:
        return "Not exist price"
    numerator_x = get_determinant(get_pairs(line_1, 2, 1, -1), get_pairs(line_2, 2, 1, -1))
    numerator_y = get_determinant(get_pairs(line_1, 0, 2, 1, -1), get_pairs(line_2, 0, 2, 1, -1))
    #print("numerator_x", numerator_x, get_pairs(line_1, 2, 1, -1), line_1)
    x = line_1[0] if numerator_x == 0 else numerator_x / determinant
    y = line_2[1] if numerator_y == 0 else  numerator_y / determinant 
    return [x, y]

