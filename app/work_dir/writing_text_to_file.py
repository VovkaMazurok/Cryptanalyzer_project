import pathlib


def file_recording(file_name: str, text: str) -> None:
    """Записує текст у файл.

    Файл створюється в каталозі box_with_documents у кореневій директорії проекту.
    """
    root_dir = pathlib.Path(__file__).resolve().parents[2]
    doc_dir = root_dir / "box_with_documents"
    file_path = doc_dir / file_name
    doc_dir.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as file:
        file.write(text)
