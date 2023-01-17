# тип данных bool, соддержит два значение -> True и False
a = True is False  # False
# булевые оператор, and, or, not
b = 55 > 1 or 88 > 65 and 78 == 78 and 98 == 98 is not True  # True
# приоритет or операторов, с большего до маленького - 1, and - 2, not - 3.
# bool -> функция переобразование в логическое значение 0 -> False, 1 -> True. "" - False, != "" == True
c, d = bool(1), bool(0)  # True, false
# ==, !=, >, >=, <, <=, is, is not, in, not in, одинаковый приоритет, слева на право.
e = 95 >= 55  # False

print(a, b, c, d, e, sep=", ")
