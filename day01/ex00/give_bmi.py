def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for each pair of height and weight.

    Args:
        height (list of int or float): A list of heights (in meters).
        weight (list of int or float): A list of weights (in kilograms).

    Returns:
        list of float: A list containing the BMI values calculated as
        weight / (height ** 2) for each corresponding pair of height and weight

    Error Handling:
        - If either input list is None,
        prints an error and returns an empty list.
        - If the input lists are not the same length,
        prints an error and returns an empty list.
        - If any element in the input lists is not an int or float,
        prints an error and returns an empty list.
        - Catches other exceptions, prints an error message,
        and returns an empty list.

    Example:
        >>> give_bmi([1.80, 1.75], [75, 67])
        [23.148148148148145, 21.877551020408163]
    """
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
    """
    Compares each BMI value in the list to a specified limit and
    returns a list of boolean values.

    Args:
        bmi (list of int or float): A list of BMI values to compare.
        limit (int): The threshold value to compare each BMI against.

    Returns:
        list of bool: A list where each element is True,
        if the corresponding BMI value is
        greater than the limit, and False otherwise.

    Error Handling:
        - If either bmi or limit is None,
        prints an error and returns an empty list.
        - If limit is not an integer,
        prints an error and returns an empty list.
        - If any value in bmi is not an int or float,
        prints an error and returns an empty list.
        - Catches any other exceptions, prints an error message,
        and returns an empty list.

    Example:
        >>> apply_limit([21.0, 25.5, 19.8], 22)
        [False, True, False]
    """
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
