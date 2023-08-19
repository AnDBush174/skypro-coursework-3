from main_folder.functions import getting_json_from_web, finding_ides, key_in_list


def test_getting_json_from_web():
    # Устанавливаем ссылку на веб-страницу с JSON данными
    link = 'https://jsonplaceholder.typicode.com/posts'

    # Вызываем функцию для получения JSON данных с веб-страницы
    result = getting_json_from_web(link)

    # Проверяем, что результат является списком
    assert isinstance(result, list)

    # Проверяем, что список не пустой (содержит хотя бы один элемент)
    assert len(result) > 0


def test_finding_ides():
    # Создаем пример JSON файла
    file = [{'id': 1, 'state': 'EXECUTED', 'date': '2021-08-01T00:00:00'},
            {'id': 2, 'state': 'EXECUTED', 'date': '2021-08-02T00:00:00'},
            {'id': 3, 'state': 'PENDING', 'date': '2021-08-03T00:00:00'},
            {'id': 4, 'state': 'EXECUTED', 'date': '2021-08-04T00:00:00'},
            {'id': 5, 'state': 'EXECUTED', 'date': '2021-08-05T00:00:00'}]

    # Вызываем функцию для поиска уникальных идентификаторов в файле
    # Параметр quantity указывает, сколько уникальных идентификаторов нужно найти (в данном случае 3)
    # Параметр sort_type указывает, нужно ли отсортировать идентификаторы (в данном случае True)
    result = finding_ides(file, quantity=3, sort_type=True)

    # Проверяем, что результат является списком
    assert isinstance(result, list)

    # Проверяем, что длина списка равна заданной (в данном случае 3)
    assert len(result) == 3

    # Проверяем, что список содержит правильные уникальные идентификаторы, отсортированные в порядке убывания
    assert result == [5, 4, 2]


def test_key_in_list_value_without_whitespace():
    # Проверяем случай, когда значение в словаре не содержит пробельных символов

    # Устанавливаем ключ и словарь, где значение не содержит пробельных символов
    key = 'key'
    list_ = {'key': 'name'}

    # Вызываем функцию для получения значения по ключу из словаря
    result = key_in_list(key, list_)

    # Проверяем, что результат равен пустой строке
    assert result == ''




