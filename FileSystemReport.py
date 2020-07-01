"""Calculate the size of all the files in each subdirectory.

Arguments to change:
    directory_to_scan:          Directory to list the size of subdirectories.
    size_units:                 Size (B|KB|MB|GB|TB) to use in calculations.
    directory_size_threshold:   Ignore directorys with size less than this.
    decimal_places:             Number of decimal places for size rounding.
"""
import os
import constants

directory_to_scan = "C:\\users\\bcsmi\\AppData\\Local"
size_units = constants.GB
directory_size_threshold = 0.5
decimal_places = 2


def run_size_scan(starting_dir):
    """Scan all subdirectories in `starting_dir` and calculate their size."""
    print("Dir: " + starting_dir)
    for dir in [os.path.join(starting_dir, dI)
                for dI in os.listdir(starting_dir)
                if os.path.isdir(os.path.join(starting_dir, dI))]:

        size = getSizes(dir)
        if size > directory_size_threshold:
            print(f"{dir:<152}  {size:>7.{decimal_places}f}{size_units[0]}")


def getSizes(dir):
    """Walk through every file in `dir` and sum the sizes."""
    size = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            size += os.stat(os.path.join(root, file)).st_size
    return size / (1024.0 ** size_units[1])


if __name__ == "__main__":
    run_size_scan(directory_to_scan)
