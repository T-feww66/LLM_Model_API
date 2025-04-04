from pathlib import Path

def find_files_by_keyword(folder_path: str, keyword: str):
    """
    Tìm các file trong thư mục có chứa keyword trong tên.
    """
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Thư mục không tồn tại: {folder_path}")
        return []

    return [str(f) for f in folder.glob("*") if f.is_file() and keyword.lower() in f.name.lower()]