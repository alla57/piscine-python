def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limt_function(*args: any, **kwds: any):
            pass