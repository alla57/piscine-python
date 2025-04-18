def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (list of lists) from row index 'start' up to,
    but not including, 'end'.
    Prints the original shape and the new shape after slicing.

    Args:
        family (list of list): The 2D list to be sliced.
        All inner lists (rows) must have the same length.
        start (int): The index at which to start slicing (inclusive).
        end (int): The index at which to end slicing (exclusive).

    Returns:
        list: The sliced 2D list containing rows from
        index 'start' to 'end - 1'.

    Raises:
        AssertionError: If 'family' is not a list of lists,
        is empty, or has irregular row sizes.
        AssertionError: If 'start' or 'end' are not integers.

    Prints:
        The original shape and the new shape of the 2D list after slicing,
        formatted as (number of rows, number of columns).

    Example:
        >>> family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        >>> slice_me(family, 0, 2)
        My shape is : (4, 2)
        My new shape is : (2, 2)
        [[1.8, 78.4], [2.15, 102.7]]
    """
    try:
        if family is None or start is None or end is None:
            raise AssertionError("Error One or more of the \
            parameters is a None.")
        if not isinstance(family, list) \
                or not all(isinstance(row, list) for row in family):
            raise AssertionError("Error One of the family \
            members is not a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Error start or end is not an int")
        height = len(family)
        if height == 0:
            raise AssertionError("Error family is empty")
        width = len(family[0])
        for item in family:
            if len(item) != width:
                raise AssertionError("Error one of the family item length is \
                different from the others")
        print(f"My shape is : ({height}, {width})")
        new_fam = family[start:end]
        height = len(new_fam)
        if height > 0:
            width = len(new_fam[0])
        else:
            width = 0
        print(f"My new shape is : ({height}, {width})")
        return new_fam

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
        return []
    except Exception as e:
        print("Something went wrong and exception has been raised:", e)
        return []
