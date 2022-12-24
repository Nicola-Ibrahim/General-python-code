# Import libraries
from dataclasses import dataclass, field
import traceback
from typing import Self

@dataclass
class Point:
    x: float
    y: float

    def __le__(self, other: Self):
        return other.x <= self.x and other.y <= self.y

    def __ge__(self, other: Self):
        return other.x >= self.x and other.y >= self.y

    def __lt__(self, other: Self):
        return self.x < other.x or self.y < other.y

    def __gt__(self, other: Self):
        return self.x > other.x or self.y > other.y


@dataclass
class Line:
    """Line class consists of two endpoints
    """
    point1: Point
    point2: Point
    name: str = field(default=None)

    def __post_init__(self):
        if self.name is None:
            filename, line_number, function_name, text = traceback.extract_stack()[-3]
            self.name = text[:text.find('=')].strip()

    def __str__(self) -> str:
        return self.name

    

    @property
    def slop(self):
        """Find the slop of the line

        Returns:
            slop_value: the slop of the line
        """
        slop_value = (self.point1.y - self.point2.y) / \
            (self.point1.x - self.point2.x)
        return slop_value

    # The standard line equation is (Ax + By = C)
    @property
    def coef(self):
        """Find line's coefficient

        Returns:
            dict: line's coefficients
        """
        A = (self.point1.y - self.point2.y)
        B = (self.point2.x - self.point1.x)
        C = (self.point1.x*self.point2.y - self.point2.x*self.point1.y)

        coef_values = dict()
        coef_values['A'] = A
        coef_values['B'] = B
        coef_values['C'] = -C
        return coef_values


@dataclass
class Rectangle:
    """
    Class is responsible to identify a new rectangle with its
    data
    """
    lowest_point: Point
    highest_point: Point
    width: float = field(init=False)
    hight: float = field(init=False)
   

    def __post_init__(self):
        self.width = self.highest_point.x - self.lowest_point.x
        self.hight = self.highest_point.y - self.lowest_point.y

    def is_inner_boundary(self, point: Point):
        """Check if the point is inner or in the boundary of the rectangle

        Args:
            point (Point): the point to be checked

        Returns:
            bool: condition belongs to the checked point
        """
        # TODO: Change condition if applicable after debugging 
        # return  self.lowest_point <= point <= self.highest_point

        COND1 = self.lowest_point.x <= point.x <= self.highest_point.x
        COND2 = self.lowest_point.y <= point.y <= self.highest_point.y
        return COND1 == True and COND2 == True
    
    def is_outer(self, point: Point):
        """Check if the point is outer of the rectangle

        Args:
            point (Point): the points to be checked

        Returns:
            bool: condition belongs to the checked point
        """
        
        # TODO: Change condition if applicable after debugging 
        # return point < self.lowest_point or point > self.highest_point

        COND1 = point.x < self.lowest_point.x or point.x > self.highest_point.x
        COND2 = point.y < self.lowest_point.y or point.y > self.highest_point.y
        return COND1 == True and COND2 == True
        
    
    @property
    def lines(self):
        """Returns the rectangle lines

        Returns:
            tuple: rectangle's lines
        """
        width = self.width
        hight = self.hight
        rec_left_line = Line(self.lowest_point, Point(
            self.lowest_point.x, self.lowest_point.y + hight))
        rec_bottom_line = Line(self.lowest_point, Point(
            self.lowest_point.x + width, self.lowest_point.y))
        rec_right_line = Line(self.highest_point, Point(
            self.highest_point.x, self.highest_point.y - hight))
        rec_top_line = Line(self.highest_point, Point(
            self.highest_point.x - width, self.highest_point.y))

        return (rec_left_line, rec_bottom_line, rec_right_line, rec_top_line)




