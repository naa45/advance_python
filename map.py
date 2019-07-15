names=["john","kofi","ama"]
print(list(map(len,names)))

def sqrt(x): return x**2
print(list(map(sqrt,map(len,names))))


items=[1,2,3,4,5]
squares=map((lambda x:x**2),items)
print(list(squares))


def too_old(x):return x>30
ages=[23,45,16,56,67]
print(list(filter(too_old,ages)))


  
