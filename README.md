# Fun
This section is only for new testing and fun. Have fun! ;) 

## scan_files.sh
Simple script for scanning directories for files matching a specific pattern.

### Usage
```bash
./scan_files.sh [directory] [pattern]
```
- **directory**: Directory to search (defaults to current directory).
- **pattern**: File name pattern (defaults to `*`).

Example:
```bash
./scan_files.sh /var '*.log'
```

## extract_jpgs.py
A Python utility for extracting embedded JPEG files from a larger binary
file. The script scans for JPEG byte markers and writes each image to a
separate output file named `extracted_<n>.jpg`.

### Usage
```bash
python3 extract_jpgs.py <input_file>
```

Where `<input_file>` is the path to the binary file you want to scan. By
default, running the script directly will attempt to process a file named
`large.jpg` in the current directory.

Example:
```bash
python3 extract_jpgs.py large.jpg
```
