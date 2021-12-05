from inspect import signature

def f(foo, bar='hello'):
    pass

def g(*args, **kwargs):
    pass
    

def main():
    print(f'hello world')
    sig = signature(f)
    sig_g = signature(g)
    print(sig.parameters)
    
    # 辞書型のオブジェクトとして保持しているため名前をキーとしてアクセスする
    print(sig.parameters['foo'])
    
    tmp = sig.parameters['foo'].name
    print(f'foo name : {tmp}')
    
    tmp = sig.parameters['foo'].default
    print(f'foo default value : {tmp}')
    
    tmp = sig.parameters['bar'].default
    print(f'bar default value : {tmp}')
    
    # パラメータがどのような使われ方をしているか
    tmp = sig.parameters['foo'].kind
    print(f'foo kind : {tmp}')
    
    # *args, **kwargs といった可変長引数のときは VAR_POSITIONAL や VAR_KEYWORD になる
    tmp = sig_g.parameters['args'].kind
    print(f'*args kind : {tmp}')

    tmp = sig_g.parameters['kwargs'].kind
    print(f'**kwargs kind : {tmp}')

if __name__ == "__main__":
    main()