def ft_statistics(*args, **kwargs):
    def mean(values):
        return sum(values) / len(values)

    def median(values):
        values = sorted(values)
        mid = len(values) // 2
        if len(values) % 2 == 0:
            return (values[mid - 1] + values[mid]) / 2
        else:
            return values[mid]

    def quartile(values):
        values = sorted(values)
        mid = len(values) // 2
        if len(values) % 2 == 0:
            left = values[:mid]
            right = values[mid:]
        else:
            left = values[:mid]
            right = values[mid + 1:]
        q1 = median(left) if left else values[0]
        q2 = median(right) if right else values[-1]
        return [q1, q2]

    def var(values):
        m = mean(values)
        return sum((val - m) ** 2 for val in values) / len(values)

    def std(values):
        return var(values) ** 0.5

    if not args or not all(isinstance(x, (int, float)) for x in args):
        for _ in kwargs:
            print("ERROR")
        return
    funcs = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
        }
    for val in kwargs.values():
        if val in funcs:
            print(f"{val} : {funcs[val](args)}")
