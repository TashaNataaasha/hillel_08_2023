def foo():
    print("Hello, I am foo")
    
def bar(name: str):
    function.__call__()
    # print(f"Hello, {name}")
    
def baz():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
gen = baz()
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))