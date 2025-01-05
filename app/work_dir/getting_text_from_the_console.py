import sys

from app.work_dir.constants import DEFAULT_ENCRYPTION_TEXT


def get_text_from_console() -> str:
    """Зчитує весь текст із стандартного вводу (sys.stdin).

    Чекає на багаторядковий текст до завершення введення EOF (Ctrl+D або Ctrl+Z).
    """
    print("Введіть текст. Для завершення введення натисніть Ctrl+D або Ctrl+Z (для Windows):")
    text = sys.stdin.read()
    if not text:
        text = DEFAULT_ENCRYPTION_TEXT
    return text
