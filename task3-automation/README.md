# Task Automation with Python

Three small Python scripts that each automate a simple repetitive task. Made as part of the CodeAlpha internship.

## Scripts

### 1. organize_files.py
Moves all `.jpg` files from `source_images/` into `sorted_images/`.

```bash
python organize_files.py
```

### 2. extract_emails.py
Scans a text file for email addresses and saves the unique ones to a new file.

```bash
python extract_emails.py
```

Input: `sample_data/sample.txt`
Output: `extracted_emails.txt`

### 3. scrape_title.py
Fetches a webpage and saves its title to a text file.

```bash
python scrape_title.py
```

Output: `page_title.txt`

To scrape a different page, change the `url` variable at the top of the script.

## Requirements

```bash
pip install requests
```

(`os`, `shutil`, and `re` are part of Python's standard library — no install needed.)

## Concepts Used

- `os` and `shutil` for file handling and moving files
- `re` for pattern matching (emails, HTML title tag)
- `requests` for fetching webpage content
- Reading and writing files

## Project Structure

```
task-automation/
├── organize_files.py
├── extract_emails.py
├── scrape_title.py
├── sample_data/
│   └── sample.txt
├── requirements.txt
└── README.md
```
