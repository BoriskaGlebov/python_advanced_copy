"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

from types import TracebackType
from typing import Type, Literal, IO
import sys
import traceback


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.new_stdout = None if stdout is None else stdout
        self.new_stderr = None if stderr is None else stderr

    def __enter__(self):
        if self.new_stdout is not None:
            self.old_stdout = sys.stdout
            sys.stdout = self.new_stdout
        if self.new_stderr is not None:
            self.old_stderr = sys.stderr
            sys.stderr = self.new_stderr

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[True] | None:

        if self.new_stdout == self.new_stderr:
            sys.stderr.write(traceback.format_exc())
            self.new_stderr.close()
            sys.stderr = self.old_stderr
            sys.stdout = self.old_stdout
            return True
        if self.new_stdout is not None:
            self.new_stdout.close()
            sys.stdout = self.old_stdout
        if self.new_stderr is not None:
            sys.stderr.write(traceback.format_exc())
            self.new_stderr.close()
            sys.stderr = self.old_stderr
        return True


if __name__ == "__main__":
    print("Hello stdout")
    stdout_file = open("stdout.txt", "w")
    stderr_file = open("stderr.txt", "w")

    with Redirect(stdout=None, stderr=stderr_file):
        print("Hello stdout.txt")
        raise Exception("Hello stderr.txt")

    print("Hello stdout again")
    raise Exception("Hello stderr")
