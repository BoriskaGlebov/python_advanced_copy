"""
Напишите код, который выводит сам себя.
Обратите внимание, что скрипт может быть расположен в любом месте.
"""

import sys

result = 0
for n in range(1, 11):
    result += n**2

# Secret magic code
with open(sys.argv[0]) as me:
    print(me.read())
