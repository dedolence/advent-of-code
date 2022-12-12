file = open("inputs/day7.txt")
input = [line.strip() for line in file.readlines()]

# assumption:
# input can be broken up into groups of:
#   $ cd (any number of lines)
#   $ ls (once)
#   int or "dir" (any number of lines)
# so input can be broken into chunks separated by whatever
# comes before a "$ cd" that isn't another "$ cd"
# then iterate through chunks, setting a working dir
# according to the "cd"s
# every cd adds a child to that dir

all_dirs = []
def get_dir(name):
    """
        Checks if a dir already exists; creates it if not.
    """
    dir = {"name": name, "size": 0}
    if len(all_dirs) > 0:
        if name in list(map(lambda d: d["name"], all_dirs)):
            return
    all_dirs.append(dir)
    return dir

working_dir_stack = []
accumulate = False
for line in input:
    if "$ cd " in line:
        accumulate = False
        sym, ins, name = line.split()
        if name == "..":
            working_dir_stack.pop()
        else:
            dir = get_dir(name)
            if dir is not None:
                working_dir_stack.append(dir)
        print(working_dir_stack)
        continue 
    
    if "$ ls" in line:
        accumulate = True
        continue
    
    if accumulate:
        line = line.split()
        if line[0].isnumeric():
            for dir in working_dir_stack:
                try:
                    dir["size"] += int(line[0])
                except TypeError:
                    pass
        continue

t = 0
for dir in all_dirs:
    if dir["size"] >= 100000:
        t += dir["size"]

print(t)