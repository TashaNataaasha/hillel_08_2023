def foo(n: int) -> None:
    print(f"{n=}")
    if n < 10:
        print("n < 10")
    else:
        print("n > 10")
        
foo(12)