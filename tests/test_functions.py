from main_folder.functions import getting_json_from_web, finding_ides, key_in_list


def test_getting_json_from_web():
    link = 'https://jsonplaceholder.typicode.com/posts'
    result = getting_json_from_web(link)
    assert isinstance(result, list)
    assert len(result) > 0

def test_finding_ides():
    file = [{'id': 1, 'state': 'EXECUTED', 'date': '2021-08-01T00:00:00'},
            {'id': 2, 'state': 'EXECUTED', 'date': '2021-08-02T00:00:00'},
            {'id': 3, 'state': 'PENDING', 'date': '2021-08-03T00:00:00'},
            {'id': 4, 'state': 'EXECUTED', 'date': '2021-08-04T00:00:00'},
            {'id': 5, 'state': 'EXECUTED', 'date': '2021-08-05T00:00:00'}]
    result = finding_ides(file, quantity=3, sort_type=True)
    assert isinstance(result, list)
    assert len(result) == 3
    assert result == [5, 4, 2]

def test_key_in_list_value_without_whitespace():
    # Проверяем случай, когда значение в словаре не содержит пробельных символов
    key = 'key'
    list_ = {'key': 'name'}
    assert key_in_list(key, list_) == ''



