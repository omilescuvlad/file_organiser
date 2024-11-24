# File Organiser

File Organiser is a Python-based script designed to help you organize files within a directory based on their extensions. It's a simple yet effective way to declutter and arrange your workspace.

## Features

- Automatically categorizes files into folders based on their extensions.
- Supports various file types, making it adaptable for diverse use cases.
- Lightweight and easy to integrate into existing workflows.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/omilescuvlad/file_organiser.git
   cd file_organiser
### Ensure Python 3.x is installed on your system.

### Usage
Place the files you want to organise in a new folder with the name "files".<br>
Place the script in the directory you want to organize or specify the target directory within the script.

Run the script:
   ```bash
   python file_organiser.py
   ```

Files will be moved into newly created folders named after their extensions (e.g., .txt, .jpg, .pdf).

### Example

Before running the script:

example/<br>
├── document.txt<br>
├── photo.jpg<br>
├── report.pdf<br>
After running the script:

example/<br>
├── txt/<br>
│   └── document.txt<br>
├── jpg/<br>
│   └── photo.jpg<br>
├── pdf/<br>
    └── report.pdf<br>
    
### Technologies Used
Python 100%


