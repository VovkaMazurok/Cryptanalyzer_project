from app.work_dir.constants import ALPHABET_FOR_CODING
from app.work_dir.encrypted import encryption_text
from app.work_dir.getting_of_text import get_text
from app.work_dir.getting_the_key import get_key


def main() -> None:
    r"""Шифрує заданий текст за допомогою шифру Цезаря та записує результат у файл.

    Функція здійснює шифрування для кожного символу тексту, який належить
    до зазначеного алфавіту (ALPHABET_FOR_CODING). Символи, які не входять
    до алфавіту (зокрема пробіли та спеціальні символи, крім перенесення рядків),
    пропускаються. Перенесення рядків (\n) також зберігаються y зашифрованому тексті.
    Після шифрування результат записується y файл ENCRYPTED.txt, який
    створюється в каталозі box_with_documents y кореневій директорії проекту.
    """
    print("Hello from cryptanalyzer-project!")
    choice = int(
        input("If you want encode text, enter: 1\n" "If you want decode text, enter: 2\n" "Enter your choice: "),
    )
    if choice == 1:
        key = get_key()
        text = get_text()
        encryption_text(text, ALPHABET_FOR_CODING, key)
    elif choice == 2:
        pass
