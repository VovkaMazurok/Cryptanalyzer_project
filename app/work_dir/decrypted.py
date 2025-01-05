from app.work_dir.reading_text_from_file import file_reading
from app.work_dir.writing_text_to_file import file_recording


def decryption_text(ALPHABET_FOR_CODING: str, encrypted_file_name: str, decrypted_file_name: str, key: int) -> None:  # noqa: N803
    text = file_reading(encrypted_file_name)
    encryption_lst = []
    for leter in text:
        if leter in ALPHABET_FOR_CODING:
            index_of_leter = ALPHABET_FOR_CODING.index(leter)
            encryption_lst.append(ALPHABET_FOR_CODING[(index_of_leter - key) % len(ALPHABET_FOR_CODING)])
        elif leter == "\n":
            encryption_lst.append("\n")  # Зберегти символ нового рядка
        else:
            # Обробка випадку, коли символ не знайдено в ALPHABET_FOR_CODING
            # Пропускаємо символ символ
            continue
    decryption_text = "".join(encryption_lst)
    file_recording(decrypted_file_name, decryption_text)
