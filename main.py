import csv
import glob
import os
import tkinter as tk
from tkinter import filedialog


def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory()  # Show the dialog to choose a directory
    root.destroy()
    return directory


def read_csv_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return list(csv.reader(file, delimiter=';'))
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='ISO-8859-1') as file:
            return list(csv.reader(file, delimiter=';'))


def consolidate_csv_correctly(directory, output_filename):
    files_pattern = os.path.join(directory, '*.csv')
    output_file = os.path.join(directory, output_filename)

    headers_set = False
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = None

        for filename in glob.glob(files_pattern):
            lines = read_csv_file(filename)
            if len(lines) <= 5:  # Skip files with not enough lines
                continue

            for _ in range(4):  # Skip first four lines
                lines.pop(0)

            if not headers_set:
                headers = lines.pop(0)  # Read headers
                writer = csv.writer(outfile)  # Default delimiter is comma
                writer.writerow(headers)
                headers_set = True
            else:
                lines.pop(0)  # Skip the headers in subsequent files

            writer.writerows(lines)  # Write data

    return f"Consolidation complete. File saved as {output_file}"


# GUI for selecting directory
directory = select_directory()
if directory:
    output_filename = 'corrected_consolidated.csv'
    consolidation_message = consolidate_csv_correctly(directory, output_filename)
    print(consolidation_message)
else:
    print("No directory selected. Operation cancelled.")
