import pytest
from methods import from_cache, random_string


@pytest.allure.feature('Требование №2. Клиент может ждать ответа не более 1 сек (после этого он отвалится по таймауту), но может перезапрашивать значение несколько раз.')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_requirement_2(config):

    timeout = 1
    attempts = 10
    with pytest.allure.step('Делаем запрос с таймаутом {} сек'.format(timeout)):
        key = random_string()
        for i in range(attempts):
            response = from_cache(key, config, timeout)
            if response:
                break
        else:
            assert False, 'Было произведено {} попыток перезапроса данных. Ни одна из попыток не оказалась успешной (все отвалились по таймауту)'.format(attempts)
