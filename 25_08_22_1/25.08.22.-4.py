class Descriptor_Tre:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) not in (int, float):
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, method_name):
        self.name = "_" + method_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Triangle:
    a = Descriptor_Tre()
    b = Descriptor_Tre()
    c = Descriptor_Tre()

    def __new__(cls, *args, **kwargs):
        if not all(type(arg) in (int, float) for arg in args):
            raise TypeError("Координата должна быть целым числом")
        if not all(arg > 0 for arg in args):
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        return super().__new__(cls)

    def __init__(self, a, b, c):
        if a < (b + c) and b < (a + c) and c < (a + b):
            self.a, self.b, self.c = a, b, c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __setattr__(self, name, value):
        # print("__setattr__")
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

        object.__setattr__(self, name, value)
        # print(value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self)*0.5
        s = (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
        return s

tr1 = Triangle(20, 20, 30)
print(len(tr1))

print("call", tr1())

tr1.x = 400
print("len = ", len(tr1))

