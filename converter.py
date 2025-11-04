import os
import sys

def rename_files(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and '-' in filename:
            # Split on last '-', keep the part after
            new_filename = filename.split('-', 1)[-1]
            new_file_path = os.path.join(folder_path, new_filename)

            if new_file_path != file_path:
                if os.path.exists(new_file_path):
                    print(f"Skipping '{filename}': target '{new_filename}' already exists.")
                    continue

                os.rename(file_path, new_file_path)
                print(f"Renamed '{filename}' → '{new_filename}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rename_files.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        rename_files(folder_path)