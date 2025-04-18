def give_bmi(height: list[int | float], \
weight: list[int | float]) -> list[int | float]:
    try:
        if height is None or weight is None:
            raise AssertionError("One of your list is a None.")
        if len(height) != len(weight):
            raise AssertionError("Height and weight must be the same length.")


        bmi = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)):
                raise AssertionError("Your list contains wrong type values. \
                Please use float or int only")
            if not isinstance(w, (int, float)):
                raise AssertionError("Your list contains wrong type values. \
                Please use float or int only")
            height_sq = h * h
            bmi.append(w / height_sq)
        return bmi

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
        return []
    except Exception as e:
        print("Something went wrong and exception has been raised:", e)
        return []

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if bmi is None or limit is None:
            raise AssertionError("Error bmi or limit is a None.")
        if not isinstance(limit, int):
            raise AssertionError("Error limit should be an int.")
        res = []
        for item in bmi:
            if not isinstance(item, (float, int)):
                raise AssertionError("Your list contains wrong type values. \
                Please use float or int only")
            if item > limit:
                res.append(True)
            else:
                res.append(False)
        return res

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
        return []
    except Exception as e:
        print("Something went wrong and exception has been raised:", e)
        return []
