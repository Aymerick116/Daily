import os
import subprocess
from datetime import datetime

# Your local path to the cloned repo
REPO_PATH = os.path.expanduser("~/Daily")  # Change this if cloned elsewhere
FILENAME = "daily_commit_log.txt"

def run(command):
    """Run a shell command inside the repo folder."""
    result = subprocess.run(command, cwd=REPO_PATH, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ Error:", result.stderr.strip())
    else:
        print("✅", result.stdout.strip())

def make_daily_commit():
    os.chdir(REPO_PATH)

    # Append timestamp to the log file
    with open(FILENAME, "a") as f:
        f.write(f"Daily commit on {datetime.now()}\n")

    # Git commands
    run("git add .")
    run(f'git commit -m "Daily commit: {datetime.now().strftime("%Y-%m-%d")}"')
    run("git push")

if __name__ == "__main__":
    make_daily_commit()
