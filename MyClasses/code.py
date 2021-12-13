class A:
    def __init__(self):
        print(f'Constructor A Class')

class B(A):
    def __init__(self):
        print(f'Constructor B Class')

class C(B):
    def __init__(self):
        print(f'Constructor C Class')

class D(C):
    def __init__(self):
        super(D,self).__init__()
        print(f'Constructor D Class')


def main():
    obj = D()

if __name__ == "__main__":
    main()