from app.work_dir.constants import ALPHABET_FOR_CODING, DECRYPTED_FILE, ENCRYPTED_FILE
from app.work_dir.decrypted import decryption_text
from app.work_dir.encrypted import encryption_text
from app.work_dir.getting_text_from_the_console import get_text_from_console
from app.work_dir.getting_the_key import get_key


def main() -> None:
    print("Hello from cryptanalyzer-project!")
    choice = int(
        input("If you want encode text, enter: 1\nIf you want decode text, enter: 2\nEnter your choice: "),
    )
    if choice == 1:
        key = get_key()
        text = get_text_from_console()
        encryption_text(text, ALPHABET_FOR_CODING, ENCRYPTED_FILE, key)
    elif choice == 2:
        key = get_key()
        decryption_text(ALPHABET_FOR_CODING, ENCRYPTED_FILE, DECRYPTED_FILE, key)
