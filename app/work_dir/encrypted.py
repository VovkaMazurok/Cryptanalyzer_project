from app.work_dir.writing_text_to_file import file_recording


def encryption_text(text: str, ALPHABET_FOR_CODING: str, file_name, key: int) -> None:  # noqa: N803
    r"""Шифрує заданий текст за допомогою шифру Цезаря та викликає функцію для запису в файл.

    Функція здійснює шифрування для кожного символу тексту, який належить
    до зазначеного алфавіту (ALPHABET_FOR_CODING). Символи, які не входять
    до алфавіту (зокрема пробіли та спеціальні символи, крім перенесення рядків),
    пропускаються. Перенесення рядків (\n) також зберігаються у зашифрованому тексті.
    """
    encryption_lst = []
    for leter in text:
        if leter in ALPHABET_FOR_CODING:
            index_of_leter = ALPHABET_FOR_CODING.index(leter)
            encryption_lst.append(ALPHABET_FOR_CODING[(index_of_leter + key) % len(ALPHABET_FOR_CODING)])
        elif leter == "\n":
            encryption_lst.append("\n")  # Зберегти символ нового рядка
        else:
            # Обробка випадку, коли символ не знайдено в ALPHABET_FOR_CODING
            # Пропускаємо символ символ
            continue
    encryption_text = "".join(encryption_lst)
    file_recording(file_name, encryption_text)
