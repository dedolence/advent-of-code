class Element():
    def __init__(self, name: str, parent: "Dir" = None) -> None:
        self.name = name
        self.parent = parent

class Dir(Element):
    def __init__(self, name: str, parent = "Dir", children: list = []) -> None:
        self.children = children
        Element.__init__(self, name, parent)


class File(Element):
    def __init__(self, name: str, size: int, parent: Dir = None) -> None:
        self.size = size
        Element.__init__(self, name, parent)


class Instruction():
    def __init__(self, line_number, line) -> None:
        self.line_number = line_number
        self.type = line.split()[1]
        if self.type == "cd":
            self.target = line.split()[2]

    @classmethod
    def do(cls):
        pass


def cd(destination):
    print("changing directory to ", destination)


def ls(working_dir):
    print("listing directory of ", working_dir)

commands = []
dirs = []
files = []
def parse_console_output():
    # parsed_console is a list of classes that represent each line of the console output (puzzle input)
    raw_lines = [line.strip() for line in open("inputs/test.txt").readlines()]
    for i in range(0, len(raw_lines)):
        if raw_lines[i][0] == "$":
            ins = Instruction(i, raw_lines[i])
            commands.append(ins)
        
        if raw_lines[i][0].isnumeric():
            files.append(File(raw_lines[i].split()[1], raw_lines[i].split()[0]))

        if raw_lines[i][:3] == "dir":
            dirs.append(Dir(raw_lines[i].split()[1]))

    return commands

for ins in parse_console_output():
    print(ins.type)