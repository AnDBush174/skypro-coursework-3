import requests

def getting_json_from_web(link):
    """Ф-я получает список словарей по ссылке"""
    file = requests.get(link)
    file = file.json()
    return file

def finding_ides(file, quantity=5, sort_type=True):
    """Ф-я находит id последних операций и возвращает их в правильном порядке"""
    list_of_id = []
    dates = []
    dict_of_dates = {}
    for index in file:
        if len(index) != 0 and index['state'] == "EXECUTED":
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
            dates.append(full_date)
            dict_of_dates[full_date] = index_id

    dates.sort(reverse=sort_type)
    dates = dates[0:quantity]
    for ides in dates:
        list_of_id.append(dict_of_dates[ides])
    return list_of_id

def key_in_list(key, list_):
    if key in list_:
        value = list_[key]
        parts = value.split()
        if len(parts) > 1:
            result = f"{parts[0]} ** **** {parts[-1][-4:]} -> "
        else:
            result = ''
        return result
    return ''
