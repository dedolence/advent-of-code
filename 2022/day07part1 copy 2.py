
class Element():
    """
        Either file or directory
    """
    def __init__(self, name: str, parent: "Dir" = None) -> None:
        self.name = name
        self.parent = parent

class Dir(Element):
    def __init__(self, name: str, parent = None, children: list = [], size: int = 0) -> None:
        self.size = size
        self.type = "(dir)"
        self.children = children
        Element.__init__(self, name, parent)

    def get_size(self):
        return sum([child.get_size() for child in self.children])


class File(Element):
    def __init__(self, name: str, size: int, parent: Dir = None) -> None:
        self.size = size
        self.type = "(file)"
        Element.__init__(self, name, parent)

    def get_size(self):
        return self.size


class Instruction():
    def __init__(self, line_number, line) -> None:
        self.line_number = line_number
        self.operation = line.split()[1]
        if self.operation == "cd":
            self.target = line.split()[2]


commands: list[Instruction] = []
dirs: list[Dir] = [Dir("/")]
files: list[File] = []
all_elements = {}
cursor = 0  # cursor keeps track of position within console output
working_dir_stack = []
raw_lines = [line.strip() for line in open("inputs/day7.txt").readlines()]

# parse each line of the console output as either an instruction or an element
for i in range(0, len(raw_lines)):
    if raw_lines[i][0] == "$":
        ins = Instruction(i, raw_lines[i])
        commands.append(ins)
    
    if raw_lines[i][0].isnumeric():
        new_file = File(raw_lines[i].split()[1], int(raw_lines[i].split()[0]))
        files.append(new_file)
        all_elements[new_file.name] = new_file

    if raw_lines[i][:3] == "dir":
        new_dir = Dir(raw_lines[i].split()[1])
        dirs.append(new_dir)
        all_elements[new_dir.name] = new_dir

# iterate through the instructions.
# keep track of the working directory, then add everything after a ls command
# to the working directory's children
for ins in commands:
    cursor = ins.line_number
    if ins.operation == "cd":
        if ins.target == "..":
            working_dir_stack.pop()
        else:
            temp_dict = dict((dir.name, dir) for dir in dirs)
            working_dir_stack.append(temp_dict[ins.target])
    
    if ins.operation == "ls":
        children = []
        working_dir = working_dir_stack[-1:][0]
        for line in raw_lines[cursor:]:
            if "cd" in line.split():
                break
            if "ls" not in line.split():
                temp_dict = dict((file.name, file) for file in files)
                element = all_elements[line.split()[1]]
                element.parent = working_dir
                children.append(element)
        working_dir.children = children

small_dirs = []
for dir in dirs:
    dir_size = dir.get_size()
    if dir_size <= 100000:
        small_dirs.append(dir_size)

print(sum(small_dirs))