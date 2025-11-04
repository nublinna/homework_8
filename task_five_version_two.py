class SuperStr(str):
    def is_repeatance(self, s):
        if len(s) == 0 or len(self) == 0:
            return False
        if len(self) % len(s) != 0:
            return False
        repeat_count = len(self) // len(s)
        return s * repeat_count == self

    def is_palindrome(self):
        str_low = self.lower()
        if str_low == str_low[::-1] or len(self) == 0:
            return True
        else:
            return False

while True:
    user_input = input("Выберите режим программы: "
                       "\n1 -- Проверка строки на палиндром"
                       "\n2 -- Выход из программы: ")
    if user_input == "1":
        str_one = input("Введите строку: ")
        str_one = SuperStr(str_one)
        print(f"Первая строка: {str_one}")
        print(f"Является ли строка палиндромом: {str_one.is_palindrome()}")
        s = input("Введите вторую строку: ")
        print(f"Строка может быть получена целым количеством повторов строки {s}: {str_one.is_repeatance(s)}")
    if user_input == "2":
        break


