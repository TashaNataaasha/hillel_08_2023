# MRO
class A:
     pass
 
class B(A):
    pass

class D(A, B):    # MRO error
    pass

print(D())