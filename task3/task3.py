import json


def rep_form(tests_, values_j_):
    # функция формирует список для репорта
    report_ = []
    # проходимся по тестам из tests.json
    for tests_dict in tests_:
        value_rep = value_search(tests_dict['id'], values_j_) # ищем статус теста по id с помощью функции
        # если нет вложенных тестов, заполняем как есть и переходим к следующему
        if 'values' not in tests_dict.keys():
            report_.append({'id': tests_dict['id'],
                            'title': tests_dict['title'],
                            'value': value_rep})

        else:
            # если есть вложенные тесты, то вызываем эту же функцию рекурсивно
            report_.append({'id': tests_dict['id'],
                            'title': tests_dict['title'],
                            'value': value_rep,
                            'values': rep_form(tests_dict['values'], values_j_)})

    return report_


def value_search(test_id, values):
    # ищет значение теста по id в values.json, подразумевая, что он отсортирован по id
    # в противном случае можно закомментить elif
    value = ''
    for values_dict in values:
        if values_dict['id'] == test_id:
            value = values_dict['value']
            break
        elif values_dict['id'] > test_id:
            break
    return value


tests_file = input('Введите путь к файлу tests.json: ')
value_file = input('Введите путь к файлу values.json: ')
vf = open(value_file, 'r')
tf = open(tests_file, 'r')

# списки с входными данными
values_j = json.load(vf)['values']
tests = json.load(tf)['tests']

# получение списка, который запишем в report.json
report = rep_form(tests, values_j)

vf.close()
tf.close()
with open('report.json', 'a') as rf:
    rf.writelines(json.dumps({"tests": report}, indent=2))
print('Отчет сохранен как report.json')
