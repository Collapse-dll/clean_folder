import sys
from pathlib import Path
import shutil


CATEGORIES = {"Video": [".avi", ".mp4", ".mov", ".mkv"],
              "Images": [".jpeg", ".png", ".jpg", ".svg"],
              "Docs": [".docx", ".txt", ".pdf", ".rtf"],
              "Audio": [".mp3", ".wav", ".flac", ".wma"],
              "Archive": [".zip", ".gz", ".rar"]}


def move_file(file:Path, category:str, root_dir:Path):
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    new_path = target_dir.joinpath(file.name)
    if not new_path.exists():
        file.replace(new_path)


def get_categories(file:Path) -> str:
    ext = file.suffix.lower()
    for cat, exst in CATEGORIES.items():
        if ext in exst:
            return cat
    return 'Other'


def sort_folder(path:Path, elements=[]):
    for element in path.glob('**/*'):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)


def delete_empty_folders(path: Path):
    for folder in path.glob("**/*"):
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()


def extract_archives(path: Path):
    for archive in path.glob("**/*"):
        if archive.is_file() and archive.suffix.lower() in [".zip", ".gz", ".rar"]:
            target_dir = archive.with_suffix("")
            target_dir.mkdir(exist_ok=True)
            shutil.unpack_archive(str(archive), str(target_dir))


def main() -> str :
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return 'No path to folder'

    if not path.exists():
        return 'Folder does not exists'
    
    sort_folder(path)
    delete_empty_folders(path)
    extract_archives(path)

    return 'All Ok !'


if __name__ == '__main__':
    print(main())