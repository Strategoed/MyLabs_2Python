def CreateSFile(path, path2):
    file = open(path, "r")
    old_lines = file.read().splitlines()
    file.close()
    new_file = open(path2, "w")
    for i in range(len(old_lines)):
        old_lines[i] = str(len(old_lines[i])) + ": " + old_lines[i]
    new_file.write('\n'.join(old_lines))
    new_file.close()

def OutputFile(path):
    file = open(path, "r")
    file_cont = file.read()
    file.close()
    print("\n" + path + ":\n")
    print(file_cont)

def CreateFFile(path):
    print("Input lines\nPress <ENTER> for end line\nPress ';' for end file input\n")
    lines = []
    while True:
        line = input()
        if line.find(";") != -1:
            lines.append(line[0:-2])
            break
        else:
            lines.append(line)
    file = open(path, "w")
    file.write('\n'.join(lines))
    file.close()