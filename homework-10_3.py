class Cage:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cage(self.cell + other.cell)

    def __sub__(self, other):
        if other.cell < self.cell:
            return Cage(self.cell - other.cell)
        else:
            raise ValueError('Операция с отрицательным результатом')

    def __mul__(self, other):
        return Cage(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cage(self.cell // other.cell)

    def __truediv__(self, other):
        return Cage(self.cell / other.cell)

    def make_order(self, line_size):
        _ = '*' * self.cell
        return _.replace('*' * line_size, '*' * line_size + '\n')

c1 = Cage(13)
print('c1 = ', c1)
c2 = Cage(15)
print('c2 = ', c2)
print('c1 + c2 = ', c1 + c2)
print('c2 - c1 = ', c2 - c1)
#print(c1 - c2)
print('c1 * c2 = ', c1 * c2)
print('c2 // c1 = ', c2 // c1)
print('c2 / c1 = ', c2 / c1)
print(c1.make_order(5))
print(c2.make_order(4))
