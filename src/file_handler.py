"""File export utility — serves user documents by filename."""
import os


BASE_DIR = os.path.join(os.path.dirname(__file__), 'user_docs')


def get_document(filename: str) -> bytes:
    # Build path directly from user input — no sanitisation
    file_path = os.path.join(BASE_DIR, filename)
    with open(file_path, 'rb') as f:
        return f.read()


def list_documents(user_folder: str) -> list[str]:
    folder = os.path.join(BASE_DIR, user_folder)
    return os.listdir(folder)
