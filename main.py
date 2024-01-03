import csv
import glob
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
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
            if len(lines) <= 9:
                continue

            for _ in range(4):
                lines.pop(0)

            if not headers_set:
                headers = lines.pop(0)
                writer = csv.writer(outfile)
                writer.writerow(headers)
                headers_set = True
            else:
                lines.pop(0)

            writer.writerows(lines)

    return output_file


def generate_scatterplot(file_path):
    # Adjust the format string to match your timestamp format
    date_format = "%Y %m %d %H:%M:%S:%f"
    data = pd.read_csv(file_path, delimiter=',')
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], format=date_format, errors='coerce')

    # Calculate statistics for numeric columns only
    stats = data.select_dtypes(include=['number']).agg(['mean', 'median', 'std', 'min', 'max'])

    # Plotting
    plt.figure(figsize=(15, 7))
    for column in data.columns[1:]:  # Skip 'Timestamp' column
        if data[column].dtype in ['float64', 'int64'] and not column.startswith('Unnamed'):
            stat_text = (f"{column} - Avg: {stats[column]['mean']:.2f}, "
                         f"Median: {stats[column]['median']:.2f}, "
                         f"Std: {stats[column]['std']:.2f}, "
                         f"Min: {stats[column]['min']:.2f}, "
                         f"Max: {stats[column]['max']:.2f}")
            plt.scatter(data['Timestamp'], data[column], label=stat_text)

    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.title('Scatter Plot of CSV Data with Statistics')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def generate_linegraph(file_path):
    # Adjust the format string to match your timestamp format
    date_format = "%Y %m %d %H:%M:%S:%f"
    data = pd.read_csv(file_path, delimiter=',')
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], format=date_format, errors='coerce')

    # Calculate statistics for numeric columns only
    stats = data.select_dtypes(include=['number']).agg(['mean', 'median', 'std', 'min', 'max'])

    # Plotting
    plt.figure(figsize=(15, 7))
    for column in data.columns[1:]:  # Skip 'Timestamp' column
        if data[column].dtype in ['float64', 'int64'] and not column.startswith('Unnamed'):
            stat_text = (f"{column} - Avg: {stats[column]['mean']:.2f}, "
                         f"Median: {stats[column]['median']:.2f}, "
                         f"Std: {stats[column]['std']:.2f}, "
                         f"Min: {stats[column]['min']:.2f}, "
                         f"Max: {stats[column]['max']:.2f}")
            plt.plot(data['Timestamp'], data[column], label=stat_text)

    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.title('Line Graph of CSV Data with Statistics')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main execution
directory = select_directory()
if directory:
    output_filename = 'corrected_consolidated.csv'
    consolidated_file = consolidate_csv_correctly(directory, output_filename)
    print(f"Consolidation complete. File saved as {consolidated_file}")
    generate_scatterplot(consolidated_file)
else:
    print("No directory selected. Operation cancelled.")
