file = open("inputs/day7.txt")
input = [line.strip() for line in file.readlines()]

all_dirs = []
dirs = {}
def get_dir(name):
    """
        Checks if a dir already exists and returns it; creates it if not.
    """
    if name not in all_dirs:
        dir = {"name": name, "size": 0}
        dirs[name] = dir
        all_dirs.append(name)
        return dir
    else:
        return dirs[name]
    

working_dir_stack = []
accumulate = False
line_num = 0
for line in input:
    line_num += 1
    if "$ cd " in line:
        accumulate = False
        sym, ins, name = line.split()
        if name == "..":
            working_dir_stack.pop()
        else:
            dir = get_dir(name)
            if dir is not None:
                working_dir_stack.append(dir)
        continue 
    
    if "$ ls" in line:
        accumulate = True
        continue
    
    if accumulate:
        line = line.split()
        if line[0].isnumeric():
            for dir in working_dir_stack:
                dir["size"] += int(line[0])

t = 0
for dir in dirs:
    dir_size = dirs[dir]["size"]
    if dir_size <= 100000:
        t += dir_size

print(t)