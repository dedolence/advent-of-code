class File():
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __hash__(self) -> int:
        return hash((self.name))

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.size == __o.size


class Dir():
    def __init__(self, name) -> None:
        self.name = name
        self.size = 0
        self.children = []
    
    def __hash__(self) -> int:
        return hash((self.name))

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name

class Ins():
    def __init__(self, line_num, line) -> None:
        self.line_num = line_num
        self.line = line


# get input and parse into lines
with open("inputs/day7.txt") as file:
    input = [line.strip() for line in file]


# parse input, creating files and directories and instructions
dirs = []
files = []
insts = []
for i in range(0, len(input)):
    l = input[i].split()
    if l[0] == "$":
        insts.append(Ins(i, input[i]))

    if l[0] == "$" and l[1] == "cd" and l[2] != "..":
        dir_name = l[2]
        dirs.append(Dir(dir_name))
        dirs = list(set(dirs))

    if l[0].isnumeric():
        file_name = l[1]
        file_size = int(l[0])
        files.append(File(file_name, file_size))


def get_dir(name: str) -> Dir:
    """
        Returns the dir that matches name.
    """
    pass


working_stacks = []
for ins in insts:
    l = ins.line.split()
    stack = working_stacks[-1:]
    if l[1] == "cd":
        if l[2] != "..":
            stack.append(l[2])
        else:
            stack.pop()
    
    if l[1] == "ls":
        # stop here and accumulate the following lines until the next
        # cd instruction is reached.
        stack.append("ls")
        continue

for stack in working_stacks:
    print(stack)