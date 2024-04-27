# **Проверка файла person.py**

### Проверка методов:

1. ##### get_age

   Было:

        def get_age(self) -> int:
            now: datetime.datetime = datetime.datetime.now()
            return self.yob - now.year

   Возраст возвращается отрицательным.
   Стало:

        def get_age(self) -> int:
            now: datetime.datetime = datetime.datetime.now()
            return now.year - self.yob

2. ##### set_name
   Было:

        def set_name(self, name: str) -> None:
            self.name = self.name
   Имя не обновлялось.

   Стало:

        def set_name(self, name: str) -> None:
            self.name = name


3. ##### set_address

   Было:

         def set_address(self, address: str) -> None:
            self.address == address

   Не меняется адрес
   Стало:

         def set_address(self, address: str) -> None:
            self.address = address
      
4. ##### is_homeless

   Было:

        def is_homeless(self) -> bool:
            '''
            returns True if address is not set, false in other case  
            '''
            return address is None
   Некорректно оформленный docstring 
   Возникает ошибка при вызове(переменная неопределена) 
   
   Стало:
         
         def is_homeless(self) -> bool:
            """returns True if address is not set, false in other case"""
            if self.address is not None:
               return False
            return True