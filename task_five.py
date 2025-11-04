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


str_one = SuperStr("madammadam")
print(f"Первая строка: {str_one}")
print(f"Является ли строка палиндромом: {str_one.is_palindrome()}")
s = "madam"
print(f"Строка может быть получена целым количеством повторов строки {s}: {str_one.is_repeatance(s)}")

str_two = SuperStr("one")
print(f"\nВторая строка: {str_two}")
print(f"Является лм строка палиндромом: {str_two.is_palindrome()}")
s = "one"
print(f"Строка может быть получена целым количеством повторов строки {s}: {str_two.is_repeatance(s)}")

str_three = SuperStr("")
print(f"\nТретья строка (пустая): {str_three}")
print(f"Является ли строка палиндромом: {str_three.is_palindrome()}")
print(f"Строка может быть получена целым количеством повторов строки {str_three} (пустая строка): {str_three.is_repeatance(str_three)}")
