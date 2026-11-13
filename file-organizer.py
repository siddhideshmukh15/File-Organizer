
import os
import shutil

print("===== FILE ORGANIZER =====")

folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

if os.path.isdir(folder):
    files = os.listdir(folder)

    print("\n===== PREVIEW =====")

    for file in files:
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()
            category = "Others"

            for name, extensions in file_types.items():
                if extension in extensions:
                    category = name
                    break

            print(file, "->", category)

    confirm = input("\nOrganize files? (yes/no): ")

    if confirm.lower() == "yes":
        for file in files:
            file_path = os.path.join(folder, file)

            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1].lower()
                category = "Others"

                for name, extensions in file_types.items():
                    if extension in extensions:
                        category = name
                        break

                new_folder = os.path.join(folder, category)
                os.makedirs(new_folder, exist_ok=True)

                destination = os.path.join(new_folder, file)

                if os.path.exists(destination):
                    print("Skipped duplicate:", file)
                    continue

                shutil.move(file_path, destination)
                print("Moved:", file)

        print("\nOrganization completed!")

    else:
        print("Organization cancelled!")

else:
    print("Invalid folder path!")

