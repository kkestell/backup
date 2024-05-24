import json
import subprocess
import os
import glob


def rsync(job):
    home_directory = os.path.expanduser("~")
    input_paths = job["input_paths"]
    output_directory = job["output_directory"]
    excludes = job.get("excludes", [])

    exclude_flags = []
    for exclude in excludes:
        exclude_flags.extend(["--exclude", exclude])

    for pattern in input_paths:
        expanded_paths = glob.glob(pattern)
        for path in expanded_paths:
            relative_path = os.path.relpath(path, start=home_directory)
            input_path = os.path.join(home_directory, ".", relative_path)
            if os.path.isdir(input_path):
                output_path = output_directory
            else:
                output_path = os.path.join(output_directory, relative_path)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            args = ["-avz", "--compress-level=9", "--delete", "--delete-excluded", "--no-links"]
            subprocess.run(["rsync"] + args + exclude_flags + [input_path, output_path])


if __name__ == "__main__":
    config_directory = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    config_file_path = os.path.join(config_directory, "backup", "config.json")
    with open(config_file_path, "r") as file:
        data = json.load(file)
        jobs = data["jobs"]
        for job in jobs:
            rsync(job)
