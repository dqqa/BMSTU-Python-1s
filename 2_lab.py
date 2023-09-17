import math


class Vector2D:
    def __init__(self, start: "Point2D", end: "Point2D") -> None:
        self.start = start
        self.end = end

    def length(self):
        return (
            (self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2
        ) ** 0.5

    def __sub__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            raise NotImplemented

        new_start = Point2D(self.start.x - other.start.x, self.start.y - other.start.y)
        new_end = Point2D(self.end.x - other.end.x, self.end.y - other.end.y)
        return Vector2D(new_start, new_end)

    def angle(self, other):
        if not isinstance(other, Vector2D):
            raise NotImplemented
        diff = self - other
        print(diff)
        return math.atan2(diff.start.x-diff.end.x, diff.start.y-diff.end.y)

    def __repr__(self) -> str:
        return f"Vector2D({self.start}, {self.end})"


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def length(self, other: "Point2D") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"


class Triangle:
    def __init__(self, a: Point2D, b: Point2D, c: Point2D) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.area = self.__area()

    def determine_type(self):
        pass

    def __area(self) -> float:
        # a1,b1,c1 =
        angle_cos = (self.a.x * self.b.x + self.a.y * self.b.y) / (
            (self.a.x**2 + self.a.y**2) ** 0.5
            * (self.b.x**2 + self.b.y**2) ** 0.5
        )
        angle_sin = (1 - angle_cos**2) ** 0.5
        a = self.a.length(self.b)

        return

    def is_point_inside(point: Point2D):
        pass


vec2d1 = Vector2D(Point2D(0, 10), Point2D(10, 0))
vec2d2 = Vector2D(Point2D(0, 0), Point2D(0, 10))
print(vec2d1)
print(vec2d1.length())
print(vec2d1.angle(vec2d2))

# pts = [Point2D(*map(int, input().split())) for _ in range(3)]
# tr = Triangle(*pts)
# print(tr.area)
