def user_name_validation(user_name):
    if user_name == None:
        '''
        raise : 例外を発生させる命令
        ValueError : 例外型のオブジェクトを指定
        引数 : 例外オブジェクトの引数にはメッセージを指定できる
        '''
        raise ValueError('名前が設定されていません')