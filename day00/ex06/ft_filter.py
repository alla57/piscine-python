def ft_filter(func, iterable):
    """ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function
    (item) is true. If function is None, return the items that are true.
    """
    if func:
        return (x for x in iterable if func(x))
    return (x for x in iterable if x)
