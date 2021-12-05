def fnc3(a, b, c):
    d = 0
    return a + b + c

arg_names = fnc3.__code__.co_varnames[:fnc3.__code__.co_argcount]
print(arg_names)

print(fnc3.__code__.co_varnames)