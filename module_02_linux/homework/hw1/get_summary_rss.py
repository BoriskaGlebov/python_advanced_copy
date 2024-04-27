"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

import os.path


def size_name(size: int, count: int = 0) -> tuple:
    """
    Рекурсивная функция поиска размера файла
    :param size: размер файла
    :param count: считает сколько раз вызывалась функция и так выбирается размерность для файла
    :return: кортеж (размер в формате строки , единица измерений )
    """
    name = ["Б", "кБ", "MБ", "ГБ"]
    counter = count
    if size > 1024:
        size /= 1024
        counter += 1
        res = size_name(size, counter)
        return res
    else:
        return str(round(size, 2)), name[counter]


def get_summary_rss(ps_output_file_path: str) -> str:
    """
    функция опрерделяет размер занимаемой памяти процессами системы
    :param ps_output_file_path: путь к файлу для анализа
    :return: строка о занимаемой памяти
    """
    with open(ps_output_file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        tot_mem_use = 0
        for line in lines[1:]:
            memory_use = int(line.split()[5])
            tot_mem_use += memory_use
        si_tot_mem_use = size_name(tot_mem_use)
        out_str = f"Всего использовано памяти: {" ".join(si_tot_mem_use)}"
        return out_str


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))
    path: str = os.path.join(dir_path, "output_file.txt")
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
