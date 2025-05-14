class calculator:
    def __init__(self, lst):
        self.lst = lst

    def __add__(self, object) -> None:
        for i in range(len(self.lst)):
            self.lst[i] += object
        print(self.lst)
        return

    def __mul__(self, object) -> None:
        for i in range(len(self.lst)):
            self.lst[i] *= object
        print(self.lst)
        return

    def __sub__(self, object) -> None:
        for i in range(len(self.lst)):
            self.lst[i] -= object
        print(self.lst)
        return

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error division by 0 impossible")
            return
        for i in range(len(self.lst)):
            self.lst[i] /= object
        print(self.lst)
        return
