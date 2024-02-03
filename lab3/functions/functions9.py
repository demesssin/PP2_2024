#Вы можете комбинировать оба типа аргументов в одной функции.
#Все аргументы до / , являются только позиционными, а все аргументы после * - только ключевыми.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(2013, 1996, c = 1976, d = 1979)