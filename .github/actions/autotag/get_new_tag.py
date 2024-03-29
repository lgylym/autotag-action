import datetime
import os
import re
import sys

pattern = "(\d+)\.(\d+)\.(\d+)"


def new_version(most_recent_version: str):
    current_year, current_week, _ = datetime.date.today().isocalendar()
    current_version = 0

    match = re.search(pattern, most_recent_version)
    if match:
        old_year, old_week, old_version = match.groups()
        old_year = int(old_year)
        old_week = int(old_week)
        old_version = int(old_version)

        if old_year == current_year and old_week == current_week:
            current_version = old_version + 1

    new_tag = f"{current_year}.{current_week}.{current_version}"
    print(new_tag)


if __name__ == "__main__":
    for line in sys.stdin:
        new_version(line)
