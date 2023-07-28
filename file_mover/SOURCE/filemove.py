import os
import shutil

def find_and_move_files(dest_directory, search_word):
    subfolder_path = os.path.join(dest_directory, search_word)

    if not os.path.exists(subfolder_path):
        print(f"The destination subfolder '{search_word}' does not exist in '{dest_directory}'. Please create it first.")
        return

    current_directory = os.getcwd()  # Get the current working directory

    for filename in os.listdir(current_directory):
        if os.path.isfile(filename) and search_word in filename:
            src_filepath = os.path.join(current_directory, filename)
            dest_filepath = os.path.join(subfolder_path, filename)

            # Move the file to the subfolder
            shutil.move(src_filepath, dest_filepath)
            print(f"Moved {filename} to {subfolder_path}")

if __name__ == "__main__":
    destination_directory = r"C:\Users\Intern07\Desktop\file_mover\TARGET"
    word_to_match = "202"  # Replace this with the word you want to match

    find_and_move_files(destination_directory, word_to_match)
