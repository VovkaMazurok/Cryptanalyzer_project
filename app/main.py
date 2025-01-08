import string

from app.work_dir.constants import ALPHABET_FOR_CODING, DECRYPTED_FILE, ENCRYPTED_FILE
from app.work_dir.decrypted import decryption_text
from app.work_dir.encrypted import encryption_text
from app.work_dir.getting_text_from_the_console import get_text_from_console
from app.work_dir.getting_the_key import get_key
from app.work_dir.reading_text_from_file import file_reading


def main() -> None:
    print("Hello from cryptanalyzer-project!")
    choice = int(
        input(
            "If you want encode text, enter: 1\nIf you want decode text, enter: 2\nIf you want to use brute force, enter: 3\nEnter your choice: ",
        ),
    )
    if choice == 1:
        key = get_key()
        text = get_text_from_console()
        encryption_text(text, ALPHABET_FOR_CODING, ENCRYPTED_FILE, key)
    elif choice == 2:
        key = get_key()
        decryption_text(ALPHABET_FOR_CODING, ENCRYPTED_FILE, DECRYPTED_FILE, key)
    elif choice == 3:
        brute_force_text = file_reading(ENCRYPTED_FILE)
        dictionary = file_reading("Dictionary_of_english_words.txt").splitlines()
        your_key = 0
        leter_lst = []

        for leter in brute_force_text:
            if leter in ALPHABET_FOR_CODING:
                index_of_leter = ALPHABET_FOR_CODING.index(leter)
                encrypted_letter = ALPHABET_FOR_CODING[(index_of_leter - your_key) % len(ALPHABET_FOR_CODING)]
                leter_lst.append(encrypted_letter.lower())
                if len(leter_lst) > 2:
                    if leter_lst[-1].isspace() or (leter_lst[-2] in string.punctuation and leter_lst[-1].isspace()):
                        if "".join(leter_lst) in dictionary:
                            print("yes")
                            print(f"Your key is: {your_key}")
                            print(leter_lst)
                            break
                    else:
                        your_key += 1
                        leter_lst.clear()
                        continue

                    continue
