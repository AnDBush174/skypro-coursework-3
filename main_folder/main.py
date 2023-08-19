from functions import getting_json_from_web, finding_ides, key_in_list


def main():
    link = "https://www.jsonkeeper.com/b/5CJU"

    # Получение JSON данных с веб-страницы
    file = getting_json_from_web(link)

    # Поиск уникальных идентификаторов в данных JSON
    list_of_id = finding_ides(file)

    for idefic in list_of_id:
        for item in file:
            if len(item) != 0 and item['id'] == idefic:
                if item["state"] == "EXECUTED":
                    time_data = item['date'].split('T')
                    date_ = time_data[0].split('-')
                    normal_date = f"{date_[2]}.{date_[1]}.{date_[0]}"
                    disc = item['description']
                    abs_from = key_in_list('from', item)
                    to = item['to'].split(' ')
                    num_of_trans = to[1]
                    summ = item["operationAmount"]["amount"]
                    cur = item["operationAmount"]["currency"]["name"]

                    # Вывод информации о выполненной операции
                    print(f"""{normal_date} {disc}\n{abs_from}"""
                          f"""{to[0]} **{num_of_trans[-4:]}\n{summ} {cur}\n""")
                elif item["state"] == "CANCELED":
                    disc = item['description']

                    # Вывод информации об отмененной операции
                    print(f"{disc} - Операция отменена")


if __name__ == "__main__":
    main()



