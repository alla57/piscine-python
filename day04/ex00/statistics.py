def ft_statistics(*args: any, **kwargs: any) -> None:
    stat_keys = ["mean", "median", "quartile"]
    all(key in kwargs.items() for key in stat_keys)
    if "mean" in kwargs.items() and "median" in kwargs.items() and "quartile" in kwargs.items():
    for key, value in kwargs.items():
        kwargs[key] = value