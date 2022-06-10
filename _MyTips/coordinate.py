WIDTH = 3

def converter(x:int, y:int) -> int:
    if x > WIDTH or x < 0:
        return -1
    return y*WIDTH + x

def rconverter(index:int) -> dict:
    if WIDTH <= 0:
        return -1
    return {'x':index%WIDTH,
            'y':index//WIDTH
            }



print(f'{converter(1,8)}')
print(f'{rconverter(25)}')