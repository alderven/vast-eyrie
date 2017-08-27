import pytest


@pytest.allure.feature('Требование №1. Сервис не должен пятисотить или падать. Сервис должен отвечать всегда в одном формате.')
@pytest.allure.story('Требование №1.1. Сервис не должен пятисотить или падать')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_requirement_11(responses):

    with pytest.allure.step('Проверяем коды ответов.'):
        for response in responses:
            code = response.status_code
            assert code < 500, 'Сервис получил код возврата: {}. Согласно требованию №1.1: "Сервис не должен пятисотить или падать"'.format(code)


@pytest.allure.feature('Требование №1. Сервис не должен пятисотить или падать. Сервис должен отвечать всегда в одном формате.')
@pytest.allure.story('Требование №1.2. Сервис должен отвечать всегда в одном формате.')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_requirement_12(responses):

    with pytest.allure.step('Проверяем форматы ответов.'):
        types = set()
        for response in responses:
            types.add(response.headers['Content-Type'])
        assert len(types) == 1, 'Форматы ответов: {}. Согласно требованию №1.2: "Сервис должен отвечать всегда в одном формате."'.format(types)
