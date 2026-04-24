# File Organizer CLI

A command-line tool written in Python that automatically organizes files inside a directory by sorting them into subfolders based on their file extension.

---

## Features

- Automatic file organization by extension
- Customizable configuration via JSON file
- **Dry-run mode** (simulate actions without modifying files)
- Logging to both console and file
- Automatic handling of duplicate filenames

---

## Tech Stack

- Python 3
- Standard Library only:
    - argparse
    - pathlib
    - logging
    - shutil
    - json

## Project Structure

```bash
. 
├── config/ 
│   └── config.example.json 
├── src/ 
│   ├── cli.py 
│   ├── main.py 
│   ├── organizer.py 
│   └── utils.py 
├── .gitignore 
├── README.md
```

> Note: some files and directories are generated at runtime and are not tracked by Git

---

## Setup

Clone the repository:

```bash
git clone https://github.com/carmineb-dev/file-organizer.git
cd file-organizer
```

(Optional) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate # Linux / Mac
.venv\\Scripts\\activate # Windows
```
---

## Configuration

The configuration file is not included in the repository
Create your local config starting from the example:

```bash
cp config/config.example.json config/config.json
``` 

Example configuration:
```json
{
    ".jpg": "Images",
    ".pdf": "Documents",
    ".mp4": "Videos",
    ".txt": "Text"
}
```

- Key -> file extension
- Value -> target folder
- Default -> Altro (fallback folder for unmatched extensions)

---

## Usage

Run the script from the project root:

```bash
python src/main.py --path "/path/to/folder"
``` 

**Options**
- --path -> (required) directory to organize
- --dry-run -> simulate the operation without moving files

**Example**
```bash
python src/main.py --path "./Downloads" --dry-run
``` 
---

## How It Works

1. Parses CLI arguments
2. Load configuration from config.json
3. Scans all files in the target directory
4. Matches file extensions to destination folders
5. Handles duplicates by renaming files (file_01.ext, file_02.ext,...)
6. Moves files or simulates the process in dry-run mode

---

## Logging

Logs are:
- printed to the console
- saved to:
    logs/app.log

The logs/ directory is automatically created at runtime

--- 

## Limitations

- No recursive directory scanning (only top-level files)
- No undo / rollback feature
- Requires proper filesystem permissions

---

## Future Improvements

- Recursive directory support
- Undo / rollback functionality
- CLI installation via pip
- Advanced filters
- GUI version

---

## Author

Developed as part of my personal portfolio