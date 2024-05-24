import subprocess
import os
import sys


def restore_from_directory(input_directory, output_directory):
    subprocess.run(["rsync", "-avz", "--compress-level=9", input_directory + "/", output_directory + "/"])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: restore.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.isdir(input_directory):
        print(f"Error: Provided input path is not a directory.")
        sys.exit(1)

    if not os.path.isdir(output_directory):
        print(f"Error: Provided output path is not a directory.")
        sys.exit(1)

    restore_from_directory(input_directory, output_directory)
