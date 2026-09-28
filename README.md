# Log Archive Tool

A Python command-line tool that archives log files by compressing them into timestamped `.tar.gz` files.

The tool accepts a log directory as a command-line argument, creates a compressed archive, stores it in an `archives` directory, and records the archive operation with its date and time.

## Features

* Accepts a log directory through the command line
* Compresses logs into `.tar.gz` format
* Generates timestamped archive filenames
* Automatically creates the archive directory
* Records archive operations with date and time
* Validates the provided directory
* Handles missing, invalid, and empty directories
* Uses Python's built-in libraries

## Techniques Used

* Python
* `argparse` — command-line argument handling
* `tarfile` — TAR/GZIP compression
* `pathlib` — file and directory handling
* `datetime` — timestamp generation

## Project Structure

```text
Log Archive Tool/
│
├── log_archive.py
├── README.md
├── .gitignore
└── logs/
    ├── app.log
    ├── server.log
    └── error.log
```

Generated files are intentionally excluded from Git using `.gitignore`.

## How to Run

Make sure Python is installed:

```bash
python --version
```

Run the tool by providing the log directory:

```bash
python log_archive.py logs
```

## Example Output

```text
Archive created successfully: archives\logs_archive_20260928_153012.tar.gz
```

The generated archive will be stored in:

```text
archives/
└── logs_archive_20260928_153012.tar.gz
```

## Archive Contents

The generated `.tar.gz` file contains the original log directory and its files:

```text
logs/
├── app.log
├── server.log
└── error.log
```

## Error Handling

The tool checks for common problems, including:

* Directory does not exist
* Provided path is not a directory
* Directory is empty
* Permission errors
* Archive creation errors

For example:

```text
Error: 'abc' does not exist.
```

## Verification

The generated archive can be inspected using:

```bash
tar -tzf archives/logs_archive_YYYYMMDD_HHMMSS.tar.gz
```

It can also be extracted using:

```bash
tar -xzf archives/logs_archive_YYYYMMDD_HHMMSS.tar.gz
```

## Future Improvements

Possible future versions could include:

* Scheduled execution using Linux `cron`
* Automatic deletion of archives older than a specified number of days
* Email or Slack notifications
* Uploading archives to remote servers
* Uploading archives to cloud storage such as Amazon S3
* Docker support
* CI/CD using GitHub Actions
