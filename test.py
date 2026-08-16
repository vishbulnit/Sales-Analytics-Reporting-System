
missing = set(["abc", "xyz", "mno"]) - set(["abc", "xyz"])
print(missing)
print(set(["abc", "xyz", "mno"]))


"""
def add_deco(func):

    def wrapper(*args, **kwargs):
        print("two number were givne as input to add.")
        result = func(*args, **kwargs)
        print(result)
        print("operation finished.")
        
    return wrapper

@add_deco
def add(a, b):
    return a + b

add(5, 6)

"""