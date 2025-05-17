def callLimit(limit: int):
    """factory decorator that limits the number of calls to a function"""
    count = 0

    def callLimiter(function):
        """decorator that limits the number of calls to a function"""
        def limit_function(*args: any, **kwds: any):
            """limits the number of calls to a function"""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return
            return function(*args, **kwds)
        return limit_function
    return callLimiter
