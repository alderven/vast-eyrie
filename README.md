# Общее
Данный проект содержит автотесты для тестирования сервиса https://vast-eyrie-4711.herokuapp.com/?from_cache=123

# Тест кейсы и результаты тестирования
Отчет Allure: https://rawgit.com/alderven/vast-eyrie/master/allure-report/index.html

№  | Описание Тест Кейса | Проверяемое требование | Тест Скрипт | Ссылка на отчет Allure | Ошибка
-- | ------------------- | ---------------------- | ----------- | ---------------------- | -------
1  | Делаем запрос к сервису, проверяем, что получили ответ, и что код ответа не 5** | Требование №1.1 Сервис не должен пятисотить или падать. | [test_requirement1.py](https://github.com/alderven/vast-eyrie/blob/master/test_requirement1.py)  | [Failed](https://rawgit.com/alderven/vast-eyrie/master/allure-report/index.html#behaviors/0b45abcccb7b85437cc44068681cc5e9/acc8f7004195fccc/) | Сервис получил код возврата: 500. Согласно требованию №1.1: "Сервис не должен пятисотить или падать"
2  | Делаем запрос к сервису, проверяем, что формат ответа всегда один и тот же | Требование №1.2 Сервис должен отвечать всегда в одном формате.  | [test_requirement1.py](https://github.com/alderven/vast-eyrie/blob/master/test_requirement1.py)  | [Failed](https://rawgit.com/alderven/vast-eyrie/master/allure-report/index.html#behaviors/8efd6d0afeee0f75dbed779a62deb4cf/b765e1cff732091f/) | Форматы ответов: {'application/json', 'text/html; charset=utf-8'}. Согласно требованию №1.2: "Сервис должен отвечать всегда в одном формате."
3  | Делаем запрос к сервису, ждем не более 1 сек. Перезапрашиваем значение, если не успели получить ответ | Требование №2. Клиент может ждать ответа не более 1 сек (после этого он отвалится по таймауту), но может перезапрашивать значение несколько раз. | [test_requirement2.py](https://github.com/alderven/vast-eyrie/blob/master/test_requirement2.py) | [Passed](https://rawgit.com/alderven/vast-eyrie/master/allure-report/index.html#behaviors/2bf0e692fd4021f086eb5db06ff0b524/2ebfb989a422965/) | –
4  | Делаем несколько запросов, проверяем, есть ли среди них два подряд "error". Если есть, отправляем электронное письмо на ответственным лицам (в зависимости от времени и дня недели отправляем разным людям) | Требование №3. При повторном (2 раза подряд) получении ошибки (ответ 'error') нужно отсылать алерт. В дополнение можно привязать список сотрудников и в нерабочее время слать уведомления об ошибках только дежурному программисту.  | [test_requirement3.py](https://github.com/alderven/vast-eyrie/blob/master/test_requirement3.py) | [Passed](https://rawgit.com/alderven/vast-eyrie/master/allure-report/index.html#behaviors/2e97295db0a89ce30172fede37e01998/314d47367ab9ed74/) | –

# Инсталляция
1. Скачать и распаковать архив с проектом: https://github.com/alderven/vast-eyrie/archive/master.zip
1. Установить Python 3.6 (и выше): https://www.python.org/downloads/
1. Установить следующие библиотики для Python:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * requests: http://docs.python-requests.org/en/master/
   * pytest-allure-adaptor: https://pypi.python.org/pypi/pytest-allure-adaptor
   * configparser: https://pypi.python.org/pypi/configparser
1. Установить Allure Framework: https://docs.qameta.io/allure/latest/

# Как запускать тесты
В командной строке выполнить следующую команду:
```javascript
python -m pytest --alluredir report
```
# Как генерировать Allure отчет:
В командной строке выполнить следующую команду:
```javascript
allure serve full_path_to_report_folder
```
