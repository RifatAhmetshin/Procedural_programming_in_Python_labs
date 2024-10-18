# TODO Найдите количество книг, которое можно разместить на дискете
volume_1 = 1.44 * (1024 ** 2)
n_page_in_book = 100
n_str_in_page = 50
n_symbol_in_str = 25
volume = 4
n_book = n_page_in_book * n_str_in_page * n_symbol_in_str * volume
a = int(volume_1 // n_book)
print("Количество книг, помещающихся на дискету:", a)
