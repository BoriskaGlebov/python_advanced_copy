"""
Удобно сохранять логи в определённом формате, чтобы затем их можно было фильтровать и анализировать. 
Сконфигурируйте логгер так, чтобы он писал логи в файл skillbox_json_messages.log в следующем формате:

{"time": "<время>", "level": "<уровень лога>", "message": "<сообщение>"}

Но есть проблема: если в message передать двойную кавычку, то лог перестанет быть валидной JSON-строкой:

{"time": "21:54:15", "level": "INFO", "message": "“"}

Чтобы этого избежать, потребуется LoggerAdapter. Это класс из модуля logging,
который позволяет модифицировать логи перед тем, как они выводятся.
У него есть единственный метод — process, который изменяет сообщение или именованные аргументы, переданные на вход.

class JsonAdapter(logging.LoggerAdapter):
  def process(self, msg, kwargs):
    # меняем msg
    return msg, kwargs

Использовать можно так:

logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Сообщение')

Вам нужно дописать метод process так, чтобы в логах была всегда JSON-валидная строка.
"""

import json
import logging


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        new_message = json.dumps(msg, ensure_ascii=False)
        return new_message, kwargs


if __name__ == "__main__":
    logger = JsonAdapter(logging.getLogger(__name__))
    logging.basicConfig(
        level=logging.DEBUG,
        filename="skillbox_json_messages.log",
        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
        datefmt="%H:%M:%S",
    )
    logger.setLevel(logging.DEBUG)
    logger.info("Сообщение")
    logger.error('Кавычка)"')
    logger.info('"')
    logger.debug("Еще одно сообщение")
    # with open('skillbox_json_messages.log', 'r') as file:
    #
    #     for el in file.readlines():
    #         print(el)
    #         d = json.loads(el)
    #         print(d['time'])
    #         print(d['level'])
    #         print(d['message'])
    #         print('*'*50)
