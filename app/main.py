from app.work_dir.constants import ALPHABET_FOR_CODING
from app.work_dir.encrypted import encryption_text
from app.work_dir.getting_of_text import get_text
from app.work_dir.getting_the_key import get_key


def main() -> None:
    print("Hello from cryptanalyzer-project!")
    key = get_key()
    text = get_text()
    encryption_text(text, ALPHABET_FOR_CODING, key)
