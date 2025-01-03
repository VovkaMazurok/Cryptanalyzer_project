import pathlib


def encryption_text(text: str, ALPHABET_FOR_CODING: str, key: int) -> None:  # noqa: N803
    encryption_lst = []
    for leter in text:
        if leter in ALPHABET_FOR_CODING:
            index_of_leter = ALPHABET_FOR_CODING.index(leter)
            encryption_lst.append(ALPHABET_FOR_CODING[(index_of_leter + key) % len(ALPHABET_FOR_CODING)])
        else:
            # Handle the case where the character is not found in ALPHABET_FOR_CODING
            # Skip the character
            continue
        index_of_leter = ALPHABET_FOR_CODING.index(leter)
        encryption_lst.append(ALPHABET_FOR_CODING[(index_of_leter + key) % len(ALPHABET_FOR_CODING)])
    encryption_text = "".join(encryption_lst)
    root_dir = pathlib.Path(__file__).resolve().parents[2]
    doc_dir = root_dir / "box_with_documents"
    file_path = doc_dir / "ENCRYPTED.txt"
    doc_dir.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as file:
        file.write(encryption_text)
