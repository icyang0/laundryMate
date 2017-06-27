import fileinput, sys
for line in fileinput.input("test.txt", inplace=True):
    line = line.replace("cleaned", "dry cleaned")
    # sys.stdout is redirected to the file
    sys.stdout.write(line)