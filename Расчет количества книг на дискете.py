page_count = 100
line_count = 50
letter_count = 25
symbol_size = 4  # Количество байт для хранения одного символа
disc_size = 1.44  # Информационный объем дискеты в Мб

disc_size_byte = disc_size * 1024 * 1024  # Информационный объем дискеты в байтах

book_count = disc_size_byte / (page_count * line_count * letter_count * symbol_size)
complete_book_count = int(book_count / 1)  # Количество целых помещающихся книг

print("Количество книг, помещающихся на дискету:", complete_book_count)
