"""
Yikes!
Create a mini file system?
Linked-list style:
dir a {
    parent: /
    children:
        [
            dir b
            file x
            file y
        ]
    folder size: sum(children + children's children)
}

what is known:
    - every dir will have a parent (except /)
    - every file will have a size and a parent
    - every file will have a ls before it (as opposed to a cd)
    - multiple cd commands in a row

what could be:
    - ls could reveal an empty folder (ls immediately followed by another instruction)
    - could be multiple of any commands: "ls ls cd" could be a valid command


"""
input = []
file_tree = {}
dir_tree = {"/": {"name": "/", "parent": None, "children": [], "size": 0}}
instructions = [] # [[line_number, command, target], [..], ...] e.g. [[6, 'cd', 'a]]: at line 6 cd to a
line_num = 0
cmds = ["cd", "ls"]
# first pass creates empty directories and unattached files
for line in open(0):
    input.append(line.strip())

    if "$" in line:
        instructions.append([line_num] + line.split()[1:])

    if "dir" in line:
        dir_tree[line.split()[1]] = {"name": line.split()[1], "parent": None, "children": [], "size": 0}

    if line[0].isnumeric():
        file_tree[line.split()[1]] = {"parent": None, "size": line.split()[0]}
    line_num += 1


working_dir = None
parent_dir = dir_tree["/"]

""" for i in range(0, len(input)):
    if "cd" in input[i]:
        if ".." in input[i]:
            working_dir = parent_dir
            parent_dir = parent_dir["parent"]
        else:
            parent_dir = working_dir
            working_dir = dir_tree[input[i].split()[2]]
            working_dir["parent"] = parent_dir
        print("working dir: ", working_dir) """

def perform(i):
    current_instruction = instructions[i]
    line_number = current_instruction[0]

    if current_instruction[1] == "ls":
        # read ahead until the next command, accumulating each line
        for line in input[i:]:
            if line.split()[0] not in cmds:
                working_dir["children"].append(line)


for i in range(0, len(instructions)):
    perform(i)
