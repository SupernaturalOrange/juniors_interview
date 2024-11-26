from typing import Dict, Optional

import requests
from requests import Response

from task2.solution.settings.settings import Settings
from task2.solution.tools.exception_classes import BadResponseException


def get_response_with_settings(
    settings: Settings, additional_param: Optional[Dict[str, str]] = None
) -> Response:
    """
    Функция сделает запрос исходя из базовых настроек и дополнительных query параметров.

    :param settings: Настройки (экземпляр класса Settings).
    :param additional_param: Дополнительные query параметры.
    :return: Вернёт объект Response, если статус-код 200, иначе вызовет исключение BadResponseException.
    """
    base_param = settings.https.base_params
    param = dict()
    param.update(base_param)
    if additional_param:
        param.update(additional_param)
    response = requests.get(settings.https.url, params=param)
    if response.status_code != requests.codes.ok:
        raise BadResponseException(
            f"Что-то пошло не так. Неожиданно получили статус-код {response.status_code}"
        )
    return response
