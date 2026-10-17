
import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]

        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()

        if length == 0:
            raise ValueError("Cannot normalize a zero vector")

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, vector):
        dot_product = self.x * vector.x + self.y * vector.y
        lengths = self.get_length() * vector.get_length()

        if lengths == 0:
            raise ValueError("Cannot calculate angle with a zero vector")

        cos_a = dot_product / lengths
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        x = self.x * cos_a - self.y * sin_a
        y = self.x * sin_a + self.y * cos_a

        return Vector(x, y)

