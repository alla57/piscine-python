class calculator:
    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        tmp = []
        res = 0
        for i in range(len(V1)):
            tmp.append(V1[i] * V2[i])
            res += tmp[i]
        print(f"Dot product is: {res}")
        return

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        tmp = []
        for i in range(len(V1)):
            tmp.append(float(V1[i]) + V2[i])
        print(f"Add Vector is : {tmp}")
        return

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        tmp = []
        for i in range(len(V1)):
            tmp.append(float(V1[i]) - V2[i])
        print(f"Sous Vector is: {tmp}")
        return
