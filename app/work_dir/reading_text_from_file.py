import pathlib


def file_reading(encrypted_file_name: str) -> str:
    """Читає текст з файлу.

    Файл знаходиться в каталозі box_with_documents у кореневій директорії проекту.
    """
    root_dir = pathlib.Path(__file__).resolve().parents[2]
    doc_dir = root_dir / "box_with_documents"
    file_path = doc_dir / encrypted_file_name
    doc_dir.mkdir(parents=True, exist_ok=True)
    with open(file_path) as file:
        return file.read()
