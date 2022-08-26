class Dimensions:

    def __init__(self, a, b, c):
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float) \
                or a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a, self.b, self.c = a, b, c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


inpurt_list = input().split("; ")
lst_dims = []
for x in inpurt_list:
    x = x.split()
    arr = []
    for y in x:
        # if y not in "0123456789."
        if "." not in y:
            y = int(y)
            arr.append(y)
        else:
            y = float(y)
            arr.append(y)
    new_obj = Dimensions(*arr)
    lst_dims.append(new_obj)

lst_dims = sorted(lst_dims, key=lambda x: hash(x))


print(lst_dims)
for x in lst_dims:
    print(hash(x))


# "a1 b1 c1;a2 b2 c2; ... ;aN b
