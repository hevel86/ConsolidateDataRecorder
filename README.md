# CSV Consolidation Tool

## Overview

This Python tool consolidates multiple CSV files into a single file. It is designed to handle CSV files where data starts from line 5 and originally uses semicolons (`;`) as separators. The consolidated file will use commas (`,`) as separators.

## Requirements

- Python 3.x
- tkinter (for the GUI directory selection)

## Usage

1. **Running the Script**: Execute the script in a Python environment. A GUI window will open for directory selection.

2. **Selecting Directory**: Use the GUI to select the directory containing your CSV files.

3. **Output**: The script will create a consolidated CSV file named `corrected_consolidated.csv` in the same directory, with data entries separated by commas.

## How It Works

- The script reads each CSV file in the selected directory, assuming they use `;` as a delimiter.
- The first four lines of each file are skipped, as data starts from line 5.
- Headers are read from the first file, and subsequent files' headers are ignored.
- Data from all files is consolidated under these headers.
- The output file is created using `,` as a delimiter.

## Notes

- Ensure that all CSV files in the directory have the same structure and headers.
- The script handles files encoded in UTF-8 and falls back to ISO-8859-1 in case of encoding issues.

## Troubleshooting

- **Encoding Errors**: If you encounter encoding errors, check if your CSV files have a consistent encoding format.
- **Missing Data**: Ensure that all files follow the expected format with data starting from line 5.

## License

This tool is open-source and free to use.
