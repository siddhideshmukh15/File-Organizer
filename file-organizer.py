
from pathlib import Path

folder_path = Path(input("Enter folder path: "))

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".java", ".c", ".html"],
    "Archives": [".zip", ".rar"]
}

if folder_path.exists() and folder_path.is_dir():
    count = 0

    for file in folder_path.iterdir():
        if file.is_file():
            extension = file.suffix.lower()

            for folder, extensions in file_types.items():
                if extension in extensions:
                    new_folder = folder_path / folder
                    new_folder.mkdir(exist_ok=True)

                    destination = new_folder / file.name

                    if destination.exists():
                        print(file.name, "already exists!")
                        break

                    file.rename(destination)
                    print(file.name, "moved to", folder)

                    count += 1
                    break

    print("\nTotal files organized:", count)

else:
    print("Invalid folder path!")
