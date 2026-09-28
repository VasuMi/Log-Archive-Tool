import argparse
import tarfile
from pathlib import Path
from datetime import datetime


parser = argparse.ArgumentParser(
    description="Archive log files into a compressed tar.gz file."
)

parser.add_argument(
    "log_directory",
    help="Directory containing the log files"
)

args = parser.parse_args()

log_directory = Path(args.log_directory)

# Check if the path exists
if not log_directory.exists():
    print(f"Error: '{log_directory}' does not exist.")
    exit(1)

# Check if the path is actually a directory
if not log_directory.is_dir():
    print(f"Error: '{log_directory}' is not a directory.")
    exit(1)

# Check if the directory contains files
if not any(log_directory.iterdir()):
    print(f"Error: '{log_directory}' is empty.")
    exit(1)

# Create archive directory
archive_directory = Path("archives")
archive_directory.mkdir(exist_ok=True)

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create archive name
archive_name = f"logs_archive_{timestamp}.tar.gz"

# Complete archive path
archive_path = archive_directory / archive_name

try:
    # Create compressed archive
    with tarfile.open(archive_path, "w:gz") as archive:
        archive.add(log_directory, arcname=log_directory.name)

    # Record archive operation
    log_file = Path("archive_log.txt")

    with log_file.open("a") as file:
        file.write(
            f"{datetime.now()} - "
            f"Archived {log_directory} -> {archive_path}\n"
        )

    print(f"Archive created successfully: {archive_path}")

except PermissionError:
    print("Error: Permission denied.")

except Exception as error:
    print(f"Error while creating archive: {error}")