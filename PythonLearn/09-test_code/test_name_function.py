from name_function import get_formated_name

def test_first_last_name():
    """能正确处理 ethan fan这个名字吗？"""
    full_name = get_formated_name('ethan', 'fan')
    assert full_name == 'Ethan Fan'

def test_first_last_middle_name():
    """能正确处理 ethan bryant fan 这个名字吗"""
    full_name = get_formated_name('ethan', 'fan', 'bryant')
    assert full_name == 'Ethan Bryant Fan'