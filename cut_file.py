import sys
import os

MIN_GETS = 1001000

def cut_files(path):
    files = os.listdir(path)
    print(files)
    getsFile = path + "/combined_get_stamps.txt"
    putsFile = path + "/combined_put_stamps.txt"

    gets = []
    with open(getsFile, 'r') as f:
        for i, line in enumerate(f):
            gets.append(line.strip())
            if i >= MIN_GETS:
                break

    last_get_time = int(gets[-1].split(' ')[0])

    puts = []
    with open(putsFile, 'r') as f:
        for i, line in enumerate(f):
            puts.append(line.strip())
            put_time = int(line.split(" ")[0])
            if put_time > last_get_time:
                break

    print(f"{len(puts)} puts, {len(gets)} gets")

    outGetsFile = getsFile[:-4] + "_cut.txt"
    outPutsFile = putsFile[:-4] + "_cut.txt"
    with open(outGetsFile, 'w') as f:
        for line in gets:
            f.write(line + "\n")
    with open(outPutsFile, 'w') as f:
        for line in puts:
            f.write(line + "\n")

def traverse(path):
    # 15
    dirs = [x[0] for x in os.walk(path)][1:]
    # cut_files(dirs[0])
    for dir in dirs:
        print(os.listdir(dir))
        print(f"cutting {dir}")
        cut_files(dir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)
    path = sys.argv[1]
    # cut_files(path)
    traverse(path)