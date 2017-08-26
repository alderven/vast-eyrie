import pytest
from methods import send_alert


@pytest.allure.feature('''Требование №3. При повторном (2 раза подряд) получении ошибки (ответ "error") нужно отсылать алерт.
* В дополнение можно привязать список сотрудников и в нерабочее время слать уведомления об ошибках только дежурному программисту.''')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_requirement_3(responses, config):

    with pytest.allure.step('Проверяем ответы на наличие повторной ошибки "error".'):
        previous_error = False
        for response in responses:
            if 'error' in response.text and previous_error:
                msg = 'Два раза подряд была получена ошибка (ответ "error"). URL запроса: {}'.format(response.url)
                send_alert(msg, config)
                assert False, msg
            elif 'error' in response.text:
                previous_error = True
            else:
                previous_error = False
