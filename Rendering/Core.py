import math

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
    def scaler(n):
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
