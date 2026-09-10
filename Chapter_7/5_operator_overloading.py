# Operator overloading:

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y;

    def sum(self, p):
        return Point((self.x +p.x), (self.y+p.y));

    def print_point(self):
        return f"X: {self.x}, Y: {self.y}";

    def __add__(self, p):
        return Point((self.x +p.x), (self.y+p.y));


p1 = Point(3,2);
p2 = Point(4,7);

p = p1.sum(p2); #returns a new point which is sum of p1 and p2.
print(p.print_point());

# can we do something like p1 + p2
# z = p1 +p2; #type error

p_ = p1 + p2; #operator overloading
print(p_.print_point());