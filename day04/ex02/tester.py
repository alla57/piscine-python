from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


try:
    for i in range(3):
        f()
        g()
except Exception as e:
    print(f"{type(e).__name__} : {e}")
