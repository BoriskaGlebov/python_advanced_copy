"""
Реализуйте контекстный менеджер, который будет игнорировать переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, то он прокидывается выше.
"""

from typing import Collection, Type, Literal
from types import TracebackType


class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.err_type = errors

    def __enter__(self) -> None: ...

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[True] | None | False:
        if exc_type is None or issubclass(exc_type, tuple(self.err_type)):
            # if exc_type:
            # print("Exception {} has been handled".format(exc_type))
            return True
        return False


if __name__ == "__main__":
    # err_types = {ZeroDivisionError, TypeError}
    # with BlockErrors(err_types):
    #     a = 1 / 0
    # print('Выполнено без ошибок')

    # err_types = {ZeroDivisionError}
    # with BlockErrors(err_types):
    #     a = 1 / '0'
    # print('Выполнено без ошибок')

    # outer_err_types = {TypeError}
    # with BlockErrors(outer_err_types):
    #     inner_err_types = {ZeroDivisionError}
    #     with BlockErrors(inner_err_types):
    #         a = 1 / '0'
    #     print('Внутренний блок: выполнено без ошибок')
    # print('Внешний блок: выполнено без ошибок')

    err_types = {Exception}
    with BlockErrors(err_types):
        a = 1 / "0"
    print("Выполнено без ошибок")
