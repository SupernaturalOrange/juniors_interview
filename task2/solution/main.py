from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool

from task2.solution.settings.settings import Settings
from task2.solution.tools.csv_tools import write_csv_file
from task2.solution.tools.data_tools import (
    convert_set_list_to_dict_counts,
    get_all_animals,
)


def main(settings: Settings) -> None:
    """
    Задача найти всех животных по алфавиту со страницы в википедии
    и записать в csv файл их статистику (количество животных на каждую букву)

    :param settings: Настройки (экземпляр класса Settings).
    :return: None.
    """
    # Получаем список из интересующих нас букв
    search_letters = list(settings.https.search_letters)
    # Подготавливаем аргументы для поисковой функции.
    input_value = ((settings, letters) for letters in search_letters)
    # В потоках ищем животных сразу на все буквы.
    with ThreadPool(processes=cpu_count()) as threadpool:
        result = threadpool.map(lambda args: get_all_animals(*args), input_value)
    # Конвертируем результат
    statistics = convert_set_list_to_dict_counts(result)
    # Записываем в файл
    write_csv_file(settings, statistics)


if __name__ == "__main__":
    main(Settings())
