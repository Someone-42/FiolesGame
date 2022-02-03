import math
from enum import Enum

def clamp(value, min_value, max_value):
    """ Returns 'value' between 'min_value' and 'max_value'"""
    return min(max(min_value, value), max_value)

class Vector2:
    """Representation of a 2D vector"""
    __slots__=("x", "y")
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def magnitude(self):
        """Returns the length of the vector"""
        return math.sqrt((self.x*self.x) + (self.y*self.y))

    def squared_magnitude(self):
        """Returns the squared length of the vector, faster to compute"""
        return (self.x*self.x) + (self.y*self.y)

    def normalize(self):
        """Normalizes the vector to have its length equal to 1"""
        magn = self.magnitude()
        if magn == 0:
            magn = 1
        return Vector2(self.x / magn, self.y / magn)

    def __len__(self):
        return self.magnitude()

    def __abs__(self):
        return self.magnitude()
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self
    
    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __str__(self):
        """ Returns the Vector2 in a easier way to read string form """
        return "x:"+str(self.x)+", y:"+str(self.y)

    def copy(self):
        """ Returns a copy of itself """
        return Vector2(self.x, self.y)

    def rotate(self, angle_radians):
        """ Rotates vector using rotation matrices """
        return Vector2((math.cos(angle_radians) * self.x) - (self.y * math.sin(angle_radians)),
                       (math.sin(angle_radians) * self.x) + (self.y * math.cos(angle_radians)))

    def mul_comp(self, vector2):
        """ Multiplies each component of the vectors individually """
        return Vector2(self.x * vector2.x, self.y * vector2.y)
    
    def div_comp(self, vector2):
        """ Divides each component of the vectors individually """
        return Vector2(self.x / vector2.x, self.y / vector2.y)

    def min_comp(self):
        """ Returns the smallest component of the vector """
        return min(self.x, self.y)
    
    def max_comp(self):
        """ Returns the biggest component of the vector """
        return max(self.x, self.y)

    def flip_comp(self):
        """ Returns a flipped around version of the vector by switching its components """
        return Vector2(self.y, self.x)

    def sort_comp(self):
        """ Returns a new vector where x < y """
        return Vector2(self.min_comp(), self.max_comp())

    @staticmethod
    def scalar(n):
        """ Returns a vector with n as components : Vector2(n, n) """
        return Vector2(1, 1) * n

    def abs_comp(self):
        """ Returns a vector with the absolute value of each comp """
        return Vector2(abs(self.x), abs(self.y))

    def squared_distance(self, point):
        """ Returns the squared distance to point : faster method because no calculation of the sqrt is needed """
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2

    def distance(self, point):
        """ Returns the distance to point"""
        math.sqrt(self.squared_distance(point))

    def to_tuple(self):
        """ Returns the vector as a tuple """
        return (self.x, self.y)

class Color:
    """ Simple color struct with, r=Red g=Green b=Blue a=Alpha"""
    __slots__=("r", "g" ,"b", "a")
    def __init__(self, r=128, g=128, b=128, a=255):
        self.r = 1 * int(clamp(r, 0, 255))
        self.g = int(clamp(g, 0, 255))
        self.b = int(clamp(b, 0, 255))
        self.a = int(clamp(a, 0, 255))

    def clamp_to_rgba_uint8(self):
        """ Clamps all the value to unsigned int 8bits (from 0 to 255) """
        self = Color.sttc_clamp_to_rgba_uint8(self)

    @staticmethod
    def sttc_clamp_to_rgba_uint8(color):
        """ Returns a Color() object with all the values clamped to unsigned int 8bits (from 0 to 255) """
        return Color(color.r, color.g, color.b, color.a)

    def __mul__(self, other):
        col = self.copy()
        col.r *= other
        col.g *= other
        col.b *= other
        return Color.sttc_clamp_to_rgba_uint8(col)

    def copy(self):
        """ Returns a copy of itself """
        return Color(self.r, self.g, self.b, self.a)

    def to_tuple_rgb(self):
        return (self.r, self.g, self.b)

    def to_tuple_rgba(self):
        return (self.r, self.g, self.b, self.a)

class Primitive:
    """ Shape base for rendering """
    __slots__=("color")
    def __init__(self, color = Color()):
        self.color = color

    def is_point_inside(self, point: Vector2) -> bool:
        return False

class Rectangle2(Primitive):
    """ 2D Rectangle primitive """
    __slots__=("pos", "size")
    def __init__(self, position=Vector2(), size=Vector2(), color=Color()):
        super().__init__(color)
        self.pos = position
        self.size = size

    def get_points2(self):
        """ Returns the rectangle as a tuple of 2 vectors, 2 vectors being the points defining it """
        return (
            self.pos.copy(), 
            self.pos + self.size)

    def get_points4(self):
        """ Returns the rectangle as a tuple of 4 vectors, 4 vectors being the points defining it """
        return (
            self.pos.copy(), 
            self.pos + Vector2(self.size.x, 0), 
            self.pos + self.size,
            self.pos + Vector2(0, self.size.y))

    def is_point_inside(self, point: Vector2):
        p1, p2 = self.get_points2()
        min_x, max_x = (p1.x, p2.x) if p1.x < p2.x else (p2.x, p1.x)
        min_y, max_y = (p1.y, p2.y) if p1.y < p2.y else (p2.y, p1.y)
        return \
            point.x >= min_x and \
            point.x <= max_x and \
            point.y >= min_y and \
            point.y <= max_y

class Button:
    __slots__=("rect", "on_click")
    def __init__(self, rect, on_click = None):
        self.rect = rect
        if on_click is None:
            self.on_click = self.default_on_click
        else:
            self.on_click = on_click

    def is_click_on_button(self, click) -> bool:
        """ Returns true or false if the button was clicked """
        return rect.is_point_inside(click)

    def default_on_click():
        print("The button at", self.rect.pos, "of size", self.rect.size, "was clicked")

class InputType(Enum):
    GO_BACK = -1
    MOVE = 0
    QUIT = 1