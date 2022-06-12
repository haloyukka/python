from src import code

def get_json_data_mock(id):
    return {'name':'MiyakoYoshika'}

def test_get_user_names(monkeypatch):
    '''
    第1引数:モックに差し替えたいモジュール
    第2引数:モックに差し替えたい関数名の文字列
    第3引数:実際に置き換えるモックの関数
    '''
    monkeypatch.setattr(
        code, 'get_json_data', get_json_data_mock)
    result = code.get_user_names(['001','009'])

    assert list(result.keys()) == ['001','009']
    assert list(result.values()) == ['MiyakoYoshika','MiyakoYoshika']