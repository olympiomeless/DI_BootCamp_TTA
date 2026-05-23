class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius} has an area of {self.area():.2f}"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.area() > other.area()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.area() == other.area()
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.area() < other.area()
        return NotImplemented
    

circle1 = Circle(5)
circle2 = Circle(3)
circle1.__add__(circle2)  # Circle with radius 8 has an area of 201.06
circle1.__gt__(circle2)  # True
circle1.__eq__(circle2)  # False
circle1.__lt__(circle2)  # False
