def foo(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    from functools import partial

    foo_curried = partial(foo, b=1)
    print(foo_curried(2))
    print(foo(1, 2))