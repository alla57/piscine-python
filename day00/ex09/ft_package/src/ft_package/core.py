def count_in_list(lst, item) -> int:
    """Count the number of occurrences of an item in a list.

    Parameters:
        lst (list): The list in which to count occurrences.
        item (any): The item to count.

    Returns:
        int: The number of times `item` appears in `lst`.

    Example:
        >>> count_in_list(["toto", "tata", "toto"], "toto")
        2
        >>> count_in_list(["toto", "tata", "toto"], "tutu")
        0
    """
    return lst.count(item)
