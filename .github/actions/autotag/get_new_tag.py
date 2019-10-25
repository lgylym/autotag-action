import datetime
import os
import sys


def new_version(most_recent_version: str):
    branch = os.environ.get("GITHUB_REF")
    current_year, current_week, _ = datetime.date.today().isocalendar()
    current_version = 0

    old_year, old_week, old_version = most_recent_version.strip().split(".")
    old_year = int(old_year)
    old_week = int(old_week)
    old_version = int(old_version)

    if old_year == current_year and old_week == current_week:
        current_version = old_version + 1
    new_tag = f"{current_year}.{current_week}.{current_version}"
    
    if branch and branch != "master":
        new_tag = "test." + new_tag

    print(new_tag)


if __name__ == "__main__":
    for line in sys.stdin:
        new_version(line)
