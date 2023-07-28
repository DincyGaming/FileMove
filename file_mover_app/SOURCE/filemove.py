import os
import shutil
import tkinter as tk
from tkinter import filedialog

# The rest of your file-moving code here
# ...

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


def on_select_folder():
    folder_path = filedialog.askdirectory()
    entry_dest_directory.delete(0, tk.END)
    entry_dest_directory.insert(tk.END, folder_path)

def on_start_moving():
    destination_directory = entry_dest_directory.get()
    word_to_match = entry_word_to_match.get()
    find_and_move_files(destination_directory, word_to_match)
    lbl_status.config(text="File moving process complete!")

# Create the main application window
app = tk.Tk()
app.title("File Mover App")
app.geometry("400x200")

# Create the GUI elements
lbl_dest_directory = tk.Label(app, text="Destination Directory:")
lbl_dest_directory.pack(pady=5)
entry_dest_directory = tk.Entry(app, width=40)
entry_dest_directory.pack(pady=5)
btn_browse = tk.Button(app, text="Browse", command=on_select_folder)
btn_browse.pack(pady=5)

lbl_word_to_match = tk.Label(app, text="Word to Match in File Names:")
lbl_word_to_match.pack(pady=5)
entry_word_to_match = tk.Entry(app, width=40)
entry_word_to_match.pack(pady=5)

btn_start_moving = tk.Button(app, text="Start Moving", command=on_start_moving)
btn_start_moving.pack(pady=10)

lbl_status = tk.Label(app, text="", fg="green")
lbl_status.pack(pady=5)

# Keep the GUI window open
app.mainloop()
