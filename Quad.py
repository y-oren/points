
#Quadrilateral is a 4 sided polygon

#parallelogram opposite sides are parallel
#Rectangle all angles are right angles
#Rhombus all sides are congruent
#Square diagonals form 4 congreunt isosceles right angle triangles.
#Trapezoid

# All functions should return a boolean value. (True / False)

import Point, Angles

class Quad:
    A=Point.Point()
    B=Point.Point()
    C=Point.Point()
    D=Point.Point()

    def __init__(self, A=Point.Point(x=0, y=0), B=Point.Point(x=0, y=0), C=Point.Point(x=0, y=0), D=Point.Point(x=0, y=0)):
        self.A.x=A.x
        self.A.y=A.y

        self.B.x=B.x
        self.B.y=B.y

        self.C.x=C.x
        self.C.y=C.y

        self.D.x=D.x
        self.D.y=D.y

    def __str__(self):
        return f"{self.A},{self.B},{self.C},{self.D}"

    def Quad(self):
        # TODO: Check if it is a quadrilateral.

    def Parallelogram(self):
        # TODO: Check if it is a parallelogram.

    def Rect(self):
        # TODO: Check if it is a rectangle.

    def Square(self):
        # TODO: Check if it is a square.

    def Trapezoid(self):
        # TODO: Check if it is a trapezoid.

    def isRhombus(self):
        # TODO: Check if it is a rhombus.
