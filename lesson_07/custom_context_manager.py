from contextlib import contextmanager


class MyContext:
    # def __enter__(self):
    #     print("Entering the context")
    #     return self

    # def __exit__(self, *args, **kwargs):
    #     print("Exiting")

    def foo(self):
        print("I am foo")


@contextmanager
def managed_resource(*args, **kwds):
    print("Inside init")
    try:
        yield "As value"
    finally:
        print("Exiting")


with managed_resource() as value:
    print(value)

# Useless
# with MyContext() as context:
#     context.foo()

# context = MyContext()
# context.foo()
# context.exit()  create the new one