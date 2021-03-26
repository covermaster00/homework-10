from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, title, size):
        self.title = title
        self.size = size

    def __str__(self):
        return f'{self.title}, размерность {self.size}'

    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def tissue_consumption(self):
        return round(self.size * 2 + 0.3, 2)


cl1 = Coat('Вечернее платье', 32)
print(cl1)
print(cl1.tissue_consumption)

cl2 = Costume('Элегантные брюки', 152)
print(cl2)
print(cl2.tissue_consumption)
