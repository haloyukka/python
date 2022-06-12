import pytest
from src import code

def test_user_name_validation():
    '''
    with句で例外処理の関数を呼ぶ
    '''
    with pytest.raises(ValueError) as e:
        code.user_name_validation(None)
    assert str(e.value) == '名前が設定されていません'