import os
import constants


folder_to_scan = "C:\\users\\bcsmi\\AppData\\Local"
# Can be constants.(B|KB|MB|GB|TB)
size_units = constants.GB
# Size threshold of which folders to display in `size_units`
folder_size_threshold = 0.5


def main():
    print("Dir: " + folder_to_scan)
    for dir in [os.path.join(folder_to_scan, dI)
                for dI in os.listdir(folder_to_scan)
                if os.path.isdir(os.path.join(folder_to_scan, dI))]:

        size = getSizes(dir)
        if size > folder_size_threshold:
            print(f"{dir:<152}  {size:>7.1f}{size_units[0]}")


def getSizes(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            size += os.stat(os.path.join(root, file)).st_size
    return size / (1024.0 ** size_units[1])







if __name__ == "__main__":
    main()