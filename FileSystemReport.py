import os

start = "C:\\users\\bcsmi\\AppData\\Local"

def main():
    print("Dir: " + start)
    for dir in [os.path.join(start,dI) for dI in os.listdir(start) if os.path.isdir(os.path.join(start,dI))]:
        size = getSizes(dir)
        if size > 0.5:
            print(f"{dir:<152}  {size:>7.1f}GB")
            
        

def getSizes(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            size += os.stat(os.path.join(root, file)).st_size
    return size / (1024.0 ** 3)







if __name__ == "__main__":
    main()