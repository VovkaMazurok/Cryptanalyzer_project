from app.work_dir.constants import DEFAULT_ENCRYPTION_TEXT


def get_text() -> str:
    """Метод для отримання тексту з консолі abo використання тексту за замовчуванням."""
    text = input("Enter text in one line: ")
    if not text:
        text = DEFAULT_ENCRYPTION_TEXT
    return text
