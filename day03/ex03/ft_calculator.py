import numpy as np


class calculator:
    def __init__(self, array):
        self.array = np.array(array)

    def __add__(self, object) -> None:
        self.array += object
        print(self.array.tolist())
        return

    def __mul__(self, object) -> None:
        self.array *= object
        print(self.array.tolist())
        return

    def __sub__(self, object) -> None:
        self.array -= object
        print(self.array.tolist())
        return

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error division by 0 impossible")
            return
        self.array /= object
        print(self.array.tolist())
        return
